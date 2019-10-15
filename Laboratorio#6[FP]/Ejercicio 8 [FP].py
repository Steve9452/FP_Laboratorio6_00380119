import msvcrt
n=int(input("Ingrese un numero para obtener su tabla de multiplicar "))
for i in range(1,11):
	print(str(n)+"x"+str(i)+"="+str(n*i))
print("Presione una tecla para continuar...")
msvcrt.getch()