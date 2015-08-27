#!/usr/bin/env python2

# -*- coding: UTF-8 -*-

# 调用thread模块中的start_new_thread()函数来产生新线程

import time
import thread

def timer(no, interval):
    cnt = 0
    while cnt < 10:
        print 'Thread: (%d) Time:%s\n' % (no, time.ctime())
        time.sleep(interval)
        cnt += 1
    thread.exit()

#Use thread.start_new_thread() to create 2 new threads
def test():
    print("start")
    thread.start_new_thread(timer, (1,1))
    thread.start_new_thread(timer, (2,2))
    time.sleep(30)
    print("end")

if __name__ == '__main__':
    test()
