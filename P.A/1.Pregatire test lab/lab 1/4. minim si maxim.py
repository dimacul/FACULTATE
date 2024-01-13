n = int(input("da n"))
maxim = int(input("primul nr"))
minim = maxim
for i in range(1, n):
    nr = int(input())
    if nr < minim:
        minim = nr
    elif nr>maxim:
        maxim = nr
print(minim, maxim)
