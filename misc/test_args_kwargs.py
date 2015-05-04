#!/usr/bin/env python

def speak(*args, **kwargs):
    print type(args)
    print type(kwargs)
    print args, kwargs

a = 1
b = 2
c = 3
speak(a, b, c, b, c, a, c, a, b, d=a, e=b, f=c)
