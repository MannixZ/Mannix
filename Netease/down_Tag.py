#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

from Function.utils import write_excel

def get_tag():
    url = "http://god-dev.gameyw.netease.com:8080/cms/tag/getChildren"
    querystring = {"tagId": "-1"}
    payload = ""
    headers = {
        'Host': "god-dev.gameyw.netease.com:8080",
        'Connection': "keep-alive",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'Referer': "http://god-dev.gameyw.netease.com:8080/cms/tag/list",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        'Cookie': "JSESSIONID=NEl0P9dxxvQt3S39UqVm6M4yac205yhyHeSbKgzw; _ntes_nnid=2d6f2ec347312fe9a8c5948f8ece4214,1539224511672; _ga=GA1.2.272634433.1539255345; P_INFO=zmjbobo9@163.com|1545046431|1|ntesgod_app|00&99|gud&1545044990&ntesgod_app#gud&440100#10#0#0|&0|ntesgod_app|zmjbobo9@163.com; _km_noosfero_session=BAh7CToJdXNlcmkCTGUiCmZsYXNoSUM6J0FjdGlvbkNvbnRyb2xsZXI6OkZsYXNoOjpGbGFzaEhhc2h7BjoLbm90aWNlIhHmiJDlip%2FnmbvlvZUGOgpAdXNlZHsGOwdGOg9zZXNzaW9uX2lkIiU2YTExNmRlMmZkZWJkNjBlNzBkZTBiZWVlOTRlN2RkYzoNYmFja191cmwiHi9wcm9maWxlL29wZD9pc19jaGVja2VkPTE%3D--714d1751fee82072c48d27370a0fdbcf69a98763; route=64782fee861487d27ae2736ee8853328; _gid=GA1.2.661476974.1548296034",
        'cache-control': "no-cache",
        'Postman-Token': "712e5b22-ac64-4bc3-91fa-8feaec61d0de"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    resp_json = json.loads(response.text)
    result = resp_json['result']
    tag_id = []
    tag_name = []
    for tag in result:
        tag_id.append(tag['id'])
        tag_name.append(tag['tagName'])
    write_excel(tag_id, tag_name, 'tag_name.xls')



if __name__ == '__main__':
    get_tag()