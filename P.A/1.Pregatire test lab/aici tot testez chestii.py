print(2.5//1.5) #1.0
print(11//3)#3

print(-11//3)#-4
print(-11%3)#1 -> impartitor poz -> cat neg, rest poz
#          -11 = 3 * -4 + 1

print(11//-3)#-4 ->rotunjire inferioara
print(11%-3)#-1 -> impartitor neg -> cat poz, rest neg
#x%y = x -( (x//y) * y)

#TEST DE PARITATE PE BITI:
x=16
print(x&(x-1) == 0)

#OPERATORUL CONDITIONAL (TERNAR):
x=2; y=3
z = x-y if x>y else y-x
print(f"Modulul diferentei numerelor {x} si {y} este: {z} ")
grupa = 130
media = 5
print(grupa//10 ==14 or grupa //10 == 10 and media >=9)
                            #evalueaza intai asta



