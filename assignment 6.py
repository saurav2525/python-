#Ques 1
def area_sphere(r):
    return 4*3.14*r*r 
r=int(input('Enter radius of sphere: '))
a=area_sphere(r)
print('Area of sphere is',a)

#Ques 2

def perfect(n):
    sum=0
    for i in range(1,n//2+1):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    return False
print("List of Perfect numbers is:")
for i in range(1,1001):
    if(perfect(i)):
        print(i)

#Ques 3

n=int(input("Enter integer: "))
print("Table of",n,"is:")
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#Ques 4

def power(a,b):
    if(b!=0):
        b-=1
    else:
        return 1
    return a*power(a,b)
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(a,"^",b,"=",power(a,b))
