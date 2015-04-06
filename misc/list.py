#!/usr/bin/env python

# Python 3: List comprehensions

fruits = ['Banana', 'Apple', 'Lime']

loud_fruits = [fruit.upper() for fruit in fruits]

print(loud_fruits)

# List and the enumerate function
print(list(enumerate(fruits)))
