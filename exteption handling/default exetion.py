try:
    a=int(input("enter the numbere :"))
    b=int(input("enter the numbere :"))
    res=a/b
    print(res)
except Exception as e:
    print("error eccord")
    print(e)
    print(e.__str__())