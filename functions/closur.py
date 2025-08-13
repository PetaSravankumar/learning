def outer():
    print('inside the outer function')
    def inner():
        print("insdie the inner function")
    return inner
res=outer()
res()
print(res())