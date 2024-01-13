a, b = input().split()
a = int(a)
b =int(b)

x=1
y=1
while y<a:
    y=x+y
    x=y-x
if y<=b:
    print(y)
else:
    print("imposibil")
