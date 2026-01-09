# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# k=2

# rotate=[]
# rotate=a[len(a)-k:]+a[:len(a)-k]
# print(rotate)

# result=[]



# for i in range(len(b)):
#     result.append(b[i]+rotate[i])
# print(result)
       

a=[1,2,3,4,5]
b=[10,20,30,40,50]
c=[]
k=2  
n=len(a)
k=k%n

for i in range(n-k,n):
    c.append(a[i])
for i in range(n-k):
    c.append(a[i])
print(c)

result=[]
for i in range(len(b)):
    result.append(b[i]+c[i])
print(result)