#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素.
# 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.

# sets 支持 x in set, len(set)和 for x in set. 作为一个无序的集合, sets不记录元素位置或者插入点.
# 因此, sets不支持 indexing, slicing, 或其它类序列(sequence-like)的操作.
# http://blog.csdn.net/business122/article/details/7541486


x = set('spam')
y = set(['h', 'a', 'm'])
print(x, y)

# 交集
print(x & y)

# 并集
print(x | y)

# 差集, 项在t中, 但不在s中
print(x - y)

# 对称差集, 项在t或s中, 但不会同时出现在二者中
print(x ^ y)

# 添加一项
x.add('x')
print(x)

# 添加多项
x.update(['a', 'b', 'c'])
print(x)

# 删除一项
x.remove('s')
print(x)

# 去重, 不用hash方法
a = [11, 22, 33, 44, 11, 22]
b = set(a)
print(b)
c = [i for i in b]
print(c)

