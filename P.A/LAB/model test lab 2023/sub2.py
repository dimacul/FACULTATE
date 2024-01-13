#citire structura din fisier:

f = open("cinema.in")
d={}
for linie in f.readlines():
    aux = [chestie for chestie in linie.split(" % ")]

    cinema_nr = aux[0]

    film = aux[1]
    ore = set(aux[2].split())
    dicti={}
    dicti[film]=ore
    if cinema_nr not in d:
        d[cinema_nr] = dicti
    else:
        #d[cinema_nr] e deja in d -> poate aparea film nou sau ora noua pt un film existent
        if film not in d[cinema_nr]:
            d[cinema_nr][film]=ore
        else: #filmul e, dar ii updatez orele
            d[cinema_nr][film].update(ore)
for cinema in d:
    print(cinema, ":", d[cinema])

def sterge_ore(d, cinema, film, ore):
    for ora in ore:
        set_ora = set()
        set_ora.add(ora)
        d[cinema][film] = d[cinema][film] - set_ora
        ls=[]
    for filmulet in d[cinema]:
        if d[cinema][filmulet] != set():
            ls.append(filmulet)
            ls.append(d[cinema][filmulet])
    return ls
c='Cinema 1'
f='Minionii 2'
o=['12:30']

#citire o:
#o=[elem for elem in input("dati ore").split()]


print(sterge_ore(d, c, f, o))
print()
for cinema in d:
    print(cinema, ":", d[cinema])
def cheie(tuplu):
    return tuplu[0], -len(tuplu[2])
def cinema_film(d, *nume_cinematografe, ora_min, ora_max):
    ls=[]
    for cinema in nume_cinematografe:
        for film in d[cinema]:
            ls_ore = []
            for ora in d[cinema][film]:
                if ora>ora_min and ora<ora_max:
                    ls_ore.append(ora)
            if ls_ore !=[]:
                ls.append((film, cinema, sorted(ls_ore)))
    return sorted(ls, key = cheie)
print()
print(cinema_film(d, 'Cinema 1', 'Cinema 2', ora_min='14:00', ora_max='22:00'))
