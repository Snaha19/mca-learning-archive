a=input("enter any string")
b=input("enter any string")
c=''
d=''
for i in a:
    if(i in b):

        c=c+i
if(c==b):
    print("balanced")
for i in a:
    if(i not in c):
        d=d+i
print(d)
