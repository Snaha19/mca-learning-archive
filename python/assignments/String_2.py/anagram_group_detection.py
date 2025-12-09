l=["eat","tea","tan","ate","nat","bat"]
d={}
for i in l:
        wrd=''.join(sorted(i))
        if(wrd in d):
                d[wrd].append(i)
        else:
                d[wrd]=[i]
print(d)
print(list(d.values()))