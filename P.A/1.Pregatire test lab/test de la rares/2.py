f=open("punctaje.in")
d={}
for linie in f.readlines():
    echipa_sau_strumf = linie.split(maxsplit=1)[0]
    if echipa_sau_strumf == "Echipa":
        echipa = linie.split(maxsplit=1)[1].strip("\n")
        d[echipa] = {}
    else:
        nume, puncte = linie.split(" : ")
        d[echipa][nume] = [int(elem) for elem in puncte.split()]
#print(d)
def cheie(tuplu):
    return (-tuplu[3], tuplu[0], tuplu[1])
def premianti(d, *scoruri, k):
    lista=[]
    for echipa in d.keys():
        for strumf in d[echipa].keys():
            ls=[]
            for punctaj in d[echipa][strumf]:
                for scor in scoruri:
                    if punctaj == scor:
                        ls.append(punctaj)
            if len(ls)>=k:
                suma=0
                for punctaj in ls:
                    suma+=punctaj
                media = suma/len(ls)
                lista.append((echipa, strumf, sorted(ls), round(media, 2) ))
    lista=sorted(lista, key=cheie)
    return lista
#print(premianti(d, 50, 25, 40, 60, 30, 45, k=3))

def stergere(d, nume_echipa, nume_membru):
    del d[nume_echipa][nume_membru]
    if len(d[nume_echipa])<2:
        nume_jucator = d[nume_echipa].keys()
        for elem in nume_jucator:
            nume = elem
        del d[nume_echipa]
        mesaj = "Am sters si jucatorul "+ nume +" din echipa "+ nume_echipa
        return mesaj
    else:
        return [elem for elem in d[nume_echipa].keys()]
print(stergere(d, 'Potiuni magice', 'Strumfita'))
print(d)
