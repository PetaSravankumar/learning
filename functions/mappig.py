def add(num):
    return num*num
li=[]
i=0
while i<=4:
    num=int(input("enter the number :"))
    li.append(num)
    i+=1
print(li)
res=list(map(add,li))
print(res)