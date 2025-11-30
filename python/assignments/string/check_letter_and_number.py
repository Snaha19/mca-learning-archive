s=input("Enter a string: ")

alfa=False
number=False
for i in s:
    if(i.isalpha()):
        alfa=True
    if(i.isdigit()):
        number=True
    if alfa and number:
     break

if(alfa and number):
    print("The string contains both letters and numbers")
else:
    print("The string does not contain both letters and numbers")   