#!/usr/bin/env python

a = []
b = {'num': 0, 'square': 0}

resurse = [1, 2, 3]

for i in resurse:
    b['num'] = i
    b['square'] = i * i
    a.append(b)

print a

a = []
resurse = [1, 2, 3]
for i in resurse:
    a.append({"num": i, "square": i * i})

print a