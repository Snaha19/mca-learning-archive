# digit sum recursion with loop
def digit(n):
    temp=0
    digit_sum=0
    while n>0:
        temp=n%10
        digit_sum=digit_sum+temp
        n=n//10
    return digit_sum
while True:
    num=int(input("enter number (enter 0 or any neg val to escape the loop :"))
    if num<=0:
        break

    a=digit(num)
    if(a>9):
        a=digit(a)

    if(a<=9):
            print(a)
    
        


    
