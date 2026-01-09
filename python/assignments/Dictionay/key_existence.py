d={}
n=int(input("enter the number of entries :"))
for _ in range(n):
    key=int(input("key"))
    val=input("val")
    d.update({key:val})

print(d)

n=int(input("enter the key u want to search"))
flag=False
for key in d:
    if(n in d):
        flag=True

    else:
        flag=False
        
if flag==True:
    print("found")
else:
    print("not found")