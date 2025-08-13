def fun():
    print("the inside the fun")
def fun2():
    print("insede the second funtion")
print(fun)
print(fun2)
ptr=fun
ptr2=fun2
ptr()
ptr2()
print(ptr)
print(ptr2)