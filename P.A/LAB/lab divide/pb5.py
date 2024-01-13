def citeste_vector(vector, fisier):

    vector = [int(x) for x in f.readline().split()]
    return vector


def gaseste_mediana_interclasare(a, b):
    n = len(a)

    # Verificăm dacă vectorul interclasat are un număr par sau impar de elemente
    numar_total_elemente = 2 * n
    este_numar_impar = numar_total_elemente % 2 != 0

    # Folosim o funcție auxiliară pentru a găsi mediana
    def gaseste_mediana(lo, hi):
        # Găsim poziția medianei în vectorul interclasat
        pozitie_mediana = (lo + hi) // 2

        # Calculăm poziția corespunzătoare în vectorii a și b
        pozitie_mediana_a = pozitie_mediana
        pozitie_mediana_b = numar_total_elemente - pozitie_mediana - 1

        # Obținem valorile de la pozițiile medianelor
        valoare_mediana_a = a[pozitie_mediana_a] if pozitie_mediana_a < n else float('inf')
        valoare_mediana_b = b[pozitie_mediana_b] if pozitie_mediana_b < n else float('inf')

        # Determinăm mediana în funcție de tipul de vector (par sau impar)
        if valoare_mediana_a <= valoare_mediana_b:
            return valoare_mediana_a
        else:
            return valoare_mediana_b

    # Inițializăm limitele pentru căutarea binară în vectorul interclasat
    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        # Folosim funcția auxiliară pentru a găsi mediana
        mediana = gaseste_mediana(mid, n - 1)

        # Verificăm dacă am găsit mediana
        if este_numar_impar and lo == hi:
            return mediana
        elif not este_numar_impar and lo == hi - 1:
            # Dacă avem un număr par de elemente, trebuie să găsim și elementul următor
            mediana_urmatoare = gaseste_mediana(mid + 1, n - 1)
            return (mediana + mediana_urmatoare) / 2

        # Ajustăm limitele pentru căutarea binară
        if a[mid] < b[n - 1 - mid]:
            lo = mid + 1
        else:
            hi = mid - 1

a=[]
b=[]
f=open("pb5.in")
a = citeste_vector(a, "pb5.in")
b = citeste_vector(b, "pb5.in")
print(a)
print(b)
mediana = gaseste_mediana_interclasare(a, b)
print("Mediana vectorului interclasat:", mediana)

