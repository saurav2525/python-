#Verify Leap Year
year=int(input("enter the year"))
if((year%4==0) or (year%400==0) and (year%100!=0)):
    print("leap year")
else:
    print("not a leap year")
#Check Whether the Given Dimensions Are of Square or Rectangle
leng=int(input("enter the length"))
brea=int(input("enter the breadth"))
if(leng==brea):
    print("SQUARE")
else:
    print("RECTANGLE")
#Determine Oldest and the Youngest Age
age1=int(input("enter the age1"))
age2=int(input("enter the age2"))
age3=int(input("enter the age3"))
print("oldest : " ,max(age1,age2,age3), "youngest : " ,min(age1,age2,age3)) 
#Analyse the Given Data
age=int(input("enter the age"))
sex=input("Male or Female")
status=input("Yes or No")
if(sex=='Female'):
    print("She will work only in urban areas")
elif(sex=='Male' and(age>=20 and age<=40)):
    print("He may work anywhere")
elif(sex=='Male' and(age>40 and age<=60)):
    print("He will work in urban areas only")
else:
    print("Error")
#Question 5
qty=int(input("Enter quantity"))
cost=100
total_cost=qty*cost
if(total_cost>1000):
    total_cost-=total_cost/10
print("Total cost",total_cost)
#Question 6
list=[]
for i in range(10):
    num=input("Enter integer")
    list.append(num)
print(' '.join(list))
#Question 7
while(1):
   print("This will print infinite times")
#Question 8
l1=[int(input("Enter integer: "))for i in range(5)]
l2=[i*i for i in l1]
print(l2)
#Question 9
l1=[1,'abc',99,9,44.4,'xyz',2,3,'ijk',1.1]
l1_int=[]
l2_float=[]
l3_string=[]
for i in l1:
    if(type(i)==int):
        l1_int.append(i)
    elif(type(i)==float):
        l2_float.append(i)
    else:
        l3_string.append(i)
print("Integer list: ",l1_int)
print("Float list: ",l2_float)
print("String list: ",l3_string)
#Question 10
l_prime=[]
for i in range(1,101):
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            break
    else:
        l_prime.append(i)
print("List of prime no. is",l_prime)
#Question 11
for i in range(4):
    for j in range(i+1):
        print("*",end=' ')
    print()
#Question 12
list=[input("enter element:")for i in range(5)]
search=input("element to be searched")
for i in list:
    if(search==i):
        list.remove(i)
print("Updated list is: ",list)
    
