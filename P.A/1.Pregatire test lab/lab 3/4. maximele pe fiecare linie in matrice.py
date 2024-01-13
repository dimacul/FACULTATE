m=2; n=3
a=[[col+linie for col in range(n)] for linie in range(m)]
for linie in range(m):
    for coloana in range(n):
        print(a[linie][coloana], end=" ")
    print()

maxime=[max(linie) for linie in a]
print(maxime)
print([f"Maximul pe coloana {i} este {maxime[i]}" for i in range(m)])

