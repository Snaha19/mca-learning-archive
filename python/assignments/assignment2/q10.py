#taking all input
age=int(input("enter your age :"))
health=input("enter ur health poor or excellent :")
sex=input("enter ur sex :")
loc=input("enter ur locality is it village or city")
pre=0
#checking age for coverage eligibity
if(age>=25 and age<=35):
    if(sex=="male" and health=="excellent" and loc=="city"):
         print("your coverage can be upto 2 lakh")
         print("your premium is 4 per thousands")
         cov=int(input("enter coverage u r expecting"))
         if(cov<=200000):
             pre=cov//1000*4
         else:
             print("expecting coverage is invalid")
             
         
            
    elif(sex=="female" and health=="excellent" and loc=="city"):
        print("your coverage can be upto 1 lakh ")
        print("your premium is 4 per thousands")
        cov=int(input("enter coverage u r expecting"))
        if(cov<=100000):
         pre=cov//1000*3
        else:
            print("expecting coverage is invalid")
             
    
            
    elif(sex=="male" and health=="poor" and loc=="village"):
        print("your coverage can be upto 10,000")
        cov=int(input("enter coverage u r expecting"))
        if(cov<=10000):
         pre=cov//1000*6
        else:
            print("expecting coverage is invalid")
             
    
    print("you can be insured")
    print("your premium will be :",pre)


                
else:
    print("person is not insured")
