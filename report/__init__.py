#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  ydbn2153
# Created: 2019-02-15
# Description: godlike recommend report module

from __future__ import absolute_import
from __future__ import division


import argparse
import os
import time
import json
import warnings
import inspect
import codecs
import atexit


from report.utils import nameddict



__dir__ = os.path.dirname(os.path.abspath(__file__))


class ExtDeprecationWarning(DeprecationWarning):
    pass

warnings.simplefilter('always', ExtDeprecationWarning)

def json2obj(data):
    data['this'] = data.pop('self', None)
    return nameddict('X', data.keys())(**data)

def center(bounds):
    x = (bounds['left'] + bounds['right'])//2
    y = (bounds['top'] + bounds['bottom'])//2
    return (x, y)


class Report(object):
    """
    Example usage:
    from report import Report
    
    info = {
        "author": "zmj",
        "module": "网易大神推荐系统排序层",
        "testcase_url": "脚本地址"
    }
    rp = Report(info=info, save_dir="rp")

    Report(info)
    """
    def __init__(self, info, save_dir='report'):
        image_dir = os.path.join(save_dir, 'images')
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        self.info = info
        self.save_dir = save_dir
        self.steps = []
        self.result = None
        self.__closed = False
        
        self.start_record()


    def start_record(self):
        self.start_time = time.time()
        self.result = dict(info=dict(
            author=self.info["author"],
            module=self.info["module"],
            testcase_url=self.info["testcase_url"],
            start_time=time.strftime("%Y-%m-%d %H:%M:%S"),
            start_timestamp=time.time(),
        ), steps=self.steps)

        self.__closed = False
        atexit.register(self.close)

    def close(self):
        if self.__closed:
            return

        save_dir = self.save_dir
        data = json.dumps(self.result)
        tmpl_path = os.path.join(__dir__, 'index.tmpl.html')
        save_path = os.path.join(save_dir, 'index.html')
        json_path = os.path.join(save_dir, 'result.json')

        with codecs.open(tmpl_path, 'rb', 'utf-8') as f:
            html_content = f.read().replace('$$data$$', data)

        with open(json_path, 'wb') as f:
            f.write(json.dumps(self.result, indent=4).encode('utf-8'))

        with open(save_path, 'wb') as f:
            f.write(html_content.encode('utf-8'))

        self.__closed = True

    def success(self, title, info):
        step = {
            'time': '%.1f' % (time.time()-self.start_time,),
            'action': 'info',
            'title': title,
            'info': info,
            'success': True,
        }   
        self.steps.append(step)

    def fail(self, title, info):
        step = {
            'time': '%.1f' % (time.time()-self.start_time,),
            'action': 'error',
            'title': title,
            'info': info,
            'success': False,
        }   
        self.steps.append(step)
