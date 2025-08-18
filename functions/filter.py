def even(num):
    if num%2==0:
        return True
    else:
        return False
li=[]
i=0
print(li)
while i<4:
    num=int(input("enter the number "))
    li.append(num)
    i+=1
print(li)
res=list(filter(even,li))
print(res)