s="abccabcababc"
poz=0
while poz!=-1:
    poz=s.find("abc", poz)
    if poz!=-1:
        print(poz)
        poz+=1

