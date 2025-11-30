#alternating seq
n=int(input("enter no of integer u want to enter"))
s=''
c=0
for i in range(n):
    num=int(input("enter integers"))
    if c==0:
        if(num%2==0):
          s=s+str(num)+' '
          c=1
    elif c==1:
        if(num%2!=0):
            s=s+str(num)+' '
            c=0
print(s)
