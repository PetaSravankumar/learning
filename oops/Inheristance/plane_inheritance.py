class Plane:
    def takeOff(self):
        print("the plane is take off")
    def fly(self):
        print("the palne is flying ")
    def land(self):
        print("the plane is landing")
class Passenger(Plane):
    def carry_p(self):
        print("the palne is carring the passengers")
class Cargo(Plane):
    def carry_c(self):
        print("the palen is carring the cargo")
class fighter(Plane):
    def carrY_w(self):
        print("the plane is carring the wepons")
p1=Passenger()
c1=Cargo()
f1=fighter()
p1.carry_p()
p1.fly()
p1.land()
p1.takeOff()
print("--------------------------------------------")
c1.takeOff()
c1.carry_c()
c1.fly()
c1.land()
print("--------------------------------------------")
f1.land()
f1.carrY_w()
f1.fly()
f1.takeOff()