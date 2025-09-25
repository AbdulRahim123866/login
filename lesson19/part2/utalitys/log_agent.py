"""Advanced and configurable logging utility.

This module provides classes and functions to configure and obtain
loggers with sane defaults for production systems.  It builds on
Python's built‑in ``logging`` module and adds features such as
time‑ and size‑based rotation, memory buffering for error bursts,
and log retention/archival.  Furthermore, the configuration class
supports loading from dictionaries or files and is designed with
immutable defaults to prevent accidental modification.

The ``AdvancedLogger`` class manages the lifecycle of a logger,
including creation of handlers based on the supplied configuration and
cleanup of old log files.  ``LoggerFactory`` exposes a registry of
named loggers to avoid duplication across a process.

New features added in this enhanced version include:

* **Type hints** for all public methods and fields to aid static
  analysis and IDE autocompletion.
* **Comprehensive docstrings** describing the purpose and usage of
  classes and methods.
* An optional **JSON formatter** controlled via configuration.  When
  enabled, log messages are emitted as JSON objects, which can be
  convenient for ingestion by log aggregation systems.
* Optional **tags** attached to the logger configuration.  Tags are
  appended to every log record, allowing extra context to be added.
* A toggle to **enable or disable console logging**.  Many services
  in production environments prefer to suppress console output to
  avoid polluting standard output streams.
* A fix to ``LoggerFactory.configure_from_file`` to correctly use
  ``LoggerConfig.from_file`` instead of the nonexistent
  ``from_json`` method.

This module requires Python 3.9+ for type hinting features such as
``list[str]``.  It uses only standard library modules.  See the
docstrings of individual classes for further details.
"""

from __future__ import annotations

import json
import logging
import logging.handlers
import os
import tarfile
import threading
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any, Dict, Iterable, List, Optional

import yaml


