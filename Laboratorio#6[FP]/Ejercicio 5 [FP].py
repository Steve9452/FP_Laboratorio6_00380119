import msvcrt

si=1000
aux=1
while(aux!=0):
    print("***CAJERO AUTOMATICO***")
    print("1- Restiro")
    print("2- Deposito")
    print("Saldo actual:$"+str(si))
    opcion=int(input("Ingrese la opcion "))
    if (opcion==1):
        n=float(input("Ingrese el monto a retirar $"))
        if(n<si):
            si-=n
            aux=0
        else:
            print("El saldo es insuficiente para realizar el retiro ")
            print("Presione una tecla para continuar...")
            msvcrt.getch()
    elif (opcion==2):
        n=float(input("Ingrese el monto a depositar $"))
        si+=n
        aux=0
    else:
        print("Ingrese una opcion valida ")
        aux=1
print("El saldo total es $"+str(si))
print("Presione una tecla para continuar...")
msvcrt.getch()
