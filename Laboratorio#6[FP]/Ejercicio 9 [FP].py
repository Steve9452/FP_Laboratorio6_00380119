import msvcrt
n=int(input("Ingrese numero para buscar multiplos : "))
print("Ingrese rango: ")
r1=int(input("desde: "))
r2=int(input("hasta: "))
nmod=0
for i in range(r1,r2+1):
    nmod=i%n
    if(nmod==0):
        print(i)
print("Presione una tecla para continuar...")
msvcrt.getch()