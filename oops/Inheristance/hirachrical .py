class A:
    def fun_A(self):
        print("inside the a")
class B(A):
    def fun_B(self):
        print("inside the B")
class C(A):
    def fun_C(self):
        print("insise the c")
c=C()
c.fun_C()
B=B()
B.fun_A()