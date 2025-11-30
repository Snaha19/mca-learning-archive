# Write a program to print all the even-length words in a string.

# Example:
# Input: "this is cool"
# Output:
# this
# is
# cool


s=input("Enter a string: ")
words = s.split()
for word in words:
    if len(word) % 2 == 0:
        print(word) 
    