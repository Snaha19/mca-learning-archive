## print the multiple with skip
n=int(input("enter no of integer u want to enter :"))
k=int(input("enter an integer k :"))
counter=0
s=''
for i in range(n):
    num=int(input("enter integers :"))
    if(num%k==0):
        if counter==0:
            counter=1
            continue
        s=s+str(num)+"  "
print(s)
