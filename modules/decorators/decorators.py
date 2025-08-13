def main():
    print("insde the main")
def outer(arg):
    print("insdie the outer ")
    def inner():
        print("inside the inner ")
        arg2=arg
        arg2()
        print("the leaving the innner ")
    return inner()
ref=outer(main)
ref()