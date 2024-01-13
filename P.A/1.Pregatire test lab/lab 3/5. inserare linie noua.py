m=[[linie+col for col in range(3)]for linie in range(2)]
print(m)
m.insert(1, [0]*3)
print(m)
m=m[:2]+[[69 for i in range(3)]]+m[2:]
print(m)
