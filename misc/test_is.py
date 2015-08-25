#!/usr/bin/env python
# -*- coding utf-8 -*-
# "is"的作用是判断是否是同一实例, "==" 的作用是取值(我们感兴趣的). 也能从另一角度看出来, 操作符"=="能通过方法__eq__()重载, 也就是允许去比较对象中我们感兴趣的东西. (在C 中, 判断两个东西的同一性实际都是靠取值, 也就是变量或指针的"=="操作; Java中则相反, Java的"=="相当于Python的"is", 对于值的比较Java中用Equal()方法.)

a = 1
b = 1
print(id(a))
print(id(b))

print(id(a) == id(b))

print(a == b)

print(a is b)

a = ''
b = ''
print(a is b)

a = ()
b = ()
print(a is b)

a = []
b = []
print(a is b)
print(a == b)

a = {}
b = {}
print(a is b)
print(a == b)

a = 1L
b = 1L
print(a is b)

a = 1.1
b = 1.1
print(a is b)



