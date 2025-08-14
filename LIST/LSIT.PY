n=int(input("enter the number of time to of list size  :"))
li=[]
for i in range(n):
    num=int(input("enter the number :"))
    li.append(num)
print(li)

i=0
while i< n:
    num1=int(input("ente the number :"))
    li.insert(i,num1)
    i=i+1
print(li)