import random
target=input("enter the target string")
char='abcdefghijklmnopqrstuvwxyz'
c=0
generated=''
while target!=generated:
    generated=''
    for i in range(len(target)):
        generated+=random.choice(char)
    c+=1
print("Matched after", c, "attempts")
