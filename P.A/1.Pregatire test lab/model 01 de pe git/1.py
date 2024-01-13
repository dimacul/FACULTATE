def citire_matrice(nume_fisier):
    f=open(nume_fisier)
    m=[]
    m.append([int(elem) for elem in f.readline().split()])
    lung = len(m[0])
    for linie in f.readlines():
        if len(linie.split())!=lung:
            return None
        else:
            m.append([int(elem) for elem in linie.split()])
    return m

m=citire_matrice("matrice.in")
print(m)
def prima_ultima(x):
    u=x%10
    while x>9:
        x //=10
    if u == x:
        return 1
    return 0
#b
def multimi(m, *indici):

    mult_poz=set()
    i=0
    for indice in indici:
        mult_neg = set()
        for elem in m[indice]:
            if elem<0:
                mult_neg.add(elem)
            else:
                if prima_ultima(elem)==1:
                    if elem not in mult_poz:
                        mult_poz.add(elem)
        if i==0:
            mult_neg_intersect = mult_neg
        else:
            mult_neg_intersect = mult_neg_intersect.intersection(mult_neg)
        i+=1
    return [mult_neg_intersect, mult_poz]

print(multimi(m, 0, 1, 2, 3))

#-----------------------------------
#c
m=citire_matrice("matrice.in")
poz = sorted(multimi(m, len(m)-1, len(m)-2, len(m)-3)[1])
for elem in poz:
    print(elem, end=" ")
print()
neg = multimi(m, 0, len(m)-1)[0]
print(len(neg))
