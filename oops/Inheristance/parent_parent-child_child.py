class A:
    def __init__(self):
        self.a=100
class B(A):
    def __init__(self):
        A.__init__(self)
        self.b=200
class C(B):
    def __init__(self):
        B.__init__(self)
        self.c=300
C1=C()
print(C1.c)
print(C1.b)
print(C1.a)