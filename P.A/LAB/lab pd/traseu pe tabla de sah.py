f=open("date.in")
matrice=[]
t=[]
m, n = f.readline().split()
m=int(m)
n=int(n)

for linie in f:
    matrice.append([int(elem) for elem in linie.split()])
print(matrice)
t=[[0 for i in range(n)]for j in range(m)]
t[0][0] = matrice[0][0]
for i in range(1, n):
    t[i][0] = t[i-1][0] +matrice[i][0]
for i in range(1, m):
    t[0][i] = t[0][i-1] + matrice[0][i]

for i in range(1,n):
    for j in range(1, m):
        t[i][j]=matrice[i][j]+max(t[i-1][j], t[i][j-1])
g=open("date.out", "w")
print(t)
string = str(t[n-1][m-1])
g.write(string)
g.write("\n")
i=n-1
j=n-1
while i>0 and j>0:
    i_str = str(i)
    j_str = str(j)
    g.write(i_str)
    g.write(" ")
    g.write(j_str)
    if t[i][j-1]>t[j][i-1]:
        j=j-1
    else:
        i=i-1
if j==0:
    while i>=0:
        i_str = str(i+1)
        g.write(i_str)
        g.write(" 1")
        g.write("\n")
        i-=1
else:
    while j>=0:



