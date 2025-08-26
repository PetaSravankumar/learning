class Animal:
    def eat(self):
        print("the animal is eating")
    def sleep(self):
       print("the animal is sleeping")
    def hunt(self):
        print("the animal is eating")
class lion(Animal):
    pass
class tiger(Animal):
    pass
class dog(Animal):
    pass
l1=lion()
t1=tiger()
d1=dog()
l1.eat()
l1.hunt()
l1.sleep()
t1.sleep()
t1.eat()
t1.hunt()
d1.hunt()
d1.eat()
d1.sleep()