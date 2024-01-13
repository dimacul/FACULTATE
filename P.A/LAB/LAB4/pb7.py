f=open("elevi.in")
d={}
for linie in f:
    cnp, nume, prenume, note=linie.split(maxsplit=3)
    cnp=int(cnp)
    note=[int(x) for x in note.split()]
    d[cnp]={"nume":nume, "prenume":prenume, "note":note}

f.close()
#b)
#functie - param: cnp, d -> creste cu1 prima nota a elevului cnp
#return -> nota dupa modif, none
def modificare_nota1(d, cnp):
    if cnp in d:
        d[cnp]['note'][0]+=1
        return d[cnp]['note'][0]
    return None

print(modificare_nota1(d, 2501910000034))
print(modificare_nota1(d, 2501810000034))

#c) f - param:cnp, lista note, d ->adauga lista note la elevul cu acest cnp
#-return lista note dupa modif sau NONE
#apel, cnp tasattura si l_note=[10, 8]

def modificare_lista_note(cnp, l_note, d):
    if cnp in d:
        for x in l_note:
            d[cnp]["note"].append(x)
        return d[cnp]["note"]
    return None
cnp=2501910000034
print(d[cnp]["note"])
l_note=[10,8]
print(modificare_lista_note(cnp, l_note, d))

#d)fucntie: param: cnp, d ->sterge info despre elev cu cnp
def stergere_elev(cnp, d):
    if cnp in d:
        del d[cnp]
print(d)
cnp=2501910000034
stergere_elev(cnp, d)
print(d)

#e)lista de liste ord descresc dupa medie
def medie(ls):
    sum=0
    for x in ls:
        sum+=x
    medie=sum/len(ls)
    return medie
def cheie(l):
    return -medie(l[2]), l[0]

d[5040726450018]={"nume":"Dima", "prenume":"Cristian", "note":[9, 10, 8, 8, 8]}
lista=[]
for cnp in d:
    l=[d[cnp]['nume'], d[cnp]['prenume'], d[cnp]['note']]
    lista.append(l)
print(lista)

print(sorted(lista, key=cheie))

#f) functie- primeste d-> adauga cod aleator

def genereaza_coduri(d):
    import random
    import string
    for cnp in d:
        litere=random.choices(string.ascii_letters, k=3)
        litere="".join(litere)
        nr=random.randint(100, 999)
        cod=litere+str(nr)
        d[cnp]['cod']=cod

genereaza_coduri(d)
print(d)



