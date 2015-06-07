#!/usr/bin/env python

f = open('file.txt', 'w')

f.writelines('123456')

f.writelines(('1', '2', '3'))

f.writelines(['1', '2', '3'])

f.close()