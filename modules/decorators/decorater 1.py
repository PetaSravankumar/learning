def main():
    str1=input("enter the string :")
    return str1
def outer(arg1):
    print("inside the outer")
    def inner():
        print("enter the inner")
        agr2=arg1
        str2=agr2()
        str3=str2.upper()
        str4=str2.lower()
        print(str3)
        print(str4)
    return inner
ref=outer(main)
ref()