class charage:
    def __init__(self,name):
        self.cname=name
    def getcharge(self):
        print("moble charage")
class moble:
    def __init__(self,name):
        self.mname=name
        self.c=""
    def hasMobile(self,p):
        self.c=p
c1=charage('220 watt')
m1=moble("mi")
m1.hasMobile(c1)
print(m1.c.cname)
m1.c.getcharge()
del m1
print(c1.cname)