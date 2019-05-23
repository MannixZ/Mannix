#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/28 17:51

@author: ZMJ

@file: download_file.py

'''

import os
import re
import time
import shutil
import requests
from contextlib import closing

# 目录名称正则
file_name_reg = re.compile(r'.*?resys_whitebox_(.*)/')

# 保存文件路径
file_path = r'E:\\recommend log'

# log名称
log_name = str(time.strftime("%Y%m%d", time.localtime()) + '.log')

# 前缀
test_front_url = 'http://10.82.125.134:8000/feed_recommend_logs/'
front_url = 'http://60.191.80.27/logs/resys/'

# url地址存储
url_dict = {
    'rank_path' : front_url + 'whitebox/opd_god_resys_whitebox_rank/', # rank 文件地址
    'recall_path' : front_url + 'whitebox/opd_god_resys_whitebox_recall/', # recall 文件地址
    # 'recall_queue_path' : front_url + 'whitebox/opd_god_resys_whitebox_recall_queue/', # recall_queue 文件地址
    'rule_path' : front_url + 'whitebox/opd_god_resys_whitebox_rule/', # rule 文件地址
    'whole_path' : front_url + 'whitebox/opd_god_resys_whitebox_whole/', # whole 文件地址
    'user_profile_path' : front_url + 'whitebox/opd_god_resys_whitebox_user_profile/', # user_profile 文件地址
    
}

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Host': "60.191.80.27",
    'Connection': "keep-alive",
    'Authorization': "Basic TjIxNTM6eWRiQCMxNjM=",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'cache-control': "no-cache",
    'Postman-Token': "cdff5bcb-a9ec-4bcf-acdb-2e6a12a7d77f"
    }
def download(url):
    start = time.time()
    size = 0
    response = requests.get(url=url+log_name, stream=True, headers=headers)
    chunk_size = 1024 #每次下载数据大小
    content_size = int(response.headers['content-length'])  # 总大小
    file_name = re.findall(file_name_reg, url) #下载文件名称
    print(response)
    if response.status_code == 200:
        print('[开始下载文件]:%s.log\n[文件大小]:%0.2f MB' % (file_name[0],(content_size / chunk_size / 1024)))
        location = os.path.abspath(file_path)
        with open(location + '/' + file_name[0] + '/' + log_name, 'wb') as f:
            for data in response.iter_content(chunk_size=chunk_size):
                f.write(data)
                size += len(data)
                print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size),float(size / content_size *100)),end='')
    end = time.time()
    print('\n'+file_name[0]+'.log 下载完成！完成时间%.2f s \n\n' %(end-start))

def main():
    while True:
        for url in url_dict:
            url_path = url_dict.get(url)
            print(url_path)
            download(url_path)
        print('全部下载完成，10分钟后将开始下次下载')
        time.sleep(600) #600秒后开始下次下载



if __name__ == '__main__':
    main()