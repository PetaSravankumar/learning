l=[10,20,30]
print(l)
print(type(l))

l1=[10,'sravan',4.3]
print(l1)
print(type(l1))

l2=[]
i=0
while True:
    num=int(input("enter the number :"))
    l2.insert(i,num)
    i=i+1
    print("do you want to continue")
    choose=int(input("enter the choice : 1:yes , 2: No "))
    if choose==1:
        continue
    else:
        break
print(l2)