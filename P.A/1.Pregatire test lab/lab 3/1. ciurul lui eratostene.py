n = int(input("dati n"))
ls=[1 for i in range( n+1)]
ls[1]=0
ls[0]=0
for i in range(1, n+1):
    if ls[i]==1:
        for j in range(2, n//i + 1):
            ls[i*j]=0
print([indice for indice in range(n+1) if ls[indice]==1])
