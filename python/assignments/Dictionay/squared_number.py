n=int(input("enter number u want to see square upto it :"))

d={x:x*x for x in range(1,n+1)}
d1={}
for x in range(1,n+1):
    d1[x]=x*x
print(d1)
print(d)