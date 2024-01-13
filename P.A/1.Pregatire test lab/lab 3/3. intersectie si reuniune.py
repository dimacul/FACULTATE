a=[2, 4, 7, 15, 23]
b=[4, 15, 30]
r=[]
#reuniunea:
i=0
j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        r.append(a[i])
        i+=1
    elif a[i]==b[j]:
        r.append(a[i])
        i+=1
        j+=1
    else:
        r.append(b[j])
        j+=1
while i<len(a):
    r.append(a[i])
    i+=1
while j<len(b):
    r.append(b[j])
    j+=1
print(r)
r=[]
#intersectia:
i=0; j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        i+=1
    elif a[i]>b[j]:
        j+=1
    else:
        r.append(a[i])
        i+=1
        j+=1
print(r)
