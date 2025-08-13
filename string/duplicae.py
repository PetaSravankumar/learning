str=input("enter the string: ")
sr1=""
for i in str:
    if i=='a':
        sr1=sr1+'@'
    else:
        sr1+=i
print(sr1)
