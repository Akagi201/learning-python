#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 直接遍历删除
l = [1, 2, 3, 4]

for i in l:
    if i != 4:
        l.remove(i)

print l

# 利用index来遍历删除
l = [1, 2, 3, 4]
# l = [1, 2, 3, 4, 5]

for i in range(len(l)):
    if l[i] == 4:
        del l[i]

print l

print("倒序删除")

# 倒序删除
l = [1,2,3,4,5]
for i in range(len(l) - 1, -1, -1):
    print i,l[i]
    if l[i] == 4:
        del l[i]

print l

# filter
l = [1, 2, 3, 4]
l = filter(lambda x: x != 4, l)
print l

# 产生一个新序列, 赋值给l

l = [1, 2, 3, 4]
l = [i for i in l if i != 4]
print l


# 建立新的list存放要删除的元素
l = [1,2,3,4]
dellist = []
for i in l:
    if i == 4:
        dellist.append(i)

for i in dellist:
    l.remove(i)

l = [1,2,3,4]
ll = l
l.remove(1)

print l
print ll
print id(l)
print id(ll)