@dataclass(frozen=True)
class LoggerConfig:
    """Configuration for constructing an ``AdvancedLogger``.

    The dataclass uses immutable fields by setting ``frozen=True`` so
    that once created, instances cannot be modified.  This helps
    prevent accidental changes to configuration values at runtime.  Use
    :meth:`from_file` or :meth:`from_dict` to construct configurations
    from external sources.  Defaults are chosen to be sensible for
    development environments.

    Attributes
    ----------
    log_dir : str
        Absolute directory path where log files will be created.  If
        relative, it will be resolved to an absolute path.
    level : str
        Logging threshold level (e.g., ``"DEBUG"``, ``"INFO"``).  Not
        case sensitive.
    buffer_size : int
        Number of log records to store in a memory buffer before
        flushing to disk.  When set to 0, no buffering occurs.
    max_mb : int
        Maximum size of an individual log file in megabytes before
        rotation occurs.
    max_error_buffer : int
        Maximum number of error records to buffer before forcing a
        flush.  This is separate from the general buffer and is used
        to expedite error reporting.
    retention_days : int
        Number of days to retain log files before archival and
        deletion.  Older logs are compressed into a tar archive.
    tags : List[str]
        Optional tags to attach to every log record.  Tags can be used
        to indicate service version, environment, or other metadata.
    json_format : bool
        If ``True``, file handlers emit log entries in JSON format
        instead of the default text formatter.  Console handlers are
        unaffected by this option.
    enable_console : bool
        When ``True`` (default), logs will also be written to the
        console via a ``StreamHandler``.  Set to ``False`` to
        suppress console output.
    """

    log_dir: str = "logs"
    level: str = "DEBUG"
    buffer_size: int = 100
    max_mb: int = 5
    max_error_buffer: int = 20
    retention_days: int = 3
    tags: List[str] = field(default_factory=list)
    json_format: bool = False
    enable_console: bool = True

    # valid logging level names
    VALID_LEVELS: set[str] = field(default_factory=lambda: {
        "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
    }, init=False, repr=False)

    def __post_init__(self) -> None:
        """Validate and normalize configuration values post‑initialization.

        Raises
        ------
        ValueError
            If any of the configuration values are invalid.
        """

        # log_dir must be a non‑empty string
        if not isinstance(self.log_dir, str) or not self.log_dir.strip():
            raise ValueError("log_dir must be a non‑empty string")
        # convert to absolute path for consistency
        object.__setattr__(self, "log_dir", os.path.abspath(self.log_dir))

        # Normalize and validate logging level
        level_upper = self.level.upper()
        if level_upper not in self.VALID_LEVELS:
            raise ValueError(
                f"Invalid logging level '{self.level}'. Must be one of: {', '.join(self.VALID_LEVELS)}"
            )
        object.__setattr__(self, "level", level_upper)

        # Validate numeric fields
        if not isinstance(self.buffer_size, int) or self.buffer_size < 0:
            raise ValueError("buffer_size must be a non‑negative integer")
        if not isinstance(self.max_mb, int) or self.max_mb <= 0:
            raise ValueError("max_mb must be a positive integer")
        if not isinstance(self.max_error_buffer, int) or self.max_error_buffer <= 0:
            raise ValueError("max_error_buffer must be a positive integer")
        if not isinstance(self.retention_days, int) or self.retention_days <= 0:
            raise ValueError("retention_days must be a positive integer")

    @staticmethod
    def from_file(path: str) -> "LoggerConfig":
        """Load a configuration from a JSON or YAML file.

        Parameters
        ----------
        path : str
            Path to a JSON or YAML file containing configuration keys.

        Returns
        -------
        LoggerConfig
            An instance populated with values from the file.  Missing
            keys fall back to default values.

        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        ValueError
            If the file content is malformed or in an unsupported
            format.
        """
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Configuration file '{path}' not found.")

        ext = os.path.splitext(path)[1].lower()
        try:
            with open(path, "r", encoding="utf-8") as f:
                if ext in (".yaml", ".yml"):
                    data: Dict[str, Any] = yaml.safe_load(f) or {}
                elif ext == ".json":
                    data = json.load(f) or {}
                else:
                    raise ValueError("Unsupported config file format. Use .json, .yaml, or .yml.")
        except Exception as e:
            raise ValueError(f"Failed to load configuration: {e}")

        return LoggerConfig.from_dict(data)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "LoggerConfig":
        """Create a configuration from a mapping of options.

        Parameters
        ----------
        data : Dict[str, Any]
            Dictionary containing configuration keys.  Unknown keys are
            ignored.  Missing keys use default values.

        Returns
        -------
        LoggerConfig
            A new configuration instance.
        """
        if not isinstance(data, dict):
            raise ValueError("Configuration input must be a dictionary.")

        return LoggerConfig(
            log_dir=data.get("log_dir", "logs"),
            level=data.get("level", "DEBUG"),
            buffer_size=data.get("buffer_size", 100),
            max_mb=data.get("max_mb", 5),
            max_error_buffer=data.get("max_error_buffer", 20),
            retention_days=data.get("retention_days", 3),
            tags=data.get("tags", []),
            json_format=data.get("json_format", False),
            enable_console=data.get("enable_console", True),
        )


class ErrorBufferHandler(logging.Handler):
    """A custom handler that buffers error messages before forwarding them.

    ``ErrorBufferHandler`` inherits from :class:`logging.Handler` and
    stores formatted error messages in an internal list.  Once the
    number of buffered messages reaches ``max_buffer``, it flushes
    them to a downstream handler.  This handler is useful for
    aggregating bursts of errors and emitting them in a single batch,
    reducing I/O overhead.

    Parameters
    ----------
    max_buffer : int
        Maximum number of error messages to retain before flushing.
    flush_target : logging.Handler
        The handler that receives flushed error messages.
    """

    def __init__(self, max_buffer: int, flush_target: logging.Handler) -> None:
        super().__init__(level=logging.ERROR)
        self.buffer: List[str] = []
        self.max_buffer: int = max_buffer
        self.flush_target: logging.Handler = flush_target
        self._lock = threading.Lock()

    def emit(self, record: logging.LogRecord) -> None:
        """Add a formatted error record to the buffer.

        When the number of buffered messages reaches the configured
        threshold, the buffer is flushed to the ``flush_target``.
        """
        with self._lock:
            self.buffer.append(self.format(record))
            if len(self.buffer) >= self.max_buffer:
                self.flush()

    def flush(self) -> None:
        """Flush buffered error messages to the target handler."""
        with self._lock:
            for msg in self.buffer:
                # Recreate a log record with the stored message
                rec = logging.makeLogRecord({
                    "msg": msg,
                    "levelno": logging.ERROR,
                    "levelname": "ERROR",
                    "args": (),
                })
                self.flush_target.emit(rec)
            self.buffer.clear()


