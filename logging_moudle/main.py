#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import core
import yaml
import logging.config
import os


def setup_logging(default_path='config.yaml', default_level=logging.INFO):
    path = default_path
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def log():
    logging.debug('Start')
    logging.info('Exec')
    logging.info('Finished')

if __name__ == '__main__':
    setup_logging()
    log()
    core.run()
