# 1. WAP to create and merge two list and then sort it wihtout function sort
# 2. WAP to create list of number and sort even numbers using LIST COMPREHENSION
# 3. WAP to calculate number of uppercase and lowercase from input string.

l1=[]
l2=[]
a=int(input("Enter number of elements you want to enter in list 1: "))
b=int(input("Enter number of elements you want to enter in list 2: "))

for i in range(a):
    x=int(input("Enter List Element: "))
    l1.append(x)

for i in range(b):
    x=int(input("Enter List Element: "))
    l2.append(x)
                
l1.extend(l2)
m=[]
for i in range (len(l1)):
    m.append(min(l1))
    l1.remove(min(l1))
m.extend(l1)
print(m,end=" ")
print("is your sorted list")

#P2

l=[]
a=int(input("Number of elements in the list: "))

for i in range(a):
    x=int(input("Enter List Element: "))
    l.append(x)
    
lee=[i for i in l if i%2==0]
print("List of your even numbers is={evenlist}".format(evenlist=lee))
    
#P3    

s=input("Enter any word string: ")
cu=0
cl=0
for i in s:
    if i.isupper():
        cu=cu+1
    else:
        cl=cl+1
print("Number of lower case:",cl)
print("Number of upper case:",cu)
         
        
        
    
                


