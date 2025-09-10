def fun1():
    print("entering the fun1")
    try:
        fun2()
    except Exception as e:
        print("error occured in fun1")
    print("leaving the fun1")
def fun2():
    print("entering the fun2")
    res=10/0
    print(res)
    print("leaving the fun2")
print("programm is started")
fun1()
print("programming isended")