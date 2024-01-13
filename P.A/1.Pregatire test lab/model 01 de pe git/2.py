def modifica_prefix(x, y, prop):
    prop = prop.split()
    prop1=[]
    nr=0
    for cuv in prop:
        if cuv[:len(x)] == x:
            nr+=1
            prop1.append( y + cuv[len(x):] )
        else:
            prop1.append(cuv)
    prop1 = " ".join(prop1)
    return (prop1, nr)
print(modifica_prefix("ma", "ta",  "mama si mam mamama"))

def poz_max(ls):
    max=ls[0]
    indici=[]
    for elem in ls:
        if max<elem:
            max=elem
    if max>0:
        for i in range(len(ls)):
            if ls[i] == max:
                indici.append(i+1)
    return indici

#c
f=open("propozitii.in")
a="cea"
b="ca"
lista_nr_modificari = []
with open("propozitii_modificate.out", "w") as g:
    for linie in f.readlines():
        g.write(modifica_prefix(a,b, linie)[0])
        g.write("\n")
        lista_nr_modificari.append(modifica_prefix(a,b, linie)[1])
if poz_max(lista_nr_modificari)!=[]:
    ind = poz_max(lista_nr_modificari)
    for elem in ind:
        print(elem, end=" ")
else:
    print("Nu s-au facut modificari")
