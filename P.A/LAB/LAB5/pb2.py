def cif_max(n):
    maxi=0
    while n>0:
        u=n%10
        if u>maxi:
            maxi=u
        n//=10
    return maxi

def alipire(*nr):
    numar=0
    for x in nr:
        c=cif_max(x)
        numar=numar*10+c

    return numar
print(alipire(4251, 73, 8, 133))

#b)
def baza2(a, b, c):
    if alipire(a, b, c)==111:
        return "DA"
    return "NU"

print(baza2(101, 103, 101))
