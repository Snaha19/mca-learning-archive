#taking no of days a mem is late as input
day=int(input("enter no of days which is late "))
#finding fine
if(day<=5):
    f=0.50*day
    print("your fine is",f)
elif(day<=10):
    f=0.50*5+(day-5)*1
    print("your fine is",f)
elif(day<=30):
    f=0.50*5+1*5+(day-10)*5
    print("your fine is",f)
else:
    print("your membership is cancelled")

