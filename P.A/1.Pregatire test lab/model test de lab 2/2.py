#a
f=open("spiridusi.in")
d={}
for linie in f.readlines():
    nume_sp = linie.split(" : ")[0]
    despre_jucarie = linie.split(" : ")[1]
    cant = int(despre_jucarie.split()[-1])
    denumire = " ".join(despre_jucarie.split()[:-1])
    print(nume_sp, denumire, cant)
    if nume_sp not in d:
        d[nume_sp] = {denumire:cant}
    elif denumire in d[nume_sp]:
        d[nume_sp][denumire]+=cant
    else:
        d[nume_sp].update({denumire:cant})

print(d)
"""
d={"masina":1}
print(d["masina"])
print(d)"""
#b
ls=[]
def top_spiridusi(d, *nume_de_spiridusi, nr_minim):
    for spiridus in nume_de_spiridusi:
        multime=set()
        nr_tot=0
        for jucarie in d[spiridus].keys():
            if d[spiridus][jucarie]>=nr_minim:
                nr_tot+=d[spiridus][jucarie]
                multime.add(jucarie)
        if nr_tot>0:
            ls.append((spiridus, multime, nr_tot))
    return ls
ls=top_spiridusi(d,  "Spiridus Harnic", "Spiridus Poznas", "Spiridus Jucaus", nr_minim = 2)
print(ls)
#c
def adauga_bucati(d, nume_spiridus, nume_jucarie="", nr_bucati=1):

    nr_total = 0
    for jucarie in d[nume_spiridus].keys():
        nr_total+=d[nume_spiridus][jucarie]
    if nume_jucarie =="":
        for jucarie in d[nume_spiridus].keys():
            d[nume_spiridus][jucarie]+=nr_bucati
        nr_total = nr_total+ nr_bucati*len(d[nume_spiridus].keys())
    else:
        if nume_jucarie in d[nume_spiridus].keys():
            d[nume_spiridus][nume_jucarie]+=nr_bucati
        else:
            d[nume_spiridus].update({nume_jucarie:nr_bucati})
        nr_total += nr_bucati
    return nr_total


s = "Spiridus Jucaus"
j = "masinuta"
print(adauga_bucati(d, s, j))
