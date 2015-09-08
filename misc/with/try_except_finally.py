#!/usr/bin/env python2

# -*- coding: utf-8 -*-

# http://www.ipython.me/python/python-with-syntax.html

try:
    f = open('ipython.txt', 'w')
    f.write('www.ipython.com try except finally\n')
    f.close()
except IOError as err:
    print("file error:\n" + str(err))
finally:
    if 'f' in locals():
        f.close()
