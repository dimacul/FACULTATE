m=3; n=4
a = [[linie+col for col in range(n)]for linie in range(m)]
for linie in range(m):
    for col in range(n):
        print(a[linie][col], end=" ")
    print()
#b=[[linie+col for col in range(m)]for linie in range(n)]
#print(b)
#for linie in range(m):
  #  for col in range(n):

#b=[[a[j][i] for i in range(m)] for j in range(n)]
b=[[0 for col in range(m)] for linie in range(n)]
print(b)
for linie in range(m):
    for col in range(n):
        b[col][linie] = a[linie][col]

for linie in range(n):
    for col in range(m):
        print(b[linie][col], end=" ")
    print()
b=[[0 for col in range(m)] for linie in range(n)]
print(b)

b=[[a[linie][col] for linie in range (m)]for col in range(n)]
print(b)
