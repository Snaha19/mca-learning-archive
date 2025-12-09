num="12 3 45 9 10 2 100"
a=[]
d=[]

for i in num.split():
    a.append(int(i))
print(a)

def digit_sum(n):
    sum=0
    while(n>0):
        num=n%10
        sum=sum+num
        n=n//10

    return sum

for i in a:
   d.append(digit_sum(i))
   
print(d)

l=[]
for i in range(1,len(d)):
    if d[i] > d[i-1]:
        l.append(a[i])
print(l)