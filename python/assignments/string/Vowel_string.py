s=input("enter any string")
set_vowels={'a','e','i','o','u'}
for i in s.lower():
    
    if(i in set_vowels):
        set_vowels.remove(i)
        if(set_vowels==set()):
           break

if set_vowels==set() :
    print("All vowels are present in the string")
else:

 print("All vowels are not present in the string")             