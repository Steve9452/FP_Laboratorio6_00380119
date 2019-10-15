import msvcrt
from random import *
x=randrange(1,10)
cont=0
n=12
while(n!=x):
    n=int(input("Ingrese un numero entre 1 y 10: "))
    if (n>x):
        print("Ingrese un numero menor: ")
    elif(n<x):
        print("Ingrese un numero mayor: ")
    cont+=1
print("Correcto ")
print("Numero de intento fue "+str(cont))
print("Presione una tecla para continuar...")
msvcrt.getch()
