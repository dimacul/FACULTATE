#textul codificat “1v3a1c1a1n1t5a2 1m13a1r4e” se va decodifica “vaaacantaaaaa maaaaaaaaaaaaareeee”
#                                                                             maaaaaaaaaaaaareeee
s="1v3a1c1a1n1t5a2 1m13a1r4e"
t=""
i=0
while i<len(s):
    start=i
    if s[i].isnumeric()==True:
        nr=0
        nr_cifre=0
        while s[i].isnumeric()==True:
            i+=1
        nr_cifre=i-start
        for p in range(nr_cifre):
            nr=10**p*(ord(s[i-p-1])-ord('0'))+nr

        t=t+nr*s[i]
    else:
        i+=1
print(t)

#b) Scrieți un program care citește un text dat pe o linie și îl codifică
s="mare"
i=0
t=""
while i<len(s):

        contor=1
        while i+contor<len(s) and s[i+contor-1]==s[i+contor]:
            contor+=1
        t=t+chr(contor+48)+s[i]
        i+=contor

print(t)
