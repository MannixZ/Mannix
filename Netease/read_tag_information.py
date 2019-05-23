#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import time
import json
import requests


def read_excel():
    wb = xlrd.open_workbook(filename='query_result（1）.xls')
    sheet1 = wb.sheet_by_index(0)
    cols_ids = sheet1.col_values(1)
    cols_row = sheet1.nrows  # 列总数
    cols_col = sheet1.ncols  # 行总数
    for j in range(cols_row):
        cols_tag_ids = []
        cols_tag_names = []
        if j != 0:
            # for i in sheet1.cell(i, 1).value:
            #     cols_tag_ids.append(i)
            # for i in sheet1.cell(i, 2).value:
            #     cols_tag_names.append(i)
            ids = sheet1.cell(j, 1).value
            names = sheet1.cell(j, 2).value
            ids = ids.split(',')
            names = names.split(',')
            for i in ids:
                cols_tag_ids.append(i)
            for i in names:
                cols_tag_names.append(i)

            if len(cols_tag_ids) != len(cols_tag_names):
                print(i+1)
                exit()
            else:
                print('%s 行数据对比通过' %j)

def read_excel1():
    wb = xlrd.open_workbook(filename='query_result（2）.xls')
    sheet1 = wb.sheet_by_index(0)
    cols_row = sheet1.nrows  # 列总数
    cols_col = sheet1.ncols  # 行总数
    for j in range(cols_row):
        cols_tag_ids = []
        cols_tag_names = []
        if j != 0:
            ids = sheet1.cell(j, 1).value
            names = sheet1.cell(j, 2).value
            if names != req_tag_name(ids):
                print('%s 不通过' %j)
                exit()
            else:
                print('%s 行数据对比通过' %j)

def req_tag_name(tag_id):
    url = "http://god-dev.gameyw.netease.com:8080/cms/miscData?datasource=&collection=tag&params=%7B%22_id%22%3A%22"+ tag_id +"%22%7D"
    headers = {
        'Host': "god-dev.gameyw.netease.com:8080",
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Origin': "http://god-test.gameyw.netease.com:8080",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'Content-Type': "application/json;charset=UTF-8",
        'Referer': "http://god-test.gameyw.netease.com:8080/qa_promote_help.html",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        'cache-control': "no-cache",
        'Postman-Token': "ac09a8f9-6740-46cd-a9a7-5fa123c4b261"
    }

    response = requests.request("GET", url, headers=headers)
    resp_json = json.loads(response.text)
    tag_name = resp_json['result'][0]['tag_name']
    return tag_name




if __name__ == '__main__':
    read_excel1()
    # req_tag_name()