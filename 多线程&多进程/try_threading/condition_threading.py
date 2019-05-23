#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/18 11:28

@author: ZMJ

@file: condition_threading.py

'''
import time
import threading

condition = threading.Condition()
products = 0  # 货品数量


# 定义生产者线程类
class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products >= 99:
                    condition.wait()
                else:
                    products += 2
                    print(self.name + "生产了2个产品，当前剩余产品数为：" + str(products))
                    condition.notify()
                condition.release()
                time.sleep(2)

# 定义消费者线程类
class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products < 3:
                    condition.wait()
                else:
                    products -= 3
                    print(self.name + "消耗了3个产品，当前剩余产品数为：" + str(products))
                    condition.notify()
            condition.release()
            time.sleep(2)

if __name__ == '__main__':
    for i in range(5):
        p = Producer()
        p.start()
    for j in range(2):
        c = Consumer()
        c.start()