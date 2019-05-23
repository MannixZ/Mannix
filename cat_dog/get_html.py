#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import xlwt
import xlrd
import json
import time
import requests
import pyautogui
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup

# 写excel表
def write_excel(title_list, content_url_list):
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet('cat&dot', cell_overwrite_ok=True)
    for row in range(0, len(title_list)):
        sheet1.write(row, 0 , title_list[row])
    for colum in range(0, len(content_url_list)):
        sheet1.write(colum, 1, content_url_list[colum])
    f.save('cat&dog.xls')

def read_excel(filename):
    wb = xlrd.open_workbook(filename)
    shee1 = wb.sheet_by_index(0)
    cols_row = shee1.nrows
    for i in range(cols_row):
        title = shee1.cell(i, 0).value
        url = shee1.cell(i, 1).value
        yinxiang_note(url)



def get_html(num):
    url = 'http://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzIzOTk0NjM3MQ==&f=json&offset=' + str(num)+'&count=10&is_ok=1&scene=124&uin=NjM3NTU1MDg0&key=d861f4d9325ef8e20bb0e087c8bc01956b0784ecc7cf698db6d33e19dcafc6c7515a8d538f4c4848f165c2f7b0f7d7d0faeb4bbdbb1ec2a03362a3821ac46c77e31f50f61c3b0e74c579b7633048003a&pass_ticket=6de3Z%2BHf9HSrdrpzoIK4%2BooBWBGAR%2BbH70j1REmmsEvBwSQMb4h%2BhnYFoNwn9nzX&wxtoken=&appmsg_token=994_d6FdUZiFPyWjLh%252F90-MKGhPJQUMeTnUHYkuXSQ~~&x5=0&f=json'
    req = requests.get(url=url)
    req_text = req.text
    json_req = json.loads(req_text)
    general_msg_list = json_req['general_msg_list']
    general_msg_list = json.loads(general_msg_list)['list']
    if general_msg_list == []:
        print('没有更多内容获取')
        exit()
    for i in general_msg_list:
        try:
            title_list.append(i["app_msg_ext_info"]["title"])
            content_url_list.append(i["app_msg_ext_info"]["content_url"])
        except Exception as reason:
            continue
    write_excel(title_list, content_url_list)
    return title_list, content_url_list

# 使用selenium思路获取内容
def brower_get():
    link_dict = {}
    url = 'http://mp.weixin.qq.com/mp/homepage?__biz=MzIzOTk0NjM3MQ==&hid=1&sn=541fe5d6af6107a0f5cb663723b3ee1e&scene=18&uin=NjM3NTU1MDg0&key=52fe516b925e4ce864bf922674ff9cc9090d0abfe3b1ac10b862b98b356f298befc0dc5bf5c916d914cd23b8a73e30474ec74d8b5c58fbcc6434d0afaf1ce5c6215d90cdc10de061ad7690592a0e501d&devicetype=Windows+10&version=62060619&lang=zh_CN&ascene=7&pass_ticket=sXWqqXHq7nYq1aOieQZMBuZWtpIdRTPMRtmNhS6E3dEY0P7pw%2Bc87X%2BzU6dvvGen&winzoom=1&cid=0&begin=12&count=5&action=appmsg_list&f=json&r=0.08375340956263244&appmsg_token=989_im89tHqGLcWOITBZpWsEWTgej-ccfdpb6zBSOA~~'
    url1 = r'http://mp.weixin.qq.com/mp/homepage?__biz=MzIzOTk0NjM3MQ==&hid=1&sn=541fe5d6af6107a0f5cb663723b3ee1e&scene=18#wechat_redirect'
    brower = webdriver.Chrome()
    brower.get(url1)
    html_text = brower.page_source
    print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    page_class = soup.find_all('div', attrs={'class':'tab_bd'})
    for i in page_class:
        a = i.findAll('a')
        for href in a:
            link_dict[href.find('h2').get_text()] = href['href']
            # link_list.append(href['href'])
            # title_list.append(href.find('h2').get_text())
        print(link_dict)
    brower.close()


def yinxiang_note(url):
    # url = 'http://mp.weixin.qq.com/s?__biz=MzIzOTk0NjM3MQ==&amp;mid=2247485819&amp;idx=1&amp;sn=b53a6560422067396684e9677fe629fd&amp;chksm=e9231697de549f81598cdfb00d6407ce36fc2d57f7acc25a4711b84352dec2a526f28a37dd8f&amp;scene=27#wechat_redirect'
    profile_dir = r'C:\Users\wb.zengmingjie\AppData\Local\Google\Chrome\User Data'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))
    brower = webdriver.Chrome(chrome_options=chrome_options)
    brower.get(url)
    pyautogui.moveTo(1694, 55)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1743, 265)
    pyautogui.click()
    time.sleep(10)
    brower.quit()

def write_yinxiang(content_url_list):
    for url in content_url_list:
        yinxiang_note(url)
        time.sleep(10)

def main(count=1):
    num = 0
    for i in range(count):
        get_html(num)
        num += 10
        time.sleep(3)
        print('获取成功, 次数为 %s, num 为 %s' %(count, num))
    # write_yinxiang()

if __name__ == '__main__':
    # title_list = []
    # content_url_list = []
    # main(50)
    # print(title_list, content_url_list)

    filename = 'cat&dog.xls'
    read_excel(filename)

    # main()