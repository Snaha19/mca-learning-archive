s=input("Enter a string: ")
word=s.split()
res=''
for i in word:
    res+=i[0].upper()+i[1:-1]+i[-1].upper()+' '
print(res) 