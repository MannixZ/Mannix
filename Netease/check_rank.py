# -*- coding: utf-8 -*- 
# @Time : 2019/5/7 上午4:41 
# @Author : ZMJ 
# @File : check_rank.py

import re
from about_excel.read_write_excel import read_excel

weight_rule = re.compile(r'.*?"weight": (.*?)}')

def check_rank_excel():
    filename = 'query_result.xls'
    content = read_excel(filename=filename)
    for role_info in content[1:]:
        weight_list = weight_rule.findall(role_info[1])
        if weight_list != sorted(weight_list, reverse=True):
            if 'null' not in weight_list:
                print(role_info)

def check_result_excel():
    filename = 'result .xls'
    content = read_excel(filename=filename, num=0)
    content = list(set(content[0:]))
    for uid in content:
        if content.count(uid) > 3:
            print(uid)

def check_issued_feed():
    error_list = []
    white_list = ['25e29203e9754705841709efc7f0cab9',
'ad21a712de294a4c95a4305e7a9e33ca',
'4b2c4f03483d4fb5b31d7ac798571e12',
'16f7ab22f42d45188b75973b562ca87d',
'9e7d2591fefe4b03813fe9d3fc0f3159',
'3f34cc7fb1e0432595c1ec9a21464e25',
'd9e9b75060964bce90b783a28aedcede',
'09fd49da1c1b40a4b0672c35580b03c7',
'8ba9f5bed55e4639b13c6f0e682f8455',
'952edce2472c495980fe019ff60fd316',
'a5c98feea09d45fdb1278ebd7318242a',
]
    filename = 'query_result (3).xls'
    contetn = read_excel(filename=filename, num=0)
    for uid in contetn[1:]:
        if uid[-1] != "6" and uid not in white_list:
            error_list.append(uid)
            print(uid)
    print(len(error_list))

if __name__ == '__main__':
    # check_rank_excel()
    # check_result_excel()
    check_issued_feed()