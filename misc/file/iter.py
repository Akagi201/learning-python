#!/usr/bin/env python

f = open('file.txt')

iter_f = iter(f)

lines = 0

for line in iter_f:
    lines += 1

print(lines)