class JsonFormatter(logging.Formatter):
    """Format log records as JSON objects.

    This formatter produces a compact JSON representation of the log
    record, including timestamp, level, thread, logger name,
    function, line number, message, and any tags from the logger
    configuration.  It inherits from :class:`logging.Formatter` but
    ignores its format string.

    Parameters
    ----------
    tags : Iterable[str]
        Optional iterable of tags to include in each emitted JSON.
    datefmt : str, optional
        Date format string passed to the base class for formatting
        timestamps.  Defaults to ``"%Y-%m-%dT%H:%M:%S"``.
    """

    def __init__(self, tags: Optional[Iterable[str]] = None, datefmt: str | None = None) -> None:
        super().__init__(datefmt=datefmt or "%Y-%m-%dT%H:%M:%S")
        self.tags = list(tags) if tags else []

    def format(self, record: logging.LogRecord) -> str:
        record_dict: Dict[str, Any] = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "thread": record.threadName,
            "logger": record.name,
            "function": record.funcName,
            "line": record.lineno,
            "message": record.getMessage(),
        }
        if self.tags:
            record_dict["tags"] = self.tags
        return json.dumps(record_dict, ensure_ascii=False)


class AdvancedLogger:
    """A wrapper around ``logging.Logger`` providing advanced features.

    ``AdvancedLogger`` creates a logger with sensible defaults for a
    microservice or long‑running application.  It sets up console and
    file handlers, performs log rotation by size and time, and buffers
    error messages to avoid log flooding.  It also cleans up old log
    files beyond a configured retention period.  Instances of this
    class should be obtained via :class:`LoggerFactory`, which
    maintains a registry to ensure a single instance per service name.

    Parameters
    ----------
    service_name : str
        Name of the service or component using the logger.  Used to
        construct log file names.
    config : LoggerConfig
        Configuration controlling the behavior of the logger.
    """

    def __init__(self, service_name: str, config: LoggerConfig) -> None:
        self.service_name: str = service_name
        self.config: LoggerConfig = config
        self.logger: logging.Logger = logging.getLogger(service_name)
        self.logger.propagate = False  # avoid duplicate logs if root logger is configured
        self._lock = threading.Lock()

        # Set the logger's level based on configuration
        self.logger.setLevel(getattr(logging, config.level, logging.DEBUG))

        # Ensure the log directory exists
        os.makedirs(config.log_dir, exist_ok=True)

        # Configure handlers
        self._setup_handlers()
        # Perform cleanup of old log files
        self._cleanup_and_archive_old_logs()

    def _create_formatter(self) -> logging.Formatter:
        """Create a formatter based on configuration options."""
        if self.config.json_format:
            # Use JSON formatter for file handlers
            return JsonFormatter(tags=self.config.tags)
        return logging.Formatter(
            fmt=(
                "%(asctime)s [%(levelname)s] [%(threadName)s] "
                "[%(name)s.%(funcName)s:%(lineno)d] - %(message)s"
            ),
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def _setup_handlers(self) -> None:
        """Set up console and file handlers based on the configuration."""
        formatter = self._create_formatter()
        log_file = os.path.join(
            self.config.log_dir,
            f"{self.service_name}_{datetime.now().strftime('%Y%m%d_%H')}.log",
        )

        # Console handler if enabled
        if self.config.enable_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(getattr(logging, self.config.level))
            self.logger.addHandler(console_handler)

        # Size‑based rotation handler
        rotating_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=self.config.max_mb * 1024 * 1024,
            encoding="utf-8",
        )
        rotating_handler.setFormatter(formatter)
        rotating_handler.setLevel(getattr(logging, self.config.level))
        self.logger.addHandler(rotating_handler)

        # Timed rotation handler (hourly)
        timed_handler = logging.handlers.TimedRotatingFileHandler(
            filename=os.path.join(self.config.log_dir, f"{self.service_name}_hourly.log"),
            when="H",
            interval=1,
            encoding="utf-8",
            utc=True,
        )
        timed_handler.setFormatter(formatter)
        timed_handler.setLevel(getattr(logging, self.config.level))
        self.logger.addHandler(timed_handler)

        # Optional memory buffer: flush on ERROR or buffer size exceeded
        if self.config.buffer_size > 0:
            memory_handler = logging.handlers.MemoryHandler(
                capacity=self.config.buffer_size,
                flushLevel=logging.ERROR,
                target=rotating_handler,
            )
            memory_handler.setLevel(getattr(logging, self.config.level))
            memory_handler.setFormatter(formatter)
            self.logger.addHandler(memory_handler)

        # Error buffer handler: flushes after a burst of errors
        error_buffer_handler = ErrorBufferHandler(
            max_buffer=self.config.max_error_buffer,
            flush_target=rotating_handler,
        )
        error_buffer_handler.setFormatter(formatter)
        error_buffer_handler.setLevel(logging.ERROR)
        self.logger.addHandler(error_buffer_handler)

    def _cleanup_and_archive_old_logs(self) -> None:
        """Remove and archive log files older than the retention period."""
        cutoff = datetime.now() - timedelta(days=self.config.retention_days)
        to_archive: List[str] = []

        for file in os.listdir(self.config.log_dir):
            full_path = os.path.join(self.config.log_dir, file)
            if os.path.isfile(full_path) and file.endswith(".log"):
                mtime = datetime.fromtimestamp(os.path.getmtime(full_path))
                if mtime < cutoff:
                    to_archive.append(full_path)

        if not to_archive:
            return

        base = f"{self.service_name}_archive_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        tar1 = os.path.join(self.config.log_dir, f"{base}.tar.gz")
        tar2 = os.path.join(self.config.log_dir, f"{base}_wrapped.tar.gz")

        # Create an inner archive containing old logs, then wrap it in an outer archive
        with tarfile.open(tar1, "w:gz") as tar:
            for f in to_archive:
                tar.add(f, arcname=os.path.basename(f))
                os.remove(f)

        with tarfile.open(tar2, "w:gz") as outer_tar:
            outer_tar.add(tar1, arcname=os.path.basename(tar1))

        os.remove(tar1)

    def get_logger(self) -> logging.Logger:
        """Return the underlying :class:`logging.Logger` instance."""
        return self.logger

    def set_level(self, level: str) -> None:
        """Change the logging level for this logger and its handlers.

        Parameters
        ----------
        level : str
            New logging level name (e.g., ``"INFO"``).  The name is
            case insensitive.  Invalid names default to ``"DEBUG"``.
        """
        with self._lock:
            new_level = getattr(logging, level.upper(), logging.DEBUG)
            self.logger.setLevel(new_level)
            for handler in self.logger.handlers:
                handler.setLevel(new_level)


