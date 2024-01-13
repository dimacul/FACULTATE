#perechea problemei cu spectacolele
#se dau n intervale [s_i, t_i]
#vreau sa le programez pe toate
#care e numarul minim de sali de care am nevoie pt a le programa pe toate + o programare?

"""
ex: 1-3, 1-4, 6-8, 5-10

rez: 1-3 6-8   sala 1
     1-4 5-10  sala 2
"""

"""
Idei:
    (1)
    - luam intervalele pe rand intr-o anumita ordine:
                                                - crescator dupa terminare (ca la spectacole)
                                                - crescator dupa inceput - cronologic
    - incercam sa programam intervalul curent i intr-o sala existenta
    - daca nu se poate, cream sala noua
    - daca se poate - nu alegem o sala arbitrar la care sa adaugam i, ci o alegem pe cea cu timpul
        de terminare al ultimului interval cat mai mare, pt a lasa spatii libere cat mai mici
    -ex:
        1-3, 1-5, 6-7, 4-8
                   |
                poate fi adaugat si in sala 1, si in sala 2->aleg cea care se termina mai tarziu
        sala 1: 1-3  4-8      |   
        sala 2: 1-5          6-7
    
    Corect, dar de ce? (tema)
    
    
    
    (2)
        Consideram intervalele ordonate crescator dupa inceput.
    -pt intervlul curent i
        -nu se poate adauga la o sala => creez sala noua
        -se poate adauga la o sala existenta => o aleg pe care vreau 
        (pt ca toate celelalte activitati incep mai tarziu decat i)
        
    Am probleme cand am multe activ care se suprapun?
    1-3 1-4 1-5   ....   1-n
    s1: 1-3               I
    s2: 1-4             le va intreba pe toate daca se poate lipi
    s3: 1-5
    
    
    s n-3: n-1

    Solutie:
    Este suficient sa testez daca i se poate adauga la sala
       cu timpul de terminare a ultimului interval minim
    
    sali [1-3 5-9], [1-4 6-8]
           sala1      sala2
           
    heap (terminare, nr_sala)
"""

n = 4
intervale = [(1, 3), (1, 4), (6, 8), (5,9)]
intervale.sort()        #sorted() nu modifica obiectul
import heapq
sali=[]
h=[]       #heap-ul = coada de prioritati
sali.append([intervale[0]])                 #punem primul interval in prima sala
heapq.heappush((h, (intervale[0][1], 0))   #in sala 0 pun timpul de terminare al primului interval intervale[0][1], adaug in heap
for i in range(1, len(intervale)):         #pe primul il sar, luam la rand celelalte intervale
    #intervale[i] e intervalul curent
    t, m = heapq.heappop(h)                 #extrage sala care se termina cel mai devreme

    #t=timp de terminare, m=indicele salii
    if intervale[i][0]>t:       #testez daca timpul de inceput intervale[i]>t=>se poate adauga in sala m
        sali[m].append(intervale[i])    #aDAUG INTERVALUL in sala m
        heapq.heappush(h, (intervale[i][1], m)) #inseram in heap sala m cu noul timp de terminare
    else:
        sali.append([intervale[i]])         #daca nu se poate adauga, creez sala noua doar cu intervalul i
                                            #noua sala va avea indicele len(sali)-1 -> o adaug in heap
        heapq.heappush(h, (intervale[i][1], len(sali)-1)))

    #t, m -> am putut adauga int[i][1], m
    #     -> nu am putut adauga ...

    heapq.heappush(h, (t, m))   #adaugam inapoi sala extrasa, pt ca nu am putut adauga nimic la ea

print(len(sali))
for sala in sali:
    print(*sala)
"""
Corect, deoarece:
        |
    ---|------
    Daca exista k intervale care contin x=> sunt necesare min k sali
    Fie k nr de sali determinat de algoritmul greedy
    E suficient sa dem ca atunci cand alg a creat sala k, existau k intervale cu un punct comun, deci 
        sala k era necesara
    
    s1      s1-----|--t1
    s2      s2-----|------t2
                   |
    
    sk -1   sk-1---|---tk-1   
    sk             s----------t

Intr-adevar, fie I=[s, t] primul interval adaugat in sala k, atunci intr-adevar orice j=1, k-1, in
    sala Sj exista un interval care contine s=> Exista k intervale care contin s


Idee: sala 1-> programez in ea un nr maxim posibil de spectacole (pb spectacolelor)
      Daca mai sunt spectacole neprogramate, creez sala2 s.a.m.d
      
      Nu merge, pt ca - similar cu contraexemplul de la spectacole
"""

