import pickle
class Emp:
    def __init__(self):
        self.name='sravan'
        self.age='21'
    def disp(self):
        print(self.name)
        print(self.age)
e1=Emp()
print(e1.disp())