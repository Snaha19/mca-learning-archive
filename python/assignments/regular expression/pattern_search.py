import re
str1="this is first far line of fat code"
b="my phone number 45975154545"
c="my dob is 19/05/2003"
d="mca baca mcamca mba bacabba mcaabcbbb"
c="my email ide sna@gmail.com"



# match=re.findall("f",str1)
# print(match)
# output :['f', 'f', 'f']

# match=re.search("fi",str1)
# print(match)
# # output :<re.Match object; span=(8, 10), match='fi'>

# match=re.search("45",b)
# print(match)


#metacharacter
# match=re.findall("[b-f]",str1)
# print(match)
# ['f', 'e', 'f', 'f', 'c', 'd', 'e']

# match=re.search("[b-f]",str1)
# print(match)
# <re.Match object; span=(8, 9), match='f'>

# match=re.search(".",str1)
# print(match)

# match=re.findall(".",str1)
# print(match)
match=re.search("\.",c)
print(match)

match=re.search("^m",c)
print(match)

match=re.search("m$",c)
print(match)

match=re.search("b{2}",d)
print(match)
# output:<re.Match object; span=(24, 26), match='bb'>

match=re.findall("b{2,4}",d)
print(match)
# output :['bb', 'bbb']

match=re.findall("b+",d)
print(match)
# output:['b', 'b', 'b', 'bb', 'b', 'bbb']
match=re.findall("fat|farr",str1)
print(match)

match=re.findall("[0-9]+",str1)
print(match)

match=re.findall("[0-9]?",str1)
print(match)

s="9745787612"
match=re.findall("[1-9]{10}",s)
print(match)

# re.findall(pattern,string)
# re.search()