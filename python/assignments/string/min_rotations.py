s = input("Enter string: ")
original = s
count = 0

while True:
    s = s[1:] + s[0]  # left rotation by 1
    count += 1
    if s == original:
        break

print("Minimum rotations to get original string:", count)
