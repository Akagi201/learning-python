#!/usr/bin/env python
#coding=utf-8

import sys

sys.stdout = open('stdout.log', 'a') # 只要是 file-like, 不管是什么类型
print 'foo'

sys.stdout = sys.__stdout__ # 恢复
print 'bar'
