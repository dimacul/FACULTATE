def prelucr_prima_lit(cuv):
    if ord(cuv[0])>=ord("a") and ord(cuv[0])<=ord("z"):
        dif=ord(cuv[0])-ord("a")
        pl=chr(ord("A")+dif)
    else:
        if ord(cuv[0])>=ord("A") and ord(cuv[0])<=ord("Z"):
            dif = ord(cuv[0]) - ord("A")
            pl = chr(ord("a") + dif)
    return pl+cuv[1:]

def cautare_cuvant(cuv, fis_out, *fis_in):
    cuv2=prelucr_prima_lit(cuv)
    for fisier in fis_in:
        l=[]
        f=open(fisier)
        linii=f.readlines()
        for k in range(len(linii)):
            if cuv in linii[k]:
                l.append(k+1)
            else:
                if cuv2 in linii[k]:
                    l.append(k+1)
        with open("pb3.out", "a") as g:
            g.write(fisier+" ")
            for i in range(len(l)):
                g.write(str(l[i])+" ")
            g.write("\n")

cautare_cuvant("floare", "pb3.out", "eminescu.txt", "paunescu.txt")

