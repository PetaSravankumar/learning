from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("bark")
class cat(Animal):
    def make_sound(self):
        print("meow")
d=Dog()
c=cat()
d.make_sound()
c.make_sound()