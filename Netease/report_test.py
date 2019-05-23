#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/5/21/0021 20:13

@author: ZMJ

@file: report_test.py

'''

from report import Report

info = {
    "author": "zmj",
    "module": "网易大神推荐系统策略层v1版",
    "testcase_url": "http://git-qa.gz.netease.com/godlike/test-scripts"
}
rp = Report(info=info, save_dir="rp")

rp.success(title='111', info='123123')