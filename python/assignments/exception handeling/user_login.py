class error(Exception):
    pass

password="greentea"
for i in range(3):
    try:
        s=input("enter ur password :")
        if(s==password):
            print("login successful !")
            break
        elif(i==2):
            raise error
        else:
            print("wrong password !")
            print(f"you have {3-i-1} attempt left ")
        
    except:
        print("you have exceeded the attempts ")
        
