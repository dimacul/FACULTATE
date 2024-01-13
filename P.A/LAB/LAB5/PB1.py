#a)
"""
def citire_lista():
    n=int(input("dati n"))
    l=[]
    for i in range(n):
        el=int(input())
        l.append(el)
    return l
citire_lista()
"""
#SAU

def cit_lista_sgline():
    n=int(input("dati n"))
    l=input()
    l=[int(x) for x in l.split()]
    return l[:n]


#b)
def pozitie(s, x, i=0, j='a'):
    if j=='a':
        j=len(s)

    for index in range(i, j):
        if s[index]>x:
            return index
    return -1

l=cit_lista_sgline()
ok=1
for k in range(0, len(l)-1):
    if pozitie(l, l[k], i=k, j=k+2)!=-1 or l[k]==l[k+1]: #verific daca l[k] e mai mare strict decat l[k+1]
        ok=0
        break
if ok==1:
    print("DA")
else:
    print("nu")


