#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', stream=sys.stdout)
# stream 控制台输出颜色

# logging.basicConfig(level=logging.INFO,
#                     filename='output.log',
#                     datefmt='%Y/%m/%d %H:%M:%S',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')


file_handler = logging.FileHandler('output.log')
file_handler.setLevel(level=logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
