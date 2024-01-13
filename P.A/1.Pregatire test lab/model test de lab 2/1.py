#a
def citire_liste(nume_fisier):

    f=open(nume_fisier)
    n = int(f.readline())
    ls = [[] for i in range(n)]
    for linie in f.readlines():
        x, k = linie.split()
        x=int(x)
        k=int(k)
        ls[k].append(x)
    return ls
L=citire_liste("liste.in")
print(L)
cL = L
#b /c
def prelucrare_liste(L, x):
    n= len(L)
    i=0
    while i<n:
        if x in L[i]:
            aparitii = L[i].count(x)
            for k in range(aparitii):
                L[i].remove(x)
        if len(L[i])<2:
            L=L[:i] + L[i+1:]
            n-=1
        else:
            i+=1
    return L

L=prelucrare_liste(L,0)

for linie in L:
    for elem in linie:
        print(elem, end=" ")
    print()

#d
#k =int(input("dati k:"))
k=4
L=cL

ls=[]
def nr_divizori(x):
    nr=2 #x e div al lui x, 1 e div al lui x
    for d in range(2, x//2+1):
        if x%d==0:
            nr+=1
    return nr

for linie in L:
    for elem in linie:
        if nr_divizori(elem) == k and elem not in ls:
            ls.append(elem)
ls = sorted(ls, reverse=True)

with open("date.out", "w") as g:
    if len(ls)==0:
        g.write("Imposibil")
    else:
        for elem in ls:
            g.write(str(elem))
            g.write('\n')
