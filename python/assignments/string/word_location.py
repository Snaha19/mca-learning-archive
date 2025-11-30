s = input("Enter a string: ").split()
w = input("Enter word to find: ")

for i in range(len(s)):
    if s[i] == w:
        print("Found at position:", i)
        break
else:
    print("Not found")
