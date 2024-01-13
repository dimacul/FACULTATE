f=open("suma M.in")
nr_elem = int(f.readline())
vector = [int(elem) for elem in f.readline().split()]
M = int(f.readline())

matrice = [[0 for i in range(M+1)] for j in range(nr_elem+1)]
for linie in range( nr_elem+1):
    matrice[linie][0]=1
for i in range(1, nr_elem+1):
    for j in range(M):
        if matrice[i-1][j]==1:
            if j+vector[i]<=M:
                matrice[i][j+vector[i]] = 1
print(matrice)
