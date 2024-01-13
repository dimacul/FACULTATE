l=[[1,2,3],[2, 3, 4, 6], [2,2,2,2,2]]
mini=len(l[0])
for row in l:
    if len(row)<mini:
        mini=len(row)
for row in l:
    del row[mini:]
print(l)
