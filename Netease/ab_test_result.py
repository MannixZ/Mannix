#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/5/5/0005 10:22

@author: ZMJ

@file: ab_test_result.py

'''

# 6055 用户标签权重接口
user_portrait = {
    '1346': '用户画像权值v1',
    '2958': '用户画像v2版本实验组1',
    '6069': '用户画像权值v1（去掉us接口）',
    '0477': '用户画像v2版本实验组2',
    '1423': '用户画像权值v1（去掉us接口）'
}

# 1859 b1全局置顶队列
b1 = {
    '3819': '实验组（全局置顶3条）',
    '1743': '本地测试配置'
}

# 9848 b2全局热门队列
b2 = {
    '3167': '实验组1（热门队列1）',
    '6533': '实验组2（热门队列2）',
    '3342': '本地测试'
}

# 4825 b3兴趣规则召回队列
b3 = {
    '6804': '实验组1（补位版）',
    '8565': '实验组2（不补位版）',
    '8047': '本地测试'
}

# 8570 b4兴趣模型召回队列
b4 = {
    '0347': '实验组1',
    '5913': '实验组2（不进行模型召回！）'
}

# 9105 b5兴趣时序召回队列
b5 = {
    '6112': '实验组1（时序召回）',
    '6001': '实验组2（不召回）'
}

# 5414 b6解耦质量分，非推荐
b6 = {
    '8944': '默认',
    '5210': '测试'
}

# 2798 b7解耦质量分，推荐
b7 = {
    '6643': '默认',
    '5450': '测试'
}

# 3862 b8游戏好友
b8 = {
    '5233': '默认',
    '1016': '测试'
}

# 8919 排序接口
sort = {
    '7563': '规则排序',
    '7880': '模型排序',
    '6679': '本地测试'
}

# 1402 规则接口
rule = {
    '2308': '规则接口v1',
    '1919': '降级策略v2'
}

# 4622 白盒日志
log = {
    '6362': '记录',
    '2658': '不记录'
}

# 5211 兜底日志
ears = {
    '3346': '无兜底',
    '6282': '有兜底'
}

# 3837 展示层
obvious = {
    '8361': 'None',
    '2993': '测试'
}

def AB_checkout():
    req_id_input = input()
    req_id_input = req_id_input.split('_')
    req_id_input =  req_id_input[:-1]
    print(' ' + user_portrait.get(req_id_input[0]) + '\n',
          b1.get(req_id_input[1]) + '\n',
          b2.get(req_id_input[2]) + '\n',
          b3.get(req_id_input[3]) + '\n',
          b4.get(req_id_input[4]) + '\n',
          b5.get(req_id_input[5]) + '\n',
          b6.get(req_id_input[6]) + '\n',
          b7.get(req_id_input[7]) + '\n',
          b8.get(req_id_input[8]) + '\n',
          sort.get(req_id_input[9]) + '\n',
          rule.get(req_id_input[10]) + '\n',
          obvious.get(req_id_input[11]) + '\n',
          ears.get(req_id_input[12]) + '\n',
          log.get(req_id_input[13]) + '\n')


if __name__ == '__main__':
    AB_checkout()