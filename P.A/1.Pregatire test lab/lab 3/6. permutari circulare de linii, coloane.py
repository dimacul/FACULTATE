m, n= 3, 4
a=[
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3]
]
k=2
for i in range(k%m):
    aux = a[m-1]
    for j in range(m-1, 0, -1):
        a[j]=a[j-1]
    a[0]=aux

print(a)

#SAU:
m, n= 3, 4
a=[
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3]
]
k=2
b=[
    [0]*4,
    [0]*4,
    [0]*4
]
print(b)
for linie in range(m):
    b[(linie + (k%m))%m]=a[linie]
print(b)
"""
def citire_matrice(a, m, n):
    a=[[int(elem) for elem in input().split()] for linie in range(m)]
    return a
a = citire_matrice(a, 2, 3)
print(a)
"""
#Permutarile circulare ale coloanelor:
m, n= 3, 4
a=[
    [0,1,1,1],
    [2,0,2,2],
    [3,3,0,3]
]
k=2
aux=[0]*m
for i in range(k%n):
    for j in range(m):
        aux[j]=a[j][n-1]
    for col in range(n-1, 0, -1):
        for j in range(m):
            a[j][col]=a[j][col-1]
    for j in range(m):
        a[j][0] =aux[j]

for linie in a:
    for col in linie:
        print(col, end=" ")
    print()

#sau cu matrice auxiliara
