l=[1,0,3,0,4,9,0,11,4,0,5,0,10]
l1=[]
for i in range(len(l)):
    if l[i]!=0:
        l1.append(i)
    if len(l1)<len(l):
        j=0
        l1.append(j)
print(l1)