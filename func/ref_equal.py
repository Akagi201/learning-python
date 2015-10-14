#!/usr/bin/env python
# http://www.cnblogs.com/yuyan/archive/2012/04/21/2461673.html

def add_list(p):
    p = p + [1]

p1 = [1,2,3]
add_list(p1)

print p1

def add_list1(p):
    p += [1]

p2 = [1,2,3]
add_list1(p2)
print p2
