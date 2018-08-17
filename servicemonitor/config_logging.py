import os
import logging.config

import yaml


def setup_logging(
        default_path='../resources/logging.yml',
        default_level=logging.DEBUG,
        env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as config_file:
            config = yaml.safe_load(config_file)
        logging.config.dictConfig(config)
    else:
        logging.basicConfiRg(level=default_level)
