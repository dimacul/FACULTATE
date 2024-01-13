
n=int(input("dati n"))
urm_elem = 1


"""
c1 = colt stg sus     c2 = colt dr sus
                ......
c3 = colt stg jos     c4 = colt dr jos
"""
def populeaza_tabla(matrice, c1, c2, c3, c4):
    global urm_elem
    if c1 == c2 and c2 == c3 and c3 == c4:
        matrice[c1[0]][c1[1]] = urm_elem
        urm_elem+=1
        print("a intrat")
    else:
        mijloc_x = (c1[0] + c3[0])//2
        mijloc_y = (c1[1] + c2[1])//2
        populeaza_tabla(matrice, (c1[0],mijloc_y+1), c2, (mijloc_x, mijloc_y +1), (mijloc_x, c4[1]))
        populeaza_tabla(matrice, (mijloc_x+1, c1[1]), (mijloc_x +1, mijloc_y), c3, (c4[0], mijloc_y))
        populeaza_tabla(matrice, c1, (c2[0], mijloc_y), (mijloc_x, c3[1]), (mijloc_x, mijloc_y))
        populeaza_tabla(matrice, (mijloc_x +1, mijloc_y +1), (mijloc_x + 1,c2[1]), (c3[0], mijloc_y + 1), c4)

def printeaza_matrice(matrice, n):
    for i in range(2**n):
        for j in range(2**n):
            print(matrice[i][j], end=" ")
        print()

matrice = [[ 0 for x in range(2**n)] for y in range(2**n)]
printeaza_matrice(matrice, n)
populeaza_tabla(matrice, (0,0), (0, 2**n-1), (2**n - 1, 0), (2**n -1, 2**n - 1))
printeaza_matrice(matrice, n)
