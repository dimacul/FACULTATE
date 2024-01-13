#lista de numere ordonata crescator si un numar x
#se returneaza nr de aparitii ale lui x in vector
v=[1,1, 2,2,2,2,7, 12]
n=8
x=1

def prima_pozitie(x, v, p, u):

        mijloc=(p+u)//2
        if (v[mijloc]==x and mijloc==0) or (v[mijloc]==x and v[mijloc]!=v[mijloc-1]):
            return mijloc
        elif x<=v[mijloc]:
            return prima_pozitie(x, v, p, mijloc - 1)
        return prima_pozitie(x, v, mijloc +1, u)

print(prima_pozitie(x, v, 0, n-1))

def ultima_pozitie(x, v, p, u):

        mijloc=(p+u)//2
        if (v[mijloc]==x and mijloc==n-1) or (v[mijloc]==x and v[mijloc]!=v[mijloc+1]):
            return mijloc
        elif x<v[mijloc]:
            return ultima_pozitie(x, v, p, mijloc - 1)
        return ultima_pozitie(x, v, mijloc +1, u)

print(ultima_pozitie(x, v, 0, n-1))

#1,1, 2,2,2,2,7, 12

print(f"Nr. de aparitii al elementului {x} este: {ultima_pozitie(x, v, 0, n-1) - prima_pozitie(x, v, 0, n-1) +1}")
