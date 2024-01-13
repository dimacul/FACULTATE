import math
def citire_matrice(nume_fisier):

    f=open(nume_fisier)
    n=int(f.readline())
    rad=math.sqrt(n)
    rad = int(rad)
    a=[[int(f.readline()) for j in range(rad)] for i in range(rad ) ]
    return a

a=citire_matrice("matrice.in")
print(a)

#b
def prelucrare_matrice(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j:
                a[i][j] = a[i][j] - a[i][i]
        del a[i][i]
    return a
a=prelucrare_matrice(a)
print(a)

#c
for i in range(len(a)):
    for j in range(len(a)-1):
        print(a[i][j], end=" ")
    print()

#d
M=citire_matrice("matrice.in")
k=7 #int(input())
print(M)

def suma_cif(nr):
    suma=0
    while nr>0:
        suma+=nr%10
        nr//=10
    return suma
ls=set()
for i in range(len(M)):
    for j in range(len(M)):
        if suma_cif(M[i][j])== k:
            ls.add(M[i][j])

ls=sorted(ls)
for elem in ls:
    print(elem, end=" ")

