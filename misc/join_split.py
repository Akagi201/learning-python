#!/usr/bin/env python

# join
li = ['my', 'name', 'is', 'bob']
output = ' '.join(li)
print(output)

output = '_'.join(li)
print(output)

# split
b = 'my..name..is..bob'

output = b.split()
print(output)

output = b.split("..")
print(output)

output = b.split("..", 0)
print(output)

output = b.split("..", 1)
print(output)

output = b.split("..", 2)
print(output)

output = b.split("..", -1) # <==> b.split("..")
print(output)
