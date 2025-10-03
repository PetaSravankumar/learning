import time
class Demo:
    def printName(self):
        l=["rathu","sravan",'suni']
        for i in l:
            print(i)
            time.sleep(3)
    def printNumebers(self):
        for i in range(10):
            print(i)
            time.sleep(2)
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)

d1=Demo()
d1.printName()
d1.printNumebers()