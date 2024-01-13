f=open("test.in")
for linie in f:
    op1, rest=linie.split("*")
    op2, rez=rest.split("=")
    op1=int(op1)
    op2=int(op2)
    rez=int(rez)
    with open("test.out", "a") as g:
        g.write(linie.strip("\n")+" ")
        if op1*op2==rez:
            g.write("Corect\n")

        else:
            g.write("Gresit ")
            g.write(str(op1*op2)+"\n")

