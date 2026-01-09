l1=[]
n1=int(input("enter how many num u want to :"))
for i in range(n1):
  val=int(input("enter elements :"))
  l1.append(val)
l3=set(l1)
print(list(l3))
len_l3=len(l3)

l2=[]
for i in range(len_l3):
  val=input("enter elements :")
  l2.append(val)
print(l2)

d=dict(zip(l3,l2))
print(d)