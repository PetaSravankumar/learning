import copy
circket={"name":"virat",'century':82,"egfgs":{"num1":"genelia","num2":"ritika"}}
print(circket)
c1=circket.copy()
print(c1)
c3=circket.copy()
c2=copy.deepcopy(circket)
print(c3)
circket["egfgs"]['num3']="tamanla"
print(c3)
print(c1)
print(c2)