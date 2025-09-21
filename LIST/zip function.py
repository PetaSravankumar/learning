from itertools import zip_longest
name=["virat","dhoni","ABD","maxwell"]
f_nam=[18,7,17,32]
country=["ind","indi"]
ipl=['rcb','csk','rcb','pb']
res=list(zip(name,f_nam,country,ipl))
print(res)

res1=list(zip_longest(name,f_nam,country,ipl))
print(res1)

res2=list(zip_longest(name,f_nam,country,ipl,fillvalue="**"))
print(res2)
print(res2)