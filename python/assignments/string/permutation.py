from itertools import permutations

s = input("Enter a string: ")

for p in permutations(s):
    print("".join(p))
