#Get Keys Corresponding to a Value in User Defined Dictionary
d=eval(input("enter dictionary"))
for key in d:
    print(key,d[key])
#Nested Dictionary
dic={}
dic2={}
for i in range(3):
    name=input("enter the name of students: ")
    print("student",name,":")
    for marks in range(3):
        s=input("enter subject: ")
        m=int(input("enter marks: "))
        dic2[s]=m
        dic[name]=dic2.copy()
        dic2.clear()
name=input("enter name")
for i in dic.keys():
    if(nam==i):
        print(dic[name])
        break
    else:
        print("Name",name,"not found")
