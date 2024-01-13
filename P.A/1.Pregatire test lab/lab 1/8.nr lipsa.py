n = int(input("Introduceti n: "))
missing_number = 1

for i in range(2, n+1):
    nr = int(input(f"Introduceti numarul {i}: "))
    missing_number ^= nr
    missing_number ^= i

print(f"Numarul lipsa este: {missing_number}")
