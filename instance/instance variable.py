class car:
    def __init__(self,name,age):
        self.brand=name
        self.age=age
    def start(self):
        self.brand='tata'
        print(self.brand)
c1=car('curv',21)
c2=car('honda',21)
print(c1)
print(c2)
print(c1.brand,c1.age)
c1.start()
c1.price=250000
print(c1.price)
