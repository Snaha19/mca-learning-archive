d={}
n=int(input("enter number of time u want to add loop :"))

for _ in range(n):
    key=int(input("enter key :"))
    val=int(input("enter val"))
    d[key]=val
print(d)

max_val=-1
max_key=''
for i in d:
    if(max_val<d[i]):
        max_val=d[i]
        max_key=i
print(max_key,max_val)

min_val=999
min_key=''
for i in d:
    if(min_val>d[i]):
        min_val=d[i]
        min_key=i
print(min_key,min_val)

