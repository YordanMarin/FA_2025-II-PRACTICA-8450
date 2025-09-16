def ejer1():
    edad = int(input("Ingrese una edad: "))

    if edad < 18:
        print("Menor de edad")
    else:
        if edad >= 18 and edad <=64:
            print("Adulto")
        else:
            print("Adulto mayor")

def ejer2():
    annio = int(input("Ingrese el año: "))

    if (annio %4 ==0 and annio %100 != 0) or (annio %400 ==0):
        print("\nEl año es bisiesto")
    else:
        print("\nEl año no es bisiesto")

    if annio %2 ==0:
        print("El año es par")
    else:
        print("El año es impar")

def ejer3():
    monto = float(input("Ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")

    opcion=int(input("\nIngrese una opción: "))

    match opcion:
        case 1: print("Dolares: ", round((monto/3.75),0))
        case 2: print(f"Euros: {monto/4.05:.2f}")
        case _: print("Opción incorrecta")

import math

def ejer4():
    print("Bienvenido al sistema de calculos de áreas\n")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo\n")

    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            lado = int(input("Ingrese lado: "))
            print("Área cuadrado: ",lado*lado)
        case 2:
            bse = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print("Área rectangulo: ",(bse*alt))
        case 3:
            bse2 = int(input("Ingrese la base: "))
            alt2 = int(input("Ingrese la altura: "))
            print("Área triangulo: ",(bse2*alt2)/2)
        case 4:
            radio = float(input("Ingrese el radio: "))
            print("Área del circulo: ",(round(math.pi * radio**2),2))
        case _: print("Opción incorrecta")

ejer4()

