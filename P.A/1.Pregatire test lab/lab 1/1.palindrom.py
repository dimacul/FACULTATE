n = int(input())
cn =n
inversul = 0
while n>0:
    inversul = inversul *10+ n%10
    n//=10
if (inversul == cn):
    print("palindr")
else: print("nu")
