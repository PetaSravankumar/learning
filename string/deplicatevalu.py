str=input("enter the string : ")
str1=''
for i in str:
    if i in str1:
        str1=str1+'@'
    else:
        str1+=i
print(str1)
