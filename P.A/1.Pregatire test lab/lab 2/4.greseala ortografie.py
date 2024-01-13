#a
propozitie = "caracteger nu sunt ggerle" #input()
s ="ger" # input()
t ="re" # input()

indexul = 0
while indexul!=-1:
    indexul = propozitie.find(s, indexul)
    if indexul!=-1:
        propozitie = propozitie[:indexul]+t+propozitie[indexul+len(s):]
        indexul+=1
print(propozitie)

#b citesc un p si corectez cel mult p greseli
propozitie = "caracteger nu sunt ggerle"
p=1
greseli =0
indexul = 0
while indexul!=-1 and greseli<=p:
    indexul = propozitie.find(s, indexul)
    if indexul!=-1:
        propozitie = propozitie[:indexul]+t+propozitie[indexul+len(s):]
        indexul+=1
        greseli+=1
if greseli>p:
    print(f"Textul contine prea multe greseli. Doar {p} au fost corectate")
print(propozitie)
