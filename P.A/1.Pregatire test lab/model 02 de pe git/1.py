f=open("text.in")
fr={}
nr_lit=0
for c in f.read():
    if c.isalpha():
        if ord(c)>=ord('A') and ord(c)<=ord('Z'):
            lit =chr( ord('a')+ord(c)-ord('A') )
        else:
            lit=c
        if lit in fr.keys():
            fr[lit]+=1
        else:
            fr[lit]=1
        nr_lit+=1
for c in fr.keys():
    fr[c]/=nr_lit

print(fr)
ls=[]
for c in fr.keys():
    ls.append([c, fr[c]])
print(ls)

def cheie(pereche):
    return (0-pereche[1], pereche[0])

ls=sorted(ls, key=cheie, )
print(ls)
for pereche in ls:
    print(pereche[0], ":", "{:.3f}".format(pereche[1]), sep=" ")

