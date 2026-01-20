import re
s="siliguri  institute 1920 2024 of technology mca 1st semester 2025 odd"
#1
match=re.search("institute",s)
print(match)
#2
match=re.findall("[0-9]",s)
print(match)
#3
match=re.search("[0-9]{1}",s)
print(match)

#4
#match=re.findall("202[4-5]",s)
match=re.findall("[0-9]{2,4}",s)
print(match)
#5
match=re.findall("2024|2025",s)
print(match)