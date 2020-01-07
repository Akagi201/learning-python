# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:07:18 2019

@author: Dell
"""

#to sort even odd numbers
l=[]
s=int(input("Enter Number of Elements in the List: "))
for i in range(s):
    x=int(input("Enter element in the list: "))
    l.append(x)
e=[]
o=[]
for i in range(len(l)):
    if l[i]%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
print("List of your Even Numbers is:",e)
print("List of your Odd Numbers is:",o)





