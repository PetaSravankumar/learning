def even(num):
    if num%2==0:
        return True
    else:
        return False
li=[]
i=0
while i<4:
    num=int(input("enter the numeber :"))
    li.insert(i,num)
    i+=1
print(li)
i=0
while i<4:
    res=li[i]
    ref=even(res)
    if ref==True:
        print(li[i])
    i+=1