class LoggerFactory:
    """Factory for creating and retrieving named loggers.

    ``LoggerFactory`` maintains a process‑level registry of loggers
    keyed by service name.  Calling :meth:`get_logger` with the same
    name multiple times returns the same logger instance, preventing
    duplicate handlers or configurations.  You can configure a new
    default configuration via :meth:`configure_from_file` or
    :meth:`configure_from_dict` before retrieving loggers.
    """

    _loggers: Dict[str, logging.Logger] = {}
    _lock = threading.Lock()
    _default_config: LoggerConfig = LoggerConfig()

    @classmethod
    def configure_from_file(cls, path: str) -> None:
        """Override the default configuration using a file.

        Parameters
        ----------
        path : str
            Path to a JSON or YAML file containing configuration keys.
        """
        cls._default_config = LoggerConfig.from_file(path)

    @classmethod
    def configure_from_dict(cls, data: Dict[str, Any]) -> None:
        """Override the default configuration using a dictionary."""
        cls._default_config = LoggerConfig.from_dict(data)

    @classmethod
    def get_logger(cls, service_name: str) -> logging.Logger:
        """Retrieve or create a logger for the given service name.

        Parameters
        ----------
        service_name : str
            Unique name identifying the service or component.

        Returns
        -------
        logging.Logger
            A configured logger instance.  Subsequent calls with the
            same name return the same instance.
        """
        with cls._lock:
            if service_name not in cls._loggers:
                advanced_logger = AdvancedLogger(service_name, cls._default_config)
                cls._loggers[service_name] = advanced_logger.get_logger()
            return cls._loggers[service_name]



def example1_basic_usage() -> None:
    """Retrieve a logger with default settings and log messages."""
    logger = LoggerFactory.get_logger('myservice')
    logger.info('Service started')
    logger.warning('A recoverable issue occurred')
    logger.error('A critical error occurred')

# def deleteThisExample():
#     LoggerFactory.configure_from_dict({
#         "log_dir":"custom_log",
#         "level":"INFO"
#     })
#     logger=LoggerFactory.get_logger("myapp")
#     logger.info("L")
def example2_custom_directory() -> None:
    """Configure logging to a custom directory before retrieving the logger."""
    LoggerFactory.configure_from_dict({
        'log_dir': 'custom_logs',
        'level': 'INFO',
    })
    logger = LoggerFactory.get_logger('myapp')
    logger.info('Logging to custom_logs directory')


def example3_tags_and_json() -> None:
    """Attach tags to every log entry and enable JSON output."""
    config = {
        'tags': ['env:prod', 'version:1.2'],
        'json_format': True,
        'level': 'INFO',
    }
    LoggerFactory.configure_from_dict(config)
    logger = LoggerFactory.get_logger('api')
    logger.info('API service started with structured logs')


def example4_disable_console() -> None:
    """Disable console logging to suppress output on standard output."""
    LoggerFactory.configure_from_dict({
        'enable_console': False,
    })
    logger = LoggerFactory.get_logger('batch_job')
    logger.debug('This message is only written to file')


def example5_dynamic_log_level() -> None:
    """Change the log level at runtime."""
    logger = LoggerFactory.get_logger('worker')
    logger.setLevel('INFO')  # ignore DEBUG messages
    logger.debug('This debug message is ignored')
    logger.setLevel('DEBUG')  # now capture DEBUG messages
    logger.debug('This debug message is now logged')


def example6_config_from_file() -> None:
    """Use a configuration file in JSON format."""
    # Suppose logging_config.json contains:
    # {
    #   "log_dir": "app_logs",
    #   "level": "WARNING",
    #   "retention_days": 5
    # }
    LoggerFactory.configure_from_file('../configs/log_agent.json')
    logger = LoggerFactory.get_logger('service')
    logger.warning('This warning goes to app_logs')


def example7_buffer_sizes() -> None:
    """Specify different sizes for the general buffer and error buffer."""
    LoggerFactory.configure_from_dict({
        'buffer_size': 50,
        'max_error_buffer': 5,
    })
    logger = LoggerFactory.get_logger('pipeline')
    for i in range(10):
        logger.error(f'Error {i}')  # errors are batched by groups of five


def example8_retention_and_rotation() -> None:
    """Change retention policy and rotation size."""
    LoggerFactory.configure_from_dict({
        'retention_days': 10,
        'max_mb': 1,  # rotate every 1 MB
    })
    logger = LoggerFactory.get_logger('backup')
    logger.info('Retention is now 10 days; rotation at 1 MB per file')


def example9_multiple_services() -> None:
    """Create separate loggers for different components with shared defaults."""
    LoggerFactory.configure_from_dict({'level': 'DEBUG'})
    web_logger = LoggerFactory.get_logger('web')
    db_logger = LoggerFactory.get_logger('database')
    web_logger.debug('HTTP request received')
    db_logger.debug('Database connection opened')


def example10_different_formats() -> None:
    """Use JSON output for one service and plain text for another."""
    # Plain text service
    LoggerFactory.configure_from_dict({'json_format': False})
    text_logger = LoggerFactory.get_logger('plaintext_service')
    text_logger.info('Plain text message')

    # Switch to JSON for a different service
    LoggerFactory.configure_from_dict({'json_format': True})
    json_logger = LoggerFactory.get_logger('json_service')
    json_logger.info('JSON formatted message')


if __name__ == '__main__':
    # Execute all examples sequentially
    # example1_basic_usage()
    # example2_custom_directory()
    # example3_tags_and_json()
    # example4_disable_console()
    example5_dynamic_log_level()
    # example6_config_from_file()
    # example8_retention_and_rotation()
    # example9_multiple_services()
    # example10_different_formats()
    # example7_buffer_sizes()