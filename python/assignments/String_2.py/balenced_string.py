a=input("enter any string :")
b=input("enter any string :")
c=''
l=[]
for i in a:
    if(i in b):
        c+=i
#print(c)
if(c==b):
    print("true")
else:
    print("false")
for i in a:
    if(i not in b):
        l.extend(i)
print(l)