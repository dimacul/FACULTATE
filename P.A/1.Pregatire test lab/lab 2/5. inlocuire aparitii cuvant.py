#a
prop = "aici voi inlocui cuv aici aici"
rau = "aici"
bun = "acolo"

poz=0
while poz!=-1:
    poz = prop.find(rau)
    if poz!=-1:
        if (poz==0 or prop[poz-1] ==" ") and (poz+len(rau)==len(prop) or prop[poz+len(rau)]==" "):
            prop = prop[:poz] + bun + prop[poz+len(rau):]
print(prop)

#b
prop = "aici... voi inlocui cuv aici, aici"
rau = "aici"
bun = "acolo"

poz=0
while poz!=-1:
    poz = prop.find(rau)
    if poz!=-1:
        if (poz==0 or prop[poz-1].isalpha()==False) and (poz+len(rau)==len(prop) or prop[poz+len(rau)].isalpha()==False):
            prop = prop[:poz] + bun + prop[poz+len(rau):]
print(prop)
