s = input("Enter string: ")
k = int(input("Enter rotation: "))

k %= len(s)
rotated = s[k:] + s[:k]

print(rotated)
