ptr=open('sravan.txt','r')
pos=ptr.tell()
print(pos)

res=ptr.read(4)
print(res)
pos1=ptr.tell()
print(pos1)

res1=ptr.seek(2)
print(res1)

pos2=ptr.tell()
print(pos2)
ptr.close()