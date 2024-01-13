def citire_din_fisier(fisier):
    f=open(fisier)
    vector = [int(x) for x in f.read().split()]
    return vector

def afisare_vector(fisier, vector):
    with open(fisier, "a") as g:
        g.write(" ".join([str(x) for x in vector]))

def divide_inversiuni(vector, p, u):
    if p == u:
        return 0
    m=(p+u)//2
    inv_stg = divide_inversiuni(vector, p, m)
    inv_dr = divide_inversiuni(vector, m+1, u)
    return inv_stg + inv_dr + interclaseaza(vector, p, m, u)


def interclaseaza(a, p, m, u):
    global ls
    b = [None]*(u-p+1)
    nr = 0
    i=p
    j=m+1
    k=0
    while i<=m and j<=u:
        if a[i]<=a[j]:
            b[k] = a[i]
            i+=1
        else:
            b[k] = a[j]
            if a[i]>2*a[j]:
                nr += m - i + 1
                ls.append([(a[i], a[j]) for i in range (p, m+1)])
            else:
                r = i
                while a[r]<=2*a[j] and r+1<=m:
                    r+=1
                if r<=m:
                    nr += m - r + 1
                    ls.append([(a[x], a[j]) for x in range(r, m+1)])
            j+=1
        k+=1

    while i<=m:
        b[k]= a[i]
        """if a[i]>2*a[j-1]: #evident, din moment ce jumatatea dreapta a fost adaugata complet in sirul de interclasare
            nr += u - m
            ls.append([(a[i], a[j]) for j in range(u, m, -1)])"""
        i+=1
        k+=1

    while j<=u:
        b[k]=a[j]
        j+=1
        k+=1

    for i in range(p, u+1):
        a[i] = b[i-p]

    return nr

ls=[]

vector = citire_din_fisier("interclasare.in")
afisare_vector("pb4.out", vector)


with open("pb4.out", "a") as g:
    g.write("\n")
    g.write(str(divide_inversiuni(vector, 0,  len(vector)-1)))
    g.write("\n")
afisare_vector("pb4.out", vector)
print(ls)
