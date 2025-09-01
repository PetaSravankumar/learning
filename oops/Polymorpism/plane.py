class plane:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
class passenger(plane):
    def land(self):
        print("plane us landng")
class cargo(plane):
    def land(self):
        print("plane us landng")
class fighter(plane):
    def land(self):
        print("plane us landng")
p1=passenger()
c1=cargo()
f1=fighter()
def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
allowplane(p1)
allowplane(c1)
allowplane(f1)