class Brain:
    def __init__(self):
        self.memeory='120gb'
    def getBrain(self):
        print("The brain is braining")

class car:
    def __init__(self,name):
        self.cname=name
    def getCar(self):
        print("the car is driving")
class person:
    def __init__(self):
        self.b=Brain()
        self.c=""
    def hasCar(self,p):
        self.c=p
        print("the c is the address ")
c1=car('tata')
p1=person()
p1.hasCar(c1)
p1.c.getCar()
print(p1.c.cname)
