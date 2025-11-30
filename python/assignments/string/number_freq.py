s=input("enter any string")
count=0
s1=''
for i in s:
    if(i.isdigit()):
        if(i not in s1):
         print(i,"   ",s.count(i))
         s1+=i
