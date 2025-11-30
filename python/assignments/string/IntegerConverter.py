s=input("enter a string: ")
num=0
for i in s:
    num=num*10+(ord(i)-48)
print("the integer value is: ",num)