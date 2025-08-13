str=input("enter a string")
print(str)
if str.isalpha():
    print("str conatins the alpha")
elif str.isdigit():
    print("str conatains the number")
elif str.isalnum():
    print("str conatains the both")
else:
    print('special character')