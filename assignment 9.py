#Question1
a=3
if(a<=4):
    try:
        a=a/(a-3)
    except ZeroDivisionError:
        print("It is a zero division error")
#Question2
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("It is an index error")
#Question3
#try:
 #   raise NameError("Hi there")
#except NameError:
 #   print("An exception")
  #  raise
#Question4
#answer---
#a)it will print the value of c.
#b)it will then print exception error message(ZeroDivisionError)
#Question5-Value error
try:
    number=int(input("Enter only number"))
except ValueError:
    print("Error!!! numbers only")
else:
    print(number)
#Index error
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("it is an index error")
#import error
try:
    print(sys.version)
except:
    print("Import error")
