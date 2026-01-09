# l1=[1,2,3,4,5,1,2,3,4,2]
# l2=[]
# l=[]
# for i in range(len(l1)):
#     l=l1[:i]+l1[i+1:]
#      #print(l)
#     if l not in l2:
#         l2.append(l)
# print(l2)


l1=[1,2,3,4,5,1,2,3,4,2]
l2=[]
for i in range(len(l1)):
    l3=[]
    for j in range(len(l1)):
        if i!=j:
            l3.append(l1[j])
    l2.append(l3)
print(l2)