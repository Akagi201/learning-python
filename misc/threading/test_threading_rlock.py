#!/usr/bin/env python2

# -*- coding: utf-8 -*-

# Python's threading module is on top of thread module

import threading
import time

mylock = threading.RLock()

num = 0

f = file("test_result.txt", 'w')

class dog(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global num
        while num <= 5:
            time.sleep(0.5)
            mylock.acquire()
            print("Th(%s) locked, number: %d\n" % (self.name, num))
            f.write(self.name + " " + str(num) + '\n')
            print("Th(%s) released, number: %d\n" % (self.name, num))
            mylock.release()
            num += 1

def test():
    th1 = dog("dog A")
    th2 = dog("dog B")
    th1.start()
    th2.start()
    time.sleep(30)

if __name__=='__main__':
    test()


