s=input("enter any string")
k=int(input("enter the length : "))
for i in s.split():
    if(len(i)>k):
        print(i)