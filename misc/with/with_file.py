#!/usr/bin/env python2

# -*- coding: utf-8 -*-

# http://www.ipython.me/python/python-with-syntax.html

try:
    with open('ipython.txt', 'w') as f:
        f.write('www.ipython.me with\n')
except IOError as err:
    print("file error:\n" + str(err))
