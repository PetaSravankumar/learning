l=[]
i=0
while i<=4:
    num=int(input('enter the numwber :'))
    l.append(num)
    i+=1
print(l)
res=list(map(lambda num:num*num,l))
print(res)