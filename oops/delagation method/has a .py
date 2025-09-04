class Radio:
    def turnOn(self,x):
        if x==1:
            print("the radio is on")
        else:
            print("the radio is off")
class car:
    def __init__(self,min,max):
        self.cmin=min
        self.max=max
        self.r=Radio()
c1=car(20,220)
print(c1.cmin)
print(c1.max)
print(c1.r)
c1.r.turnOn(1)
c1.r.turnOn(3)