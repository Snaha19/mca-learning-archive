words = []
word = ''
for char in s:
    if char != ' ':
        word += char
    else:
        if word != '':
            words.append(word)
            word = ''
# Append last word if there is one
if word != '':
    words.append(word)

print("After manual split:", words)

separator = '-' 
joined_string = ''
for i in range(len(words)):
    joined_string += words[i]
    if i != len(words) - 1:
        joined_string += separator

print("After manual join:", joined_string)