"""
Usage:
    test.py [-h|--help] [--id <your_id>] [--password <your_password>] [-a <args>...]

Options:
    -h,--help                   show this help message and exit
    --id=<your_id>              your id [default: 0123456789]
    --password=<your_password>  your password [default: abc]
    --args                      something input
"""

from docopt import docopt
from logging import getLogger, config
import json


def setup_logger():
    with open('log_config.json', 'r') as f:
        log_conf = json.load(f)
        config.dictConfig(log_conf)
        logger = getLogger(__name__)
        return logger


logger = setup_logger()


def setup():
    arguments = docopt(__doc__, version='1.0')
    logger = setup_logger()
    logger.info("Start program...")
    logger.info(arguments)


def main():
    setup()


if __name__ == '__main__':
    main()
