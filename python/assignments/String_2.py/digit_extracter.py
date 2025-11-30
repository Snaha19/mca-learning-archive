s1=input("enter any string: ")
l=[]
for i in s1:
    if(i.isdigit()):
        l.append(i)
if(len(l)==0):
        print("no digit found")
else:
        sum=0

        for i in l:
            sum=sum+int(i)
        print("the sum of digits in the string is :",sum)
        print("the avg of digits in the string is :",sum/len(l))
        print("the max digits in the string is :",max(l))
        print("the min digits in the string is :",min(l))
