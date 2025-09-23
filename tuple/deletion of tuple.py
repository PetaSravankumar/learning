t=(10,20,30,40)
print(t)
t1=t[:3]+(99,)+t[3:]
print(t1)
t2=t[:3]+t1[4:]
print(t2)

t3=(10,20,("shiva","krishna","kk"),30)
print(t3)
print(t3[3])
print(t3[2][2])