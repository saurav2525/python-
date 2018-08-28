#Create a List
list=[]
n=int(input("Enter the size of list"))
print("Enter elements of the  list")
for i in range(0,n):
    a=input()
    list.append(a)
print(list)
#Add the following list to above created list: 
list2=["google","apple","facebook","microsoft","tesla"]
list.extend(list2)
print(list)
#Count the Occurance in a List
for x in list:
    a=list.count(x)
    print("count of %s in list is %d" %(x,a))
#sort
list3=[1,1,9,8,0,5,6,7,4,8,10,11]
list3.sort()
print(list3)
#Concatinate and Sort 2 Sorted Arrays
l1=[10,1,45,23,78,65]
print(l1)
l2=[0,2,3,4,5,7]
print(l2)
l1.extend(l2)
l1.sort()
print(l1)
#Count Even and Odd Neumbers in a List
counteven=0
countodd=0
for i in l1:
    if(i%2==0):
        counteven+=1
    else:
        countodd+=1
        
print('odd count: ',countodd)
print('even count: ',counteven)


#TUPLES
#Print a Tuple in Reverse Order
t=("saurav","saaaa","sjjdjfd","assfddd")
print(t)
s=reversed(t)
print(tuple(s))
#Find largest and smallest elements of a tuple
t1=(1,5,7,3,10,4,14)
print("Largest= ",max(t1))
print("Smallest= ",min(t1))
#Convert a String to Uppercase
str="my name is saurav"
print(str.upper())
#Check If the String Contains All Numeric Characters
val=input("enter a string\n")
c=0
for i in range(len(val)):
    if val.isdigit():
        c=1
    else:
        c=0
        break;
if c==1:
    print("True")
else:
    print("False")
#Replce the Given String With Your Name
str2="hello hii"
str3=str2.replace("hii","Saurav")
print(str3)
    

          
          
    
