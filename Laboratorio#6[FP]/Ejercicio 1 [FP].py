import msvcrt
a=float(input("Ingrese precio de pelicula 1: "))
b=float(input("Ingrese precio de pelicula 2: "))
c=float(input("Ingrese precio de pelicula 3: "))
total=0
if ((a<b)and(a<c)):
    total+=a
    if (b<c):
        total+=b
    else:
        total+=c
if ((b<a)and(b<c)):
    total+=b
    if (a<c):
        total+=a
    else:
        total+=c
if ((c<a)and(c<b)):
    total+=c
    if (a<b):
        total+=a
    else:
        total+=b
print(total)
print("Presione una tecla para continuar...")
msvcrt.getch()
