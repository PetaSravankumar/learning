try:
    a=int(input("enter the numbere :"))
    b=int(input("enter the numbere :"))
    res=a/b
    print(res)
except ValueError as e:
    print("it is value error")
except ZeroDivisionError :
    print("dividing with the zero")
except Exception as e:
    print("error occured")