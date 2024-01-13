s="alaturare"
lit = s[0]
i=1

s=s[1:len(s)]
n = len(s)
while i< n:
    if s[i] == lit:
        s =s[:i]+s[i+1:]
        n-=1
    else:
        i+=1
print(s)


#SAU:
s='alaturare'
lit=s[0]
s=list(s)
for elem in s:
    if elem == lit:
        s.pop(s.index(elem))
print(s)
