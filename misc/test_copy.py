#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

# Python中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的copy模块。
# 1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。
# 2. copy.deepcopy 深拷贝 拷贝对象及其子对象

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a # 赋值, 传对象的引用
c = copy.copy(a)  # 对象拷贝, 浅拷贝
d = copy.deepcopy(a)  # 对象拷贝, 深拷贝

a.append(5) # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print ('a = %r, %r', (a, id(a)))
print ('b = %r, %r', (b, id(b)))
print ('c = %r, %r', (c, id(c)))
print ('d = %r, %r', (d, id(d)))
