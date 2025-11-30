words_list = ['apple', 'orange', 'banana', 'grape', 'pineapple']
s = input("Enter a string to match: ")

matches = []
for word in words_list:
    if s in word:   # check if input is part of word
        matches.append(word)

print("Close matches:", matches)
