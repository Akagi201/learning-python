# !/usr/bin/env python

# http://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

# when ues an iterable, you store all the values in memory

# iterables
mylist = [1, 2, 3]
for i in mylist:
    print(i)

# list comprehension
mylist = [x * x for x in range(3)]
for i in mylist:
    print(i)

# generators
# Generators are iterators, but you can only iterate over them once.
# Its because they do not store all the values in memory, they generate the values on the fly.

mygenerator = (x * x for x in range(3))
for i in mygenerator:
    print(i)

# yield

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i

# create a generator
mygenerator = createGenerator()

# mygenerator is an object!
print(mygenerator)

for i in mygenerator:
    print(i)
# when you call the function, the code you have written in the function body does not run.
# your code will be run each time the for uses the generator.
