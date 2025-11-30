s=input("enter any string")
for i in s:
    if not i.isalnum():
        print("special found")
        break
else:
        print("not")