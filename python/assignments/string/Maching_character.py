s=input("enter any string")
s1=input("enter any string")
count=0
for i in set(s):
    if(i in set(s1)):
        count+=1
        
    
print(count)
