s=input("enter any string")
l=[]
for i in s:
 if(i.isdigit()):
        l.append(int(i))

print(l)
if(l==list()):
    print("no digit found")

else:
    s=0
    for i in l:
        s=s+i
    print("sum :",s)
    print("avg :",s/len(l))
    print("max :",max(l))
    print("min :",min(l))
