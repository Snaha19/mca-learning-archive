# If a five-digit number is input through the keyboard, write a program to print a new number by
# adding one to each of its digits. For example, if the number that is input is 12391 then the output
# should be displayed as 23402.


# input
num = int(input("Enter a 5-digit number: "))

# getting each  digits and adding 1
ones = (num % 10) + 1
tens = ((num // 10) % 10) + 1
hundreds = ((num // 100) % 10) + 1
thousands = ((num // 1000) % 10) + 1
ten_thousands = (num // 10000) + 1

# carry handling
if ten_thousands > 9:
    thousands += ten_thousands // 10
    ten_thousands %= 10

if thousands > 9:
    hundreds += thousands // 10
    thousands %= 10

if hundreds > 9:
      tens += hundreds // 10
    hundreds %= 10

if tens > 9:
    ones += tens // 10
    tens %= 10

# new number
new_num = ten_thousands * 10000 + thousands * 1000 + hundreds * 100 + tens * 10 + ones
print(new_num)



## output:
Enter a 5-digit number:  12391
23403








