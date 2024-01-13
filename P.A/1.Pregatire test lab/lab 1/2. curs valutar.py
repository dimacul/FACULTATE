n = int(input("da-mi n: "))
curs_ant = float(input())
dif_max = 0
i_max=1
for i in range(1, n):
    curs = float(input())
    dif = curs - curs_ant
    if dif > dif_max:
        i_max = i + 1
        dif_max = dif
    curs_ant = curs
if(dif_max == 0):
    print("Nu a crescut sau s-a modificat doar scazand")
else:
    print(f"Dif max e {dif_max} inregistrata inntre zilele {i_max-1} si {i_max}")
