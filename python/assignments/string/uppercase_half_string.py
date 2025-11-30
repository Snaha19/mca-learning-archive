s=input("Enter a string: ")
mid =len(s)//2
s1=''
for i in range(mid):
    s1+=s[i].upper()
s1=s1+s[mid:]
print("Uppercase first half string is:",s1)