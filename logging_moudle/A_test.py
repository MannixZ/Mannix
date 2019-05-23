#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging_moudle.main import setup_logging

# logger = logging.getLogger('main.A_test')

def compler():
    a = 3
    b = 2
    if a > b:
        logging.info("++++++%s %s", a, b)

def hahaha():
    logging.info('__________')

if __name__ == '__main__':
    setup_logging()
    compler()
    hahaha()