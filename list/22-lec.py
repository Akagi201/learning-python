# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:37:23 2019

@author: Dell
"""
 
import random
l=[2,3,4,3,3,4,1,2,3]
random.shuffle(l)
print(l)

random.randint(2,3)
s="hello"#firstly string is converted to lower case firstly and output is always in uppercase
s.startswith('h')#check whether starting word is h
s.endswith('O')

s={1,2,3,3,4,5,6}
print(s)

s="hello"
ss=set(s)
print(ss)

ss.add(40)
ss.update(["orange"])#Always give articles in form of a list
print(ss)


s="hello"
ss=set(s)
print(ss)
ss.update("orange")
print(ss)

#remove an item from set
ss.remove('h')

ss.discard('o')

del(ss)

sset=set(("orange","apple"))
print(sset)