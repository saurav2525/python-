import math
##  Ques 1
list1=[1,2,3,4]
cube=[x**3 for x in list1]
print(cube)

##Ques 2
list_2=[x for x in range(1,15) if all(x%i!=0 for i in range(2,(int(x/2)+1)))]
print(list_2)

##Ques 3
'''A list comprehension '[]' executes immediately and returns a list
whereas a Generator expression '()' returns an object that can be iterated'''

##Lambda & Map
##Ques 4
Celsius = [39.2, 36.5, 37.3, 37.8]
a=list(map(lambda x:(9/5)*x+32,Celsius))
print(a)

##Ques 5

sq_num=(lambda x:x*x)
print(sq_num(5))

##Filter & Reduce
##Ques 6
n=int(input('Enter number of elements'))
p_list = []
l=[]
print('Enter the elements')
l=[int(input()) for i in range(0,n)]
def prime(x):
    flag=0
    for i in range(2,x):
        if(x % i == 0):
            return False
    if (flag == 0):
        return True
p_list= list(filter(prime, l))
print(p_list)

##Ques 7
from functools import *
n=int(input('Enter number of elements'))
mullist = []
l=[]
print('Enter the elements')
l=[int(input()) for i in range(0,n)]
mullist= reduce(lambda x,y : x*y, l)
print(mullist)
