import msvcrt
cont=0
p="s"
aux=1
n2=0
while (aux!=0):
    while (p=="s"):
        n=int(input("Ingrese un numero par "))
        n2=n%2
        if(n2!=0):
            print("El numero ingresado no es un numero par intentelo de nuevo ")
            p="s"
        else:
            cont+=1
            p=str(input("Quiere escribir otro numero par? s/n: "))
            aux=1
    aux=0
print("Ha escrito "+str(cont)+" numeros pares")
print("Presione una tecla para continuar...")
msvcrt.getch()