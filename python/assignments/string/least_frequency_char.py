s=input("enter any string")
d={}

for char in s:
    if char not in d:
        d[char]=1
    else:
        d[char]+=1
min_val=min(d.values())
l=[]
for i in d:
   if(d[i]==min_val):
        l.append(i)
print(l)