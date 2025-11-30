# taking len,breath as input
le=int(input("enter lenght"))
bre=int(input("enter breath"))

#finding area and perimeter of rectangle
area=le*bre
peri=2*(le+bre)

if(area>peri):
    print(f"the area of the rect. with lenght= {le} and breath={bre} is greater than its perimeter")
else:
    print(f"the area of the rect. with lenght= {le} and breath={bre} is not greater than its perimeter")
