s=input("enter a binary string: ")
num=0
power=len(s)-1
for i in s:
    num+=(ord(i)-48)*pow(2,power)
    power-=1
print("the integer value is: ",num)