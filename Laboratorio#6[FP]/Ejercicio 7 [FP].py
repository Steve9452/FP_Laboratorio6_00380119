import msvcrt
n=int(input("Ingrese el numero de filas: "))

for i in range(1,n+1):
    print((str("*")+" ")*n)
print("Presione una tecla para continuar...")
msvcrt.getch()
