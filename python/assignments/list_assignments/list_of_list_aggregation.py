sales=[

    [5,3,0,2],
    [7,0,2,1],
    [0,1,4,0]
]
l=len(sales[0])
# print(l)
t=[0]*l
# print(t)
for i in sales:
    for j in range(len(i)):
        t[j]=t[j]+i[j]

max_v=max(t)
min_v=min(t)

print(max_v)
print(min_v)  
print(t)  

