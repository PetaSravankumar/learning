try:
    a=int(input("enter the numbere :"))
    b=int(input("enter the numbere :"))
    res=a/b
    print(res)
except (ValueError,ZeroDivisionError )as e:
    print("it is value error or zero division error")
except Exception as e:
    print("error occured")