l=[]
a=[]
for i in range(3):
    for j in range(3):
        k=int(input("enter the number :"))
        a.append(k)
    l.append(a)
    a=[]
print(l)
for i in  range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j],end=" ")
    print()