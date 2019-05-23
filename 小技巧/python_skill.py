#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/19 20:31

@author: ZMJ

@file: python_skill.py

'''

from collections import Counter


# 把list的所有元素拼接成一个字符串
a = ['a', 'b', 'c']
print(''.join(a))

# 找出list中出现频率最高的元素
a = [1,2,3,4,5,4,3,1,3,5,3,5,7,8,4,4,4]
print(max(set(a), key = a.count))

# 判断两个字符串是否包含相同的字符
str1 = 'abc'
str2 = 'cba'
print(Counter(str1) == Counter(str2))

# 反转字符串
a = 'abc'
print(a[::-1])

# 反转列表
a = ['a', 'b', 'c']
print(a[::-1])

# 转置2D阵列
a = [['a','b'], ['c','d'], ['e','f']]
transport = zip(*a)
print(list(transport))

# 字典的get方法
a = {'a':1, 'b':2}
# d.get('c', 3)就是取key为'c'的值，如果不存在该key则默认返回3
print(a.get('c',3))

# 按值排序字典
a = {'a':1, 'b':3 ,'c':2}
print(sorted(a, key=a.get))

# 把列表用符号拼接成字符串
a = ['a', 'b', 'c']
print(','.join(a))

# 合并字典
d1 = {'a': 1}
d2 = {'b': 2}
d1.update(d2)
print(d1)

# 找出列表中最大值或最小值的index
lst = [30, 40, 20, 80]
def minIndex(l):
    return min(range(len(l)), key=l.__getitem__)

def maxIndex(l):
    return max(range(len(l)), key=l.__getitem__)

print(minIndex(lst), maxIndex(lst))

# 去掉列表中重复的元素
l = [2,2,2,3,3,1]
print(list(set(l)))
