d={}
n=int(input("enter the number of entries :"))
for _ in range(n):
    key=int(input("key"))
    val=input("val")
    d.update({key:val})

print(d)

for i,j in d.items():
  print(i,j)
