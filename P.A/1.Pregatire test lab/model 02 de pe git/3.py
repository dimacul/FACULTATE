f=open("legaturi.in")
d={}
for linie in f.readlines():
    x, y, cul, leg = linie.split(maxsplit=3)
    x = x.strip("[")
    x = x.strip(']')
    abscisa =int(x.split(',')[0])
    ordonata = int(x.split(',')[1])
    x = (abscisa, ordonata)

    y = y.strip("[")
    y = y.strip(']')
    abscisa = int(y.split(',')[0])
    ordonata = int(y.split(',')[1])

    y = (abscisa, ordonata)
    leg = leg.strip('\n')
    d[leg]={}
    d[leg]['x']=x
    d[leg]['y']=y
    d[leg]['cul']=cul

print(d)

#b
def insereaza_leg(d, capat1, capat2, cul, leg):
    for cheie in d.keys():
        if (d[cheie]['x']==capat1 and d[cheie]['y']==capat2) or (d[cheie]['y']==capat2 and d[cheie]['x']==capat1):
            return False
    d[leg]={}
    d[leg]['x']=capat1
    d[leg]['y']=capat2
    d[leg]['cul']=cul
    return True

insereaza_leg(d, (1,3), (2,7), "negru", "legatura noua")
insereaza_leg(d, (3,8),(1,2), "mov", "legatura perversa")
for leg in d.keys():
    print(list(d[leg]['x']), list(d[leg]['y']), d[leg]['cul'], leg, sep=" ")


def vecini(d, *puncte):
    vecinii = {}
    for punct in puncte:
        ok=1
        for leg in d.keys():

            if d[leg]['x']==punct:
                if punct in vecinii.keys():
                    vecinii[punct].add(d[leg]['y'])
                else:
                    vecinii[punct] = {d[leg]['y']}
            else:
                if d[leg]['y'] == punct:
                    if punct in vecinii.keys():
                        vecinii[punct].add(d[leg]['x'])
                    else:
                        vecinii[punct] = {d[leg]['x']}
    print(vecinii)
    k=0
    for punct in vecinii.keys():
        if k==0:
            intersectie = vecinii[punct]
            k=1
        else:
            intersectie = intersectie.intersection(vecinii[punct])
    intersectie = list(intersectie)

    def cheie(tuplu):
        return -tuplu[1]
    return(sorted(intersectie, key=cheie))

print(vecini(d, (2,7), (1,2)))
