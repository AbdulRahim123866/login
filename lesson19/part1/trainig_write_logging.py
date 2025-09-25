"""
log_svc_client.py

A unified, distributed, scalable, and robust logger supporting both local file logging
and distributed log collection via ZeroMQ. Suitable for regular and audit logging in microservice
architectures, with all logic and configuration handled via a single class: MultiPurposeLogger.

Author: [Your Name]
Date: [2025-07-23]
"""

import os
import threading
from typing import Any, Dict, Optional, Union

import yaml
import json
from datetime import datetime
from enum import Enum
import zmq
import time


class LogType(Enum):
    """
    Enum for log type: regular logs (plain text) or audit logs (JSON).
    """
    REGULAR = "regular"
    AUDIT = "audit"


class LoggerRunMode(Enum):
    """
    Enum for logger run mode.
    - LOCAL: Only writes locally to disk.
    - WORKER: Sends logs via ZeroMQ to a collector.
    - COLLECTOR: Receives logs from workers and writes to disk.
    """
    LOCAL = "local"
    WORKER = "worker"
    COLLECTOR = "collector"


class MultiPurposeLogger:
    """
    Unified, thread-safe, distributed logger supporting local, worker, and collector modes.

    Supports in-memory buffering for log entries that fail to be sent or written,
    and basic internal monitoring counters.
    """

    DEFAULT_CONFIG: Dict[str, Any] = {
        "log_path": "logs", # directory
        "log_file_max_size_mb": 10, # max size per file
        "buffer_size": 10,
        "error_buffer_max_size": 250  # max entries kept in RAM if all writes fail
    }

    def __init__(self,
                 service_name: str,
                 log_type: LogType = LogType.REGULAR,
                 mode: LoggerRunMode = LoggerRunMode.LOCAL,
                 config_path: Optional[str] = None,
                 zmq_endpoint: str = "tcp://127.0.0.1:45557",
                 zmq_port: int = 45557):
        """
        Initialize the logger.

        Args:
            service_name: Name of the service (used in log path and file names).
            log_type: Type of logging (REGULAR or AUDIT).
            mode: Operation mode (LOCAL, WORKER, COLLECTOR).
            config_path: Path to optional YAML config file.
            zmq_endpoint: ZeroMQ endpoint string for worker PUSH.
            zmq_port: Port number for collector PULL.
        """
        self.service_name: str = service_name
        self.log_type: LogType = log_type
        self.mode: LoggerRunMode = mode
        self.config: Dict[str, Any] = self._load_config(config_path)
        self._file_lock: threading.RLock = threading.RLock()
        self._current_suffix: str = 'a'
        self._current_hour_dir: Optional[str] = None
        self._current_file_path: Optional[str] = None
        self._current_file: Optional[Any] = None
        self._current_size: int = 0
        self._zmq_endpoint: str = zmq_endpoint
        self._zmq_port: int = zmq_port

        # Error buffering and monitoring
        self._error_buffer: list = []
        self._error_buffer_lock: threading.Lock = threading.Lock()
        self._error_buffer_max_size: int = int(self.config.get("error_buffer_max_size", 5000))
        self.metrics: Dict[str, int] = {
            "log_entries_written": 0,
            "log_entries_failed": 0,
            "log_entries_buffered": 0,
            "log_entries_dropped": 0,
            "batches_sent": 0,
            "batches_failed": 0
        }

        # Mode initialization
        if self.mode == LoggerRunMode.WORKER:
            self._setup_sender()
        elif self.mode == LoggerRunMode.COLLECTOR:
            self._setup_collector()
            self._init_file_writer()
        else:
            self._init_file_writer()

    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """
        Load configuration from YAML file (if present), else use defaults.

        Args:
            config_path: Path to YAML file.

        Returns:
            Configuration dictionary.
        """
        config = self.DEFAULT_CONFIG.copy()
        if config_path and os.path.isfile(config_path):
            with open(config_path, "r") as f:
                yaml_config = yaml.safe_load(f) or {}
                for k, v in yaml_config.items():
                    key = k.lower()
                    if key in config and v is not None:
                        config[key] = v
        config["log_file_max_size_mb"] = int(config["log_file_max_size_mb"])
        config["buffer_size"] = int(config["buffer_size"])
        return config

    def _get_hour_dir(self) -> str:
        """
        Get the log directory for the current hour.

        Returns:
            Path to directory for the current hour.
        """
        hour_str = datetime.now().strftime("%Y%m%d%H")
        return os.path.join(self.config["log_path"], self.service_name, hour_str)

    def _get_log_file(self) -> str:
        """
        Get the full path of the current log file.

        Returns:
            Log file path.
        """
        hour_dir = self._get_hour_dir()
        hour_str = os.path.basename(hour_dir)
        return os.path.join(hour_dir, f"{self.service_name}_{hour_str}_{self._current_suffix}.log")

    def _rotate_if_needed(self, force: bool = False) -> None:
        """
        Rotate log file if needed (new hour, file size exceeded, or forced).

        Args:
            force: Force file rotation.
        """
        hour_dir = self._get_hour_dir()
        hour_changed = hour_dir != self._current_hour_dir
        size_exceeded = (
                self._current_file is not None and
                self._current_size >= self.config["log_file_max_size_mb"] * 1024 * 1024
        )
        need_rotation = force or hour_changed or size_exceeded or (self._current_file is None)
        if need_rotation:
            with self._file_lock:
                if self._current_file:
                    self._current_file.close()
                if hour_changed:
                    self._current_suffix = "a"
                elif size_exceeded:
                    self._current_suffix = chr(ord(self._current_suffix) + 1) if self._current_suffix < 'z' else 'a'
                self._current_hour_dir = hour_dir
                os.makedirs(hour_dir, exist_ok=True)
                self._current_file_path = self._get_log_file()
                self._current_file = open(self._current_file_path, "a", encoding="utf-8", buffering=1)
                self._current_size = os.path.getsize(self._current_file_path)

    def _init_file_writer(self) -> None:
        """
        Prepare file system and open log file for writing.
        """
        os.makedirs(self.config["log_path"], exist_ok=True)
        self._rotate_if_needed(force=True)

    # --------- Worker Mode: ZMQ Sender ---------
    def _setup_sender(self) -> None:
        """
        Initialize ZeroMQ PUSH socket and batching for worker mode.
        """
        self._zmq_context: zmq.Context = zmq.Context()
        self._zmq_socket: zmq.Socket = self._zmq_context.socket(zmq.PUSH)
        self._zmq_socket.connect(self._zmq_endpoint)
        self._batch: list = []
        self._batch_lock: threading.Lock = threading.Lock()
        self._buffer_size: int = self.config["buffer_size"]
        self._flush_thread: threading.Thread = threading.Thread(target=self._flush_loop, daemon=True)
        self._flush_running: bool = True
        self._flush_thread.start()

    def _flush_loop(self) -> None:
        """
        Periodically flush log batches in worker mode.
        """
        while self._flush_running:
            time.sleep(0.5)
            self.flush()

    def log(self, entry: Union[Dict[str, Any], str]) -> None:
        """
        Log a message/record. In WORKER mode, will send batched logs via ZeroMQ.
        In COLLECTOR or LOCAL mode, writes to file directly.
        Uses in-memory buffer for failed writes.

        Args:
            entry: Dictionary (for audit logs) or string (for regular logs).

        Raises:
            RuntimeError: If logger mode is not recognized.
        """
        try:
            # Attempt to flush any buffered logs first
            self._flush_error_buffer()

            if self.mode == LoggerRunMode.WORKER:
                with self._batch_lock:
                    self._batch.append(entry)
                    if len(self._batch) >= self._buffer_size:
                        self._send_batch()
            elif self.mode in (LoggerRunMode.COLLECTOR, LoggerRunMode.LOCAL):
                self._write_log_entry(entry)
            else:
                raise RuntimeError("Unknown logger mode")
        except Exception as ex:
            self._buffer_error_log(entry)
            self.metrics["log_entries_failed"] += 1
            print(f"[WARN] Failed to log entry, buffered in RAM: {ex}")

    def _buffer_error_log(self, entry: Union[Dict[str, Any], str]) -> None:
        """
        Buffer log entry in memory for retry later.
        Oldest entries are dropped if buffer is full.

        Args:
            entry: The log entry.
        """
        with self._error_buffer_lock:
            if len(self._error_buffer) >= self._error_buffer_max_size:
                # Drop oldest
                self._error_buffer.pop(0)
                self.metrics["log_entries_dropped"] += 1
            self._error_buffer.append(entry)
            self.metrics["log_entries_buffered"] += 1

    def _flush_error_buffer(self) -> None:
        """
        Attempt to flush buffered log entries (file or network).
        Should be called at every log() call.
        """
        with self._error_buffer_lock:
            if not self._error_buffer:
                return
            to_retry = self._error_buffer[:]
            self._error_buffer.clear()
        for entry in to_retry:
            try:
                if self.mode == LoggerRunMode.WORKER:
                    with self._batch_lock:
                        self._batch.append(entry)
                        if len(self._batch) >= self._buffer_size:
                            self._send_batch()
                else:
                    self._write_log_entry(entry)
                self.metrics["log_entries_written"] += 1
            except Exception:
                # If retry fails, buffer again (will be retried next call)
                self._buffer_error_log(entry)
                self.metrics["log_entries_failed"] += 1
                print(f"[WARN] Retry to flush buffer failed, entry remains buffered.")

    def _send_batch(self) -> None:
        """
        Send batched logs via ZeroMQ (worker mode). Failed batches are buffered for retry.
        """
        try:
            self._zmq_socket.send_pyobj(self._batch)
            self.metrics["batches_sent"] += 1
            self.metrics["log_entries_written"] += len(self._batch)
            self._batch = []
        except Exception as e:
            print(f"[MultiPurposeLogger] Send error: {e}, buffering unsent batch")
            for entry in self._batch:
                self._buffer_error_log(entry)
            self.metrics["batches_failed"] += 1
            self.metrics["log_entries_failed"] += len(self._batch)
            self._batch = []

    # --------- Collector Mode: ZMQ Receiver ---------
    def _setup_collector(self) -> None:
        """
        Initialize ZeroMQ PULL socket and collector thread.
        """
        self._zmq_context: zmq.Context = zmq.Context()
        self._zmq_socket: zmq.Socket = self._zmq_context.socket(zmq.PULL)
        self._zmq_socket.bind(f"tcp://127.0.0.1:{self._zmq_port}")
        self._collector_thread: threading.Thread = threading.Thread(target=self._collector_loop, daemon=True)
        self._collector_running: bool = False

    def _collector_loop(self, timeout=300) -> None:
        """
        Collector thread: receives log batches and writes to file.
        """
        while self._collector_running:
            try:
                if self._zmq_socket.poll(timeout=timeout) == 0:
                    continue
                message = self._zmq_socket.recv_pyobj()
                if isinstance(message, list):
                    for entry in message:
                        self._write_log_entry(entry)
                else:
                    self._write_log_entry(message)
            except Exception as e:
                print(f"[MultiPurposeLogger] Collector error: {e}")

    def start(self) -> "MultiPurposeLogger":
        """
        Start the collector (collector mode only).

        Returns:
            self, for chaining.
        """
        if self.mode == LoggerRunMode.COLLECTOR:
            self._collector_running = True
            self._collector_thread.start()
        return self

    def stop(self) -> None:
        """
        Stop the collector (collector mode) or flush and close files (other modes).
        """
        if self.mode == LoggerRunMode.COLLECTOR:
            self._collector_running = False
            if self._collector_thread.is_alive():
                self._collector_thread.join(timeout=2.0)
            if self._zmq_socket:
                self._zmq_socket.close()
            if self._zmq_context:
                self._zmq_context.term()
        if hasattr(self, "_flush_running"):
            self._flush_running = False
            if self._flush_thread.is_alive():
                self._flush_thread.join(timeout=1.0)
            self.flush()
        self.close()

    # ---- File Writing (all modes) ----
    def _write_log_entry(self, entry: Union[Dict[str, Any], str]) -> None:
        """
        Write a log entry to disk, rotating files as needed.

        Args:
            entry: Dictionary (for audit) or string (for regular logs).
        """
        with self._file_lock:
            self._rotate_if_needed()
            try:
                if self.log_type == LogType.AUDIT:
                    log_entry = dict(entry)
                    log_entry.setdefault('timestamp', datetime.now().isoformat())
                    log_entry.setdefault('service', self.service_name)
                    log_line = json.dumps(log_entry) + "\n"
                else:
                    log_line = f"{datetime.now().isoformat()} {str(entry)}\n"
                self._current_file.write(log_line)
                self._current_file.flush()
                self._current_size += len(log_line.encode("utf-8"))
                self.metrics["log_entries_written"] += 1
            except Exception as ex:
                # Buffer entry for retry later
                self._buffer_error_log(entry)
                self.metrics["log_entries_failed"] += 1
                print(f"[WARN] File write failed, entry buffered: {ex}")
            self._current_size += len(log_line.encode("utf-8"))

    def flush(self) -> None:
        """
        Flush log buffer (worker mode only) and any buffered failed logs.
        """
        self._flush_error_buffer()
        if self.mode == LoggerRunMode.WORKER:
            with self._batch_lock:
                if self._batch:
                    self._send_batch()

    def close(self) -> None:
        """
        Flush (if needed) and close the current log file.
        """
        self.flush()
        with self._file_lock:
            if self._current_file:
                self._current_file.close()
                self._current_file = None

    def get_metrics(self) -> Dict[str, int]:
        """
        Get a snapshot of logger metrics for monitoring.

        Returns:
            Dictionary with metric counts.
        """
        return self.metrics.copy()

    def __enter__(self) -> "MultiPurposeLogger":
        """
        Enter context (with statement support).

        Returns:
            self
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exit context, ensuring logs are flushed and files closed.
        """
        self.stop()


