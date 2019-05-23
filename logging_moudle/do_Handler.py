#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from logging.handlers import HTTPHandler


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# StreamHandelr
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)

# FileHandler
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# HTTPHandler
# http_handler = HTTPHandler(host='localhst:8001', url='log', method='POST')
# logger.addHandler(http_handler)

# Log
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
try:
    result = 10 / 0
except Exception:
    logger.exception('Faild to get result')