#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from time import sleep


def str2dict(headers_str):
    res = {}
    str_list = headers_str.split("\n")   #以 换行符为分割
    # print(str_list)
    for item in str_list:  #检查每一行元素
        try:
            tmp = item.split(": ")    #以 ： 号为分隔
            if tmp[0] == "Content-Length":
                continue
            res[tmp[0]] = tmp[1]
            # print(res)
        except Exception as e:
            pass
    return res

# 白名单推送
def req_singleSend(count, headers):
    url = 'http://god-test.gameyw.netease.com:8080/cms_test/push/singlePush'
    if count == 0:
        data = {"whiteList": ["ea7c010cef734d04bf6a9d733bf4cda3"], "jumpType": "1", "title": "12白名单测试文字推送标题3", "brief": "白名单测试文字推送消息",
            "scheduledTime": None, "uid": "ea7c010cef734d04bf6a9d733bf4cda3"}
    elif count == 1:
        data = {"whiteList":["ea7c010cef734d04bf6a9d733bf4cda3"],"jumpType":"4","title":"白名单测试h5推送标题","brief":"白名单测试h5推送消息","url":"https://www.baidu.com","imgUrl":"https://ok.166.net/reunionpub/2019-01-18/ntesgod_cms/1547781328122_35lpzw.jpg","hashL":None,"hashR":None,"scheduledTime":None,"uid":"ea7c010cef734d04bf6a9d733bf4cda3"}
    elif count == 2:
        data = {"whiteList": ["ea7c010cef734d04bf6a9d733bf4cda3"], "jumpType": "5", "title": "白名单测试动态推送标题",
                "brief": "白名单测试动态推送消息", "url": "5c4142a6e795d130bebe0303;b183361662cc45ec954fc5173c647d8d",
                "imgUrl": "https://ok.166.net/reunionpub/2019-01-18/ntesgod_cms/1547781328122_35lpzw.jpg",
                "hashL": None, "hashR": None, "scheduledTime": None, "uid": "ea7c010cef734d04bf6a9d733bf4cda3"}
    elif count == 3:
        data = {"whiteList":["ea7c010cef734d04bf6a9d733bf4cda3"],"jumpType":"6","title":"白名单测试话题推送标题","brief":"白名单测试话题推送消息","url":"老司机","imgUrl":"https://ok.166.net/reunionpub/2019-01-18/ntesgod_cms/1547781328122_35lpzw.jpg","hashL":None,"hashR":None,"scheduledTime":None,"uid":"ea7c010cef734d04bf6a9d733bf4cda3"}
    elif count == 4:
        data = {"whiteList":["ea7c010cef734d04bf6a9d733bf4cda3"],"jumpType":"7","title":"白名单测试个人主页推送标题","brief":"白名单测试个人主页推送消息","url":"b183361662cc45ec954fc5173c647d8d","imgUrl":"https://ok.166.net/reunionpub/2019-01-18/ntesgod_cms/1547781328122_35lpzw.jpg","hashL":None,"hashR":None,"scheduledTime":None,"uid":"ea7c010cef734d04bf6a9d733bf4cda3"}
    req = requests.post(url, headers=headers, data=json.dumps(data))
    if json.loads(req.text)['code'] == 200:
        print('推送成功')

# 实验组推送测试
def req_portraitSend(count,headers):
    url = 'http://god-test.gameyw.netease.com:8080/cms_test/push/portraitPush'
    if count == 0:
        data = {"tags":["5b0cc966d5456877cb7d0236"],"pushes":[{"jumpType":"1","whiteList":["b183361662cc45ec954fc5173c647d8d"],"title":"测试文字推送标题","brief":"测试文字推送消息","hashL":40,"hashR":45}]}
    elif count == 1:
        data = {"tags":["5b0cc966d5456877cb7d0236"],"pushes":[{"hashL":40,"hashR":45,"jumpType":"4","title":"测试h5推送消息","brief":"测试h5推送消息","url":"https://www.baidu.com","imgUrl":"https://ok.166.net/reunionpub/2019-01-18/ntesgod_cms/1547782965419_ner70u.jpg"}]}
    elif count == 2:
        data = {"tags":["5b0cc966d5456877cb7d0236"],"pushes":[{"jumpType":"5","url":"5c4142a6e795d130bebe0303;b183361662cc45ec954fc5173c647d8d","hashL":40,"hashR":45,"title":"测试动态推送标题","brief":"测试动态不推送消息","imgUrl":"https://ok.166.net/reunionpub/2019-01-18/ntesgod_cms/1547783073424_gsxjz1.jpg"}]}
    elif count == 3:
        data = {"tags":["5b0cc966d5456877cb7d0236"],"pushes":[{"jumpType":"6","hashL":40,"hashR":45,"title":"测试话题推送消息","url":"老司机","brief":"测试话题推送消息","imgUrl":"https://ok.166.net/reunionpub/2019-01-18/ntesgod_cms/1547783141334_miii4m.jpg"}]}
    elif count == 4:
        data = {"tags":["5b0cc966d5456877cb7d0236"],"pushes":[{"hashL":40,"hashR":45,"jumpType":"7","title":"测试个人主页推送消息","brief":"测试个人主页推送消息","url":"ea7c010cef734d04bf6a9d733bf4cda3","imgUrl":"https://ok.166.net/reunionpub/2019-01-18/ntesgod_cms/1547783218827_oflwnc.jpg"}]}
    req = requests.post(url, headers=headers, data=json.dumps(data))
    if json.loads(req.text)['code'] == 200:
        print('推送成功')

if __name__ == '__main__':
    headers = '''
Host: god-test.gameyw.netease.com:8080
Connection: keep-alive
Content-Length: 305
Pragma: no-cache
Cache-Control: no-cache
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://god-test.gameyw.netease.com:8080
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Content-Type: application/json;charset=UTF-8
Referer: http://god-test.gameyw.netease.com:8080/cms_test/push/portrait
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: _ntes_nnid=2d6f2ec347312fe9a8c5948f8ece4214,1539224511672; _ga=GA1.2.272634433.1539255345; commonly_used_tags=[%225beb80fd421aa9e91913bae3%22%2C%225beb80fd421aa9e91913bb0b%22%2C%225beb7e45421aa9e6587cc495%22]; P_INFO=zmjbobo1@163.com|1555409946|1|ntesgod_app|00&99|gud&1555332121&urs#gud&440100#10#0#0|&0|godlike_app&urs&ntesgod_app|zmjbobo1@163.com; NTES_GOD_CMS_USER=GO0620; route=64782fee861487d27ae2736ee8853328; _km_noosfero_session=BAh7CToNYmFja191cmwiHS93aWtpL3Nob3c%2FcGFnZV9pZD0yMDM2NzoJdXNlcmkCTGU6D3Nlc3Npb25faWQiJWI1OGUyMzBiMzljYzA3MzdmMDE5YzEzMjg3NzRlY2NhIgpmbGFzaElDOidBY3Rpb25Db250cm9sbGVyOjpGbGFzaDo6Rmxhc2hIYXNoewY6C25vdGljZSIR5oiQ5Yqf55m75b2VBjoKQHVzZWR7BjsJVA%3D%3D--55fc4f941fb7a1316c341b3fc28724acff4abb8a; cms_session=JVcb3JucKYGGTsN8_2ghi-u0iEsqe1c0RRxf1IOt
    '''
    headers = str2dict(headers)
    for count in range(5):
        req_singleSend(count , headers)
        req_portraitSend(count, headers)
        sleep(10)