# 1. Local Logging (Single Process, File Only)
# if __name__ == "__main__":
#     with MultiPurposeLogger(service_name="api", log_type=LogType.REGULAR, mode=LoggerRunMode.LOCAL) as logger:
#         for i in range(10):
#             logger.log(f"Health check event {i}")
#         logger.log("Service started")
#         print("Metrics:", logger.get_metrics())

# 2. Audit Logging (Local Mode, JSON Lines)
# if __name__ == "__main__":
#     with MultiPurposeLogger("myservice", LogType.AUDIT, LoggerRunMode.LOCAL) as logger:
#         logger.log({"event": "user_login", "user_id": 123, "result": "success"})
#         logger.log({"event": "config_reload", "details": {"config_version": 4}})
#         print("Metrics:", logger.get_metrics())
#
# # 3. Distributed Logging: Worker and Collector (Multiple Processes)
# # s1 : Collector Process (central node):

#
# def _workers_example():
#     # s2 : Worker Process (could be started many times):
#     logger = MultiPurposeLogger("myservice002", LogType.REGULAR, LoggerRunMode.WORKER,
#                                 zmq_endpoint="tcp://127.0.0.1:55555")
#     for i in range(100):
#         logger.log({"event": "batch_task", "worker_id": 1, "item": i})
#     logger.close()
#
# if __name__ == "__main__":
#     collector = MultiPurposeLogger("workers_running", LogType.AUDIT, LoggerRunMode.COLLECTOR, zmq_port=55555).start()
#     try:
#         print("Collector running. CTRL+C to stop.")
#
#         while True:
#             # Print stats every 5 seconds
#             import time
#
#             time.sleep(5)
#             _workers_example()
#             # collector.log({"time":time.time()})
#             print("Collector metrics:", collector.get_metrics())
#     except KeyboardInterrupt:
#         pass
#
#     collector.stop()

# # 4. Log Buffering and Error Handling (Simulate Disk Full or Network Down)
if __name__ == "__main__":
    with MultiPurposeLogger("abd_service",LogType.AUDIT,LoggerRunMode.COLLECTOR) as logger:
        for i in range(10):
            logger.log({"name":"abd","age":20})
            print("Matrics: ",logger.get_metrics())
if __name__ == "__main__":
    collector=MultiPurposeLogger("My service",LogType.AUDIT,LoggerRunMode.COLLECTOR,zmq_port=55555).start()
    try:
        print("Collector running. CTRL+C to stop.")
        while True:
            import time
            time.sleep(5)
            collector.log({"time":time.time()})
            # print("Collector metrics:",collector.get_metrics())
    except KeyboardInterrupt:
        pass
    finally:
        collector.stop()
#
# # 5. Get Internal Monitoring Metrics
# if __name__ == "__main__":
#     logger = MultiPurposeLogger("monitored", LogType.REGULAR, LoggerRunMode.LOCAL)
#     logger.log("A test log line")
#     logger.close()
#     print("Logger stats:", logger.get_metrics())
#
# # 6. Context Manager in Distributed Worker (Best Practice)
# if __name__ == "__main__":
#     with MultiPurposeLogger("microservice", LogType.AUDIT, LoggerRunMode.WORKER,
#                             zmq_endpoint="tcp://127.0.0.1:55555") as logger:
#         for i in range(50):
#             logger.log({"action": "call", "call_id": i})
#         print("Worker metrics:", logger.get_metrics())


# # 7. Metrics Monitoring in Real Time
# if __name__ == "__main__":
#     logger = MultiPurposeLogger("metricsvc0101", LogType.REGULAR, LoggerRunMode.LOCAL)
#     for i in range(1000):
#         logger.log(f"metric test {i}")
#         if i % 20 == 0:
#             print(logger.get_metrics())
#         time.sleep(0.01)
#     logger.close()