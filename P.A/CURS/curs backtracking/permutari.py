#1 Cum reprezint solutia?
#x=(x0, x1, ... xn-1) - o permutare, xk aprtine 1,2,   n

#2 Ce vreau la final de la vector?
#xi!=xj, orice i diferit de j

#3 Care sunt conditiile de continuare la pasul k?

#xk != x0, ...., xk-1

def back(k, x, n):   #k -> dam valori lui xk
    if k == n:   #k==1 + ultimul indice
    # incerc sa dau valori lui xn, deci am completat deja x
        print(*x) #retinem solutia
    else:
        #luam pe rand toate valorile posibile pt xk
        for val in range(1, n+1):
            x[k]=val
            if continuare(k, x):
                back(k+1, x, n) #avanseaza

def continuare(k, x):
    #return x[k] not in x[:k] - felierea are complex O(n) si face si copie//nu recomanda profa
    for i in range(0, k): #si cu index(x[k], 0, k)
        if x[i]==x[k]:
            return False
    return True

def genereaza_permutari(n):
    x=[0]*n
    back(0, x, n)

genereaza_permutari(3)

#as putea marca cand am fost deja pe la un anumit elem
