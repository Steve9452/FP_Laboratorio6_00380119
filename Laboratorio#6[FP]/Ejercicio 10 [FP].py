import os
import msvcrt
def menu():
    print("CONVERTIDOR DE UNIDADES DE TEMPERATURA")
    print("Selecciona una opción")
    print("\t1 - Convertir Fahrenheit a Celsius: ")
    print("\t2 - Convertir Celsius a Fahrenheit: ")
    print("\t3 - Convertir Kelvin a Celsius: ")
    print("\t9 - salir")

def fac():#(32 °F − 32) × 5/9 = 0 °C
    n=float(input("Ingrese grados Fahrenheit: "))
    n-=32
    n*=5/9
    print(n)
    print("Presione una tecla para continuar...")
    msvcrt.getch()
def caf():#(0 °C × 9/5) + 32 = 32 °F
    n=float(input("Ingrese grados Celsius "))
    n*=9/5
    n+=32
    print(n)
    print("Presione una tecla para continuar...")
    msvcrt.getch()
def kac():#0 K − 273.15 = -273.1 °C
    n=float(input("Ingrese grados Celsius "))
    n-=273.15
    print(n)
    print("Presione una tecla para continuar...")
    msvcrt.getch()
while True:
    menu()
    opcionmenu=int(input("Opcion: "))
    if(opcionmenu==1):
        fac()
        break
    elif(opcionmenu==2):
        caf()
        break
    elif(opcionmenu==3):
        kac()
        break
    elif(opcionmenu==9):
        break
    else:
        print("Ingrese una opcion valida")