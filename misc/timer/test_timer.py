#!/usr/bin/env python2

# -*- coding: UTF-8 -*-

import threading

def sayhello():
    print("hello world")
    global t # notice: use global variable!
    t = threading.Timer(5.0, sayhello)
    t.start()

if __name__ == "__main__":
    t = threading.Timer(5.0, sayhello)
    t.start()