class A:
    def fun_A(self):
        print("inside the a")
class B(A):
    def fun_B(self):
        print("inside the B")
class C(B):
    def fun_C(self):
        print("insise the c")
c=C()
c.fun_B()