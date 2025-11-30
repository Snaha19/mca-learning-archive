s1=input("enter any string")
s2=input("enter any string")
s3=''
l=len(s1)
l2=len(s2)
m=min(l,l2)
for i in range(m):
    
    s3+=s1[i]+s2[l2-i-1]

print(s3)
if(l>l2):
  s3=s3+s1[len(s2):]
  print(s3)
else:
    s4=s2[:len(s1)-1]
    
    s3=s3+s4[::-1]
    print(s3)
