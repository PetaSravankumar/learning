import copy
l=[10,20,['kumar','sravan','sam'],40]
print(l)
l1=copy.deepcopy(l)
print(l1)
print(l)
l[2][2]='sumo'
print(l)
print(l1)