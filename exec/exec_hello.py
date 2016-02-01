#!/usr/bin/env python
# http://www.mojidong.com/python/2013/05/10/python-exec-eval/

a = 2
exec "a=1"
print(a)

a = 10
b = 20
g = {
    'a':6,
    'b':8
}
exec "global a; print a,b" in g

a = 10
b = 20
c = 20
g = {
    'a':6,
    'b': 8
}
l = {
    'b':9,
    'c':10
}
exec "global a;print a,b,c" in g,l
