str=input("enter the string: ")
rev=""
for i in str:
    rev=i+rev
print(rev)
if rev==str:
    print("palli")
else:
    print("non palli")