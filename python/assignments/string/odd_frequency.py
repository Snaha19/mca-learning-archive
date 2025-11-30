s=input("enter any string")
s1=''
for i in s:
    if (s.count(i)%2!=0):
        if(i not in s1):
            print(i)
            s1+=i