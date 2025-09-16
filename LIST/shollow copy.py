# 
# shallow copy
#

l=[10,20,30,40]
print(l)
l1=l
print(l1)
print(l)
l[2]=300
print(l)
print(l1)


##
## deep copy
##

li=[10,20,['krisna','radha','rama'],30,50,5,60]
print(li)
li1=li.copy()
print(li)
print(li1)
li1[1]=22
li[2][1]='rupmini'
print(li)
print(li1) 
