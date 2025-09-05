class os:
    def __init__(self):
        self.status=True
        print("os is ready")
    def getOs(self):
        print("os is installing")
class mobile:
    def __init__(self,name):
        self.cname=name
        self.o=os()
        print("mobile is redy")
        print("with the os is installed")
m1=mobile("samsung")
m1.o.getOs()
del m1
print(m1.o.status)