f=open("autori.in")
m,n = f.readline().split()
m=int(m)
n=int(n)
d={}
for i in range(m):
    linie=f.readline().split(maxsplit=1)
    cod=int(linie[0])
    nume = linie[1].strip("\n")
    d[cod]=[nume]
for i in range(n):
    linie = f.readline().split(maxsplit=4)
    cod = int(linie[0])
    cod_c = int(linie[1])
    an = int(linie[2])
    nr_pg = int(linie[3])
    denumire = linie[4].strip("\n")
    d[cod].append([cod_c, an, nr_pg, denumire])

print(d)

#b
def sterge_carte(d, cod_c):
    gasit = 0
    numele = None
    for cod_autor in d.keys():
        for carti in d[cod_autor][1:]:
            if carti[0]==cod_c:
                gasit =1
                numele = d[cod_autor][0]
                del d[cod_autor][d[cod_autor].index(carti)]
    return numele
cod_c = 333
nume = sterge_carte(d, cod_c)
if nume == None:
    print("Nu exista")
else:
    print(f"Cartea scrisa de {nume}")
print(d)

def cheie(ls):
    return (ls[1], -ls[2], ls[3])
#c
cod_autor = 11
def carti_autor(d, cod_autor):
    if cod_autor not in d.keys():
        return []
    else:
        ls = d[cod_autor][1:]
        ls = sorted(ls, key=cheie)
        return [d[cod_autor][0], ls]
lista = carti_autor(d, cod_autor)
if lista ==[]:
    print("cod incorect")
else:
    print(lista[0])
    for carte in lista[1]:
        print(carte[3], carte[1], carte[2], sep=" ")

