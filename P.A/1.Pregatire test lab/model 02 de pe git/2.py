
def citire_matrice(n):
    a=[]
    f=open("date.in")
    for i in range(n):
        linie = [int(elem) for elem in f.readline().split()]
        a.append(linie)
    return a
a=citire_matrice(5)
print(a)
#b
def functie(m, ch, x=0, y=0):
    if ch == 'c':
        for linie in range(len(m)):
            m[linie][x]+=m[linie][y]
            m[linie][y]=m[linie][x]-m[linie][y]
            m[linie][x]=m[linie][x]-m[linie][y]
    else: #ch='d'
        for i in range(len(m)):
            aux=m[i][i]
            m[i][i] = m[i][len(m)-i-1]
            m[i][len(m)-i-1]=aux
    return m

#a=functie(a, 'd')
print(a)

#c
n=5
for col in range(n//2):
    a = functie(a, 'c', col, len(a)-1-col)
a=functie(a, "d")
for linie in range(n):
    if linie%2 == 0:
        for col in range(n):
            print(a[linie][col], end=" ")
    else:
        for col in range(n-1, -1, -1):
            print(a[linie][col], end=" ")
