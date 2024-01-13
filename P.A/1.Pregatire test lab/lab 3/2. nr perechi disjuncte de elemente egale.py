v=[4, 5, 2, 9, 1, 0, 1, 1, 3, 2, 3, 9, 4, 4, 0]
fr=[0]*100
for elem in v:
    fr[elem]+=1
sum = 0
for i in range(100):
    if fr[i]!=0:
        fr[i] = (fr[i]-1)*fr[i]//2
        print(f"Cu sosete de tipul {i} se pot forma {fr[i]} perechi")
        sum+=fr[i]

print(f"Nr total perechi: {sum}")

