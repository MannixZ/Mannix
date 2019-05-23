#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/5/23/0023 17:35

@author: ZMJ

@file: Logging.py

'''


# log记录方法2
def log_record(logger, BASE_DIR):
    '''

    :param logger:
    :param BASE_DIR:
    :return:

    使用模块头部需要先使用
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    logger = logging.getLogger(__name__)
    Logging.log_record(logger, BASE_DIR)
    '''
    # 创建 log 目录
    os.makedirs(BASE_DIR + '/log', exist_ok=True)
    file_path = BASE_DIR + '/log'
    formatter_style = '%(asctime)s - %(lineno)d - %(funcName)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(formatter_style)
    logging.basicConfig(level=logging.INFO, format=formatter_style, stream=sys.stdout)  # 控制台显示
    # 错误文本记录 ERROR
    # file_handler = logging.FileHandler('error.log', encoding='utf-8')
    file_handler = logging.FileHandler(
        file_path + '/' + 'errmsg_' + str(time.strftime("%Y%m%d", time.localtime())) + '.log', encoding='utf-8')
    file_handler.setLevel(level=logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # 文本日常记录 INFO
    file_handler_info = logging.FileHandler(
        file_path + '/' + 'info_' + str(time.strftime("%Y%m%d", time.localtime())) + '.log', encoding='utf-8')
    file_handler_info.setLevel(level=logging.INFO)
    file_handler_info.setFormatter(formatter)
    logger.addHandler(file_handler_info)