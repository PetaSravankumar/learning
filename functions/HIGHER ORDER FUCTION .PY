def fun1():
    print("iside the fun1")
def fun2(ref):
    print("Inside the fun2 ")
    res=ref
    res()
fun1()
fun2(fun1)