## sum even and od seperately
n=int(input("enter how many interer u want to write :"))
e_sum=0
o_sum=0
for i in range(1,n+1):
    num=int(input("enter ur numbr :"))
    
    if(num%2==0):
        e_sum+=num
    else:
        o_sum+=num
print("even sum :",e_sum)
print("odd sum  :",o_sum)
