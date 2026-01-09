list1=[1,2,3,4,5]
k=3
list2=[]
for i in range(len(list1)-k+1):
    w=list1[i:i+k]
    total=0
    for i in w:
        total+=i
    avg=total/k
 
    sum=0
    var=0
    for i in w:
        sum+=(i-avg)**2
    var=sum/k

    list2.append((avg,var))
print(list2)