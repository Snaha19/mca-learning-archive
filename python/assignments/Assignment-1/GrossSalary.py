# Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
# salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross
# salary.


# inputing basic salary

basic=int(input("enter ur salary :"))

# calculating DA
da=basic*40/100

#calculating rent
rent=basic*20/100

#calculating gross salary
gross=basic+da+rent

#printing gross salary
print(f"gross salary = {gross} rupeess")


## output:
enter ur salary : 45000
gross salary = 72000.0 rupeess
