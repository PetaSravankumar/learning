import pickle
class Emp:
    def __init__(self):
        self.name='sravan'
        self.age='21'
    def disp(self):
        print(self.name)
        print(self.age)

f=open('sravan.txt','rb')
e=pickle.load(f)
print("object is retrived")
e.disp()