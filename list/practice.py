"""
Q1. WAP that will create a new list of age given the list of year of birth using list comprehension.
Q2. Create a list which will print all the characters in a string which are not vowels using list
    comprehension.
Q3. Create a list of squares of numbers given a list of ten numbers using list comprehension.
Q4. WAP which will input a string from the user and gives the list of first letter of every word
    in the list using list comprehension.
Q5. WAP to create a tuple containing types of fishes and using list comprehension print all the items 
    of the tuple if item is not octupus.
Q6. Differentiate between deep copy and shallow copy.
Q7. Write some of the features of python.
Q8. How will you get all the keys from the dictionARY.Write a small program to demonstrate it.
Q9. Do following conversions:
    String to integer
    String to long
    String to float
    String to a tupple
    String to a list
    String to a set
    String to a dictonary
Q10.Create a dictionary using tupple.
Q11.What do you understand by frozen set.
Q12.What is the purpose of following operators:-
      1) **
      2) //
      3) is
      4) not in
"""
#break and continue
#P1
List_Year=[]
n=int(input("Enter number of elements in your list: "))
for i in range(n):
    x=int(input("Enter Year Of Birth: "))
    List_Year.append(x)
List_age=[2019-x for x in List_Year]
print("LIst of Ages are: ",List_age)

#P2
s=input("Enter a string: ")
l=[x for x in s if x not in ['a','e','i','o','u']]
print("Your list of consonants is:",l)

#P3
a=int(input("Enter starting number: "))
l=[x**2 for x in range(a,a+10)]
print("Your list of square of numbers is:",l)

#P4
s=input("Enter any string: ")
ls=s.split()
l=[x[0] for x in ls ]
print("Your first letter of all words are:",l)

#P5
List=[]
n=int(input("Enter number of fishes in your list: "))
for i in range(n):
    x=input("Enter Name of Fish: ")
    List.append(x)
t=tuple(List)
l=[x for x in t if x !='octopus']
print("Your list is:",l)


#FEB 5/2019
#Some more functions on lists and tupples and dictionaries.

t=(23,45,67,78)
len(t)
max(t) #Only works when we have same datatypes ,in string compares ASCII value.
min(t)

d1={'aman':1,'srishti':2,'babita':3}
s=str(d1)
print(s)

#dict also has clear and copy(it makes a deep copy.) as lists. simple assignment gives (shallow copy).

seq={'name','class','roll'}
dict1={}
dict1= dict1.fromkeys(seq,10)#wiillform keys as elements of seq and every key has a value 10
print(dict1)
l1=[1,2,3]
dict1=dict1.fromkeys(l1)#form keys as that of l1

dict1={'1':1,'2':2,'3':3}

#we can delete anything using del(list,tupple,lists).



#Q1. Count the number of words in a string.
#Q2. Calculate factorial of a function using functions.

#P1
para=input("Enter a paragraph: ")
para.lower()
paral=para.split()
dict1={}
dict1=dict1.fromkeys(paral,0)
for p in paral:
    dict1[p]=dict1[p]+1
print(dict1)

para=input("Enter a paragraph: ")
para.lower()
l=para.split()
d={}
for i in l:
    d[i]=d.get(i,0)+1

#P2
def facto(n):
    if n==1:
        return (1)
    elif n>1:
        return n*facto(n-1)
    else:
        print("Error!!! Negative numbers don't have a factorial")
num=int(input("Enter the number whose factorial you want to find: "))
print("Your {number}! is: {factorial}".format(number=num,factorial=facto(num)))


#Create a function to check whether input is interger or not.
#Create a function to find lcm of two given number.
#Create a function which will give sum of ASCII values of all the characters in a string.
#Create a function to check whether the numbers is prime or not.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check(i):
    if i-round(i)==0 :
        print("It is an interger")
    else:
        print("It is not an integer")
a=float(input("Input: "))
check(a)

def check(i):
    if type(i)==type(1):
        print("It is an integer")
    else:
        print("It is not an integer")
#---------------------------------------------------------------------------------------------------------------------
def lcm(a,b):
    z=max(a,b)
    l=[]
    m=[]
    n=[]
    for i in range(1,z+1):
        if a%i==0 and b%i==0:
            l.append(i)
            a=a/i
            b=b/i
        if a%i==0 and b%i!=0:
            m.append(i)
            a=a/i
        if a%i!=0 and b%i==0:
            n.append(i)
            b=b/i
    print(l)
    print(m)
    print(n)
    lm=l+m+n
    print(lm)
    x=1
    for i in lm:
        x=x*i
    return(x)
lcm(12,14)           
    
    
    
















































