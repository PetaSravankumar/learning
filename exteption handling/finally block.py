def fun1():
    print("entering the fun1")
    try:
        fun2()
    except Exception as e:
        print("error occured in fun1")
    print("leaving the fun1")
def fun2():
    print("entering the fun2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("error is occured")
        raise e
    finally:
        print("leaving the fun2")
print("programm is started")
fun1()
print("programming is ended")