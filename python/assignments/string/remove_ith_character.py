s=input("enter a string: ")
i=int(input("enter the index of character to be removed: ") )
new_s=""
new_s=s[:i]+s[i+1:]
print("string after removing the character at index ",i," is: ",new_s)

 