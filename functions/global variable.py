a=10
def fun1():
    #global a
    a=100
    b=200
    print(a)
    print(b)
def fun2():
    #global a
    a=150
    c=500
    print(a)
    print(c)
print(a)
fun1()
print(a)
fun2()
print(a)