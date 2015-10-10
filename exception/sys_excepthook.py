#!/usr/bin/env python
# encoding: utf-8

import sys


def my_excepthook(type, value, traceback):
    print 'Unhandled error:', type, value


sys.excepthook = my_excepthook

print 'Before exception'

raise RuntimeError('This is the error message')

print 'After exception'
