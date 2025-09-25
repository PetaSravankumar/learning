dic={"name":"sravan","age":35,"gender":"male"}
print(dic)
print(dic["age"])
for i in dic:
    print(i)
print("-------------------------------")
for i in dic:
    print(dic[i])
print("-------------------------------")  
for i in dic.keys():
    print(i)
print("-------------------------------")  
for i in dic.values():
    print(i)
print("-------------------------------")  
for i in dic.items():
    print(i)
dic['clg']='vela'
print(dic)