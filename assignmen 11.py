#Question1
import re
a=re.finditer('[a-zA-Z0-9_.]*[@](gmail.com|yahoo.com)','sauravpreet@gmail.com_spsingh@yahoo.com')
print('Email id:')
for i in a:
    print(i.group())
#Question2
a=re.finditer('[+][9][1][-][6-9][0-9]{9}','+91-8146355297 lmn +91-8146155197')
print("Phone number:")
for i in a:
    print(i.group())
