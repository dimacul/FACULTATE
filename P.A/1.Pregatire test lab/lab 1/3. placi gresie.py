l1, l2 = input().split()
l1 = int(l1)
l2 = int(l2)
def cmmdc(x, y):
    while x!=y:
        if x>y:
            x-=y
        else:
            y-=x
    return x #y
lat_patrat = cmmdc(l1, l2)
nr_bucati = l1*l2/(lat_patrat*lat_patrat)
print(nr_bucati, lat_patrat)
