def fact(n):
    if n==0 :
        return 1
    else:
        return n*fact(n-1)
    
def rev(n):
    r=0
    while(n>0):
     n1=n%10
     r=r*10+n1
     n=n//10
    return r