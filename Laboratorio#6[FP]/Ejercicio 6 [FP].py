import msvcrt
aux=1
while(aux!=0):
    n=int(input("Ingrese un numero de dos digitos "))
    if(n>10):
        n1=n%10
        n2=n-n1
        n3=int(n2/10)
        aux=0
print (str(n1)+str(n3))
print("Presione una tecla para continuar...")
msvcrt.getch()