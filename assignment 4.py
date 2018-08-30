#Reverse the List
l=[1,2,3,4,5,6,7]
l.reverse()
print(l)
#Extract all the uppercase letters from a string
str=input("enter any string \n")
for i in str:
    if(i>="A" and i<="Z"):
        print(i,end="")
#Split and Store the Values After TypeCasting
n=input("enter the number using commas: ").split(",")
list=[]
for i in n:
    b=int(i)
    list.append(b)
print(list)
#Check for Palindrome
str1=input("enter any string: ")
str2=str1[::-1]
if(str1==str2):
    print("String is palindrome")
else:
    print("String is not a palindrome")
#Understand Deep and Shallow Copy
import copy

old_list=[[1,1,1],[2,2,2],[3,3,3]]
new_list=copy.deepcopy(old_list)
old_list[1][0]='BB'
print("Old list: ",old_list)
print("New list: ",new_list)
