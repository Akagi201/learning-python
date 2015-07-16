#!/usr/bin/env python

l = [5, 2, 3, 1, 4]
print(l)

b = sorted(l)
print(b)

l.sort()
print(l)

dict = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
dict_sorted = sorted(dict)
print(dict)
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

a1 = "This is a test string from Andrew"
a2 = a1.split()
print(a2)

a3 = sorted(a2, key=str.lower)
print(a3)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda student: student[2])) # sort by age