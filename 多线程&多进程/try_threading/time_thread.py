#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import threading

def catch_meizi(count):
    print('抓到野生妹子 X %d' % count)
    time.sleep(0.1)

def normal_test():
    start_time = time.time()
    for i in range(1, 100):
        catch_meizi(i)
    end_time = time.time()
    print('normal_test 耗时 === %s' % str(end_time - start_time))

def muti_thread_test():
    start_time = time.time()
    for i in range(1, 100):
        t = threading.Thread(target=catch_meizi(i)).start()
    end_time = time.time()
    print('muti_thread_test 耗时 === %s' %str(end_time - start_time))


if __name__ == '__main__':

    t = threading.Thread(normal_test())
    t.start()

    muti_thread_test()