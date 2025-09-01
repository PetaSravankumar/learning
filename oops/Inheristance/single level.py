class A:
    def fun_A(self):
        print("inside the a")
class B(A):
    def fun_B(self):
        print("inside the B")
b=B()
b.fun_B()