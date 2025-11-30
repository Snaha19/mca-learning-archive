s1=input("enter any string 1 :")
s2=input("enter any string 2 :")
s3=""
m=min(len(s1),len(s2))
for i in range(m):
    s3=s3+s1[i]+s2[-(i+1)]

if(len(s1)>len(s2)):
    s3=s3+s1[m:]
else:
    
    s3=s3+s2[m:][::-1]
print("the interleaved merged string is :",s3)