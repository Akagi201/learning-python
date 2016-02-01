#!/usr/bin/env python
# http://www.mojidong.com/python/2013/05/10/python-exec-eval/

a = 1
print(eval("a + 1"))

a = 1
g = {
    'a': 10
}
print(eval("a + 1", g))

a = 10
b = 20
c = 20
g = {
    'a': 6,
    'b': 8
}
l = {
    'b': 9,
    'c': 10
}
print(eval("a+b+c", g, l))

print(eval('abs(a)',{'__builtins__':__builtins__, 'a':-1}))
# eval('abs(a)',{'__builtins__':None, 'a':-1})
