l=[1,4,3,5,6]
print(l)
for i in range(len(l)//2):
        l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
print(l)
