class A:
    def disp(self):
        print("Inside the A")
class B(A):
    def disp(self):
        print("inside the B")
class C(B):
    def disp(self):
        print("Inside the c")
c1=C()
c1.disp()
c1.disp()
c1.disp()