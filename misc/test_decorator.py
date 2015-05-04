#!/usr/bin/env python
# coding: utf-8

def hello(fn):
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__
    return wrapper

#@hello
def foo():
    print "I am foo"

# 与上面装饰函数等价
foo = hello(foo)

foo()