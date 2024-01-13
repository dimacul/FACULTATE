#a

def citire_numere(nume_fisier):
    lista_liste=[]
    f=open(nume_fisier)
    for linie in f.readlines():
        sublista = [int(x) for x in linie.split()]
        lista_liste.append(sublista)
    return lista_liste

lista_liste=citire_numere("numere.in")
print(lista_liste)

#b
def prelucrare_lista(lista_liste):
    for sublista in lista_liste:
        minim = min(sublista)
        i=0
        n=len(sublista)
        while i<n:
            if sublista[i] == minim:
                del sublista[i]
                n -= 1
            else:
                i+=1
    lung_min = len(lista_liste[0])
    for sublista in lista_liste:
        if len(sublista)<lung_min:
            lung_min=len(sublista)
    for i in range(len(lista_liste)):
        if len(lista_liste[i])>lung_min:
            lista_liste[i] = [lista_liste[i][j] for j in range(lung_min)]
    return lista_liste

lista_liste = prelucrare_lista(lista_liste)
print(lista_liste)
#c
for i in range(len(lista_liste)):
    for j in range(len(lista_liste[0])):
        print(lista_liste[i][j], end=" ")
    print()

#d
def cate_cifre_are(x):
    k=0
    while x>0:
        k+=1
        x = x//10
    return k
k=int(input("da-mi k: "))
lista_fin = set()
for i in range(len(lista_liste)):
    for j in range(len(lista_liste[0])):
        if cate_cifre_are(lista_liste[i][j]) == k:
            lista_fin.add(lista_liste[i][j])


with open("cifre.out", "w") as g:
    if lista_fin == set():
        g.write("imposibil")
    else:
        g.write(" ".join(sorted([str(x) for x in lista_fin], reverse = True)))
