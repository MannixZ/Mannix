#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

file_name = 'test.txt'
lock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self, string):
        super().__init__()
        self.string = string

    def run(self):
        write_to_file(self.name + '~' + self.string)
        time.sleep(1)

def write_to_file(string):
    if lock.acquire(): # 上锁，防止多个线程并发去访问临界资源引起线程同步安全问题
        try:
            with open(file_name, 'a+', encoding='utf-8') as f:
                f.write(string + '\n')
        except OSError as reason:
            print(str(reason))
        finally:
            lock.release()

for i in range(1,100):
    t = MyThread(str(i)).start()

