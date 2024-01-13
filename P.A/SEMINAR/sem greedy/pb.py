L=[20, 30, 20, 50]
L1=[]
import heapq
for i in range(len(L)):
    heapq.heappush(L1, (L[i], i+1))
i=0
while(len(L1)>1):
    x1, xi=heapq.heappop(L1)
    y1, yi=heapq.heappop(L1)
    print(f"interclasare({xi}, {yi})")
    heapq.heappush(L1, (x1+y1, len(L)+i))
    i+=1
