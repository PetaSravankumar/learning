l=[]
a=[]
for i in range(3):
    for j in range(3):
        k=int(input("enter the number :"))
        a.append(k)
    l.append(a)
    a=[]
print(l)
sum1=0
sum2=0
for i in  range(len(l)):
    for j in range(len(l[0])):
        if i==j:
            sum1+=l[i][j]
        elif i+j==len(l)-1:
            sum2+=l[i][j]
    print()
print(sum1-sum2)