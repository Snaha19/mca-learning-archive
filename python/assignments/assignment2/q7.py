#taking age input of ram ,shyam,ajay
ram=int(input("enter the age of ram :"))
shyam=int(input("enter the age of shayam :"))
ajay=int(input("enter the age of ajay :"))

#checking who is youngest
if(ram<shyam):
    if(ram<ajay):
        print("ram is the youngest one")
    else:
        print("ajay is the youngest one")
else:
    if(shyam<ajay):
        print("shyam is the yongest one")
    else:
        print("ajay is the youngest one")
