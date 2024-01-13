n = 812383
cn =n
nr_cif = 0

while n>0:
    n//=10
    nr_cif+=1
copie_nr_cif = nr_cif
n = cn
#   8 1 2 3 8 3
#       <-
#maximul:
ok = 0
while ok ==0:
    p=0
    ok=1
    while p<nr_cif-1:

        x= n%(10**(p+1))//(10**p)
        y= n%(10**(p+2))//(10**(p+1))
        if  x>y :
            n = n//(10**(p+2))*(10**(p+2)) + x*(10**(p+1)) + y*(10**p) + n%(10**p)
            ok=0
        p+=1
    nr_cif-=1

print(n)
n=cn
#MINIMUL: #SE MAI PUTEA SI RASTURNAND MAXIMUL
nr_cif = copie_nr_cif
ok = 0
while ok ==0:
    p=0
    ok=1
    while p<nr_cif-1:

        x= n%(10**(p+1))//(10**p)
        y= n%(10**(p+2))//(10**(p+1))
        if  x<y :
            n = n//(10**(p+2))*(10**(p+2)) + x*(10**(p+1)) + y*(10**p) + n%(10**p)
            ok=0
        p+=1
    nr_cif-=1

print(n)
