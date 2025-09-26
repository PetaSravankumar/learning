import copy
circket={"name":"virat",'century':82,"egfgs":{"num1":"genelia","num2":"ritika"}}
print(circket)
c1=circket.copy()
print(c1)
c2=circket.copy()
print(c2)
circket["egfgs"]['num3']="tamanla"
print(c2)
print(c1)