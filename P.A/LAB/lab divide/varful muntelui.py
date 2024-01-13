

def cautare_binara(x, v, p, u):
    if p>u:
        return (False, u)
    else:
        mijloc = (p+u)//2
        if x==v[mijloc]:
            return (True, mijloc)
        elif x<v[mijloc]:
            return cautare_binara(x, v, p, mijloc - 1)
        else:
            return cautare_binara(x, v, mijloc +1, u)
n=6 #int(input("n="))
v=[1, 3, 4, 5, 9, 12] #[int(x) for x in input().split()]
x=5
print(cautare_binara(x, v, 0, n-1))



#varful muntelui:
def varful_muntelui(mijloc, v, p, u):
        mijloc = (p+u)//2
        if v[mijloc]>v[mijloc+1] and v[mijloc-1]<v[mijloc]:
            return (mijloc, v[mijloc])
        elif v[mijloc]>v[mijloc+1]:
            return varful_muntelui(mijloc, v, p, mijloc - 1)
        else:
            return varful_muntelui(mijloc, v, mijloc +1, u)

n=7
v=[1, 3, 4, 8, 9, 12, 1]
print(varful_muntelui("orice", v, 0, n-1))
