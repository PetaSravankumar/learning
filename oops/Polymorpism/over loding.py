class A:
    def disp(self,a):
        print(a)
class B(A):
    def disp(self,a,b):
        print(a)
        print(b)
class c(A):
    def disp(self,a,b,c):
        print(a)
        print(b)
        print(c)
c1=c()
c1.disp(10,20,30)
c1.disp(10)
