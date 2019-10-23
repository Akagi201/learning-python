""" CLEAR COMMAND """
l=[1,2,3,4,5,6]
l.clear()
#Use to clear all elements in the list 
# but maintain the id of the objects (erased elements of the list).
print(l)



""" COPY COMMAND """
l=[1,2]
l1=l
#so here actually whats happening a copy of l is not made in l1
#instead l1 will also call the same elements as being called by l.
id(l)
# in python whatever is in square brackets in a list are objects.
id(l1)
#Hence, both the id of l and l1 will be same
#no copy of the list is made.

#so lets do try append 'l1' and see if it affects 'l' or not
 
l1.append(4)
print(l1)# l1 got changed
print(l)# so did l

"""But what if i don't want to change l and 
make l1 a copy of the objects not the pointer of the same objects.
We have a command called copy() in lists """

#Let's use the copy command.
l=[1,2]
l1=l.copy()#makes a copy of object at different ID
print(id(l))
print(id(l1))
l1.append(4)# Will only change l1 not l.
print(l)
print(l1)


""" AN ANALOGY OF THE COPY COMMAND """
""" without copy command """
#Suppose you want to read a novel.
#You asked one of your friends(Srishti) for it.
#She found it in the library and told u it's location
#(same like variable gives you a output via print command)
#You asked another friend(Prashant) too.
#He contacted Srishti and told u about the same location.


""" with copy command """
#Suppose you want to read a novel.
#You asked one of your friends(Srishti) for it.
#She found it in the library and told u it's location
#(same like variable gives you a output via print command)
#You asked another friend(Prashant) too.
#He contacted Srishti and went to the library
#Took a copy of it and added it to his own personal llibrary
#Now told you to come and read it from his library whenever u want to.


l=[1,2,3,4,5,6]
le=[]
for i in l:
    if i%2==0:
        le.append(i)

lee=[i for i in l if i%2==0]

lx=[x**2 for x in l]

import keyword
keyword.iskeyword("1srishti")#willl tell us whether the word is a keyword or not

'1srish'.isidentifier()#helps in identifying whether the name given to any identifier
# is feasible or not but it can't differentiate the keywords



#program to find feasible names of an identifier
#By:-Srishti Singh
c=input("Enter any string: ")
import keyword
if(keyword.iskeyword(c)==False and c.isidentifier()==True ):
    print("It is an identifier")
else:
    print("It is not an identifier")


l=[1,2,3,[4,5],6,7,8]
import copy
a=copy.copy(l)
b=copy.deepcopy(l)
print(a,b)
l[3][0]=10
print(a,b)


#Program to show difference between shallow and deep copy
l=[1,2,3,[4,5],6,7,8]
import copy
a=copy.copy(l)
b=copy.deepcopy(l)
print("Original list:",l)
print("Your Shallow Copied list is:",a)
print("Your Deep Copied list is:",b)
l[3][0]=10
print("Original list after alteration:",l)
print("Shallow Copied list after alteration:",a)
print("Deep Copied list after alteration:",b)

d={"Name":"Srishti Singh","System ID":2018013720,"Course":"B.Tech. CSE with specialisation in A.I. and Machine Learning"}
a=d.keys()
print(a)

s="234"
integer_s=int(s)
float_s=float(s)
tuple_s=tuple(s)
list_s=list(s)
















