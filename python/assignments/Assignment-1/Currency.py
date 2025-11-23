# A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is
# input through the keyboard in hundreds, find the total number of currency notes of each
# denomination the cashier will have to give to the withdrawer.

#inputing withdrwan amount from usd

withdraw=int(input("enter amount u want to withdraw"))

#currency notes denomination
d1=10
d2=50
d3=100

#calculating the no of currency

w1=withdraw//d3 # 100 rup note

w2=(withdraw%d3)//d2

w3=(withdraw%d2)//d1

print(" no of 100 rup note will be : ",w1)
print(" no of 50 is : ",w2)
print(" no of 10 is : ",w3)

## output:
enter amount u want to withdraw 450
 no of 100 rup note will be :  4
 no of 50 is :  1
 no of 10 is :  0







