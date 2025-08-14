def outer():
    a=10
    b=20
    print(a)
    print(b)
    print("outer function")
    def inner():
        nonlocal a
        a=100
        d=300
        print(a)
        print(d)
        print('inside fun')
    print(a)
    inner()
    print(a)
outer()


