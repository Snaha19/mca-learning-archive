s = input("Enter string: ")

while "abc" in s:
    s = s.replace("abc","")

if s == "":
    print("String can become empty")
else:
    print("String cannot become empty")
