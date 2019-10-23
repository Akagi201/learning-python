# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:59:06 2019

@author: Dell
"""
"""
#freelancers,fibrepay,upwork
Q1. Using L.C. ,print squares of even number from 1-20
Q2. Using L.C. ,print the vowels present in a given string (entered by a user)
Q3. Using L.C. ,print the string in uppercase.
Q4. WAP to print a matrix.
Q5. WAP to transpose the matrix
Q6. Using L.C. ,print transpose of a matrix.
"""
#P1
list_of_sq_of_even_num=[x*x for x in range(1,21) if x%2==0]
print(list_of_sq_of_even_num)

#P2
word=input("Enter any word or string: ")
word.lower()
list_vowel=[x for x in word if x=='a' or x=='e' or x=='i' or x=='o' or x=='u']
print(list_vowel)

#P3
word=input("Enter a word: ")
list_uppercase_word=[x.upper() for x in word]
''.join(list_uppercase_word)



#P4+P5+P6
e=[]
for i in range(2):
    nl=[]
    for j in range(2):
        x=int(input("Enter element of the matrix: "))
        nl.append(x)
    e.append(nl)
print(e)
print("Matrix :-")
for i in range(2):
    for j in range(2):
        print(e[i][j],end='  ')
    print('',end='\n')   

print("Transpose of the matrix :-")
for i in range(2):
    for j in range(2):
        print(e[j][i],end='  ')
    print('',end='\n')
 
l=[[int(input("Element:")) for x in range(2)] for x in range(2)]
lm=[[print(l[i][j],end='  ')for j in range(2)]for i in range(2)]




#Element in binary or linear search


n=int(input("Enter number of elements in list: "))
l=[int(input("Enter list element: ")) for x in range(n)]  
key=int(input("Enter number you want to find: "))
if len(l)%2==0:
    for i in range(len(l)):
        lb=l[0]
        ub=l[-1]
        x=/2
        mid_e=l[x]
        if key==mid_e:
            print(mid_e.index())
        elif key>mid_e:
            l=l[x+1:]
        else:
            l=l[:x-1]
else:
    for i in range(len(l)+1):
        x=(len(l)-1)
        y=x/2
        mid_e=l[y]
        if key==mid_e:
            print(mid_e.index())
        elif key>mid_e:
            lb=mid_e+1
        else:
            ub=mid_e-1


           
    
    
    
    
    