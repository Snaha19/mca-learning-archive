class bad(Exception):
    pass
s=(input("enter any string :"))
try:
    if isinstance(s,str):
        raise bad
    res=int(s)
    print(res)
except bad:
    print(' string can not be typecast into int !!!')

    
    