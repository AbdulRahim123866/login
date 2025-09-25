import argparse
import os

from trainig_write_logging import MultiPurposeLogger, LogType, LoggerRunMode


def cli():
    parser=argparse.ArgumentParser()
    parser.add_argument('-c','--config',required=True,type=str,help="Path to the YAML configuration file.")
    args=parser.parse_args()

    return args
if __name__=="__main__":
    args=cli()
    print(args.config)
    print(os.getcwd())

    logger=MultiPurposeLogger(service_name="api_service",
                              log_type=LogType.REGULAR,
                              mode=LoggerRunMode.LOCAL,
                              config_path=args.config)
    for i in range(100):
        logger.log(f"Line num {i}")

    logger.close()