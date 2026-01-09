class bad(Exception):
    pass

age=int(input("enter ur age :"))
try:
    if age<18:
        raise bad
    print("you can vote ")

except:
    print("you are not elligible for voting")