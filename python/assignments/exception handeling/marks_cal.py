class negetive(Exception):
    pass
class outofbound(Exception):
    pass
class all_marks(Exception):
    pass
total=0
for i in range(4):
    try:
            mark=int(input("enter ur sem marks if not enter 0:"))
            if mark<0:
                raise negetive
                
            elif mark<0 or mark>100:
                raise outofbound
                
            elif mark==0:
                raise all_marks
                
            total+=mark
            

    except negetive:
         print("marks can't be in negetive ")
         break
         
    except outofbound:
         print("marks can't be in greater than 100 ")
         break
         
    except all_marks:
        print("u have to enter all marks")
        break
        
avg=total/4
print(avg)  
