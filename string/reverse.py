str=input("enter the string  ")
rev=" "
for i in str:
    rev=i+rev
print(rev)

str=input("enter the string  ")
rev=" "
for i in range(len(str)):
    rev+=str[i]
print(rev) 
