def ejer1(): #creando metodo ejer1
    nombre = input("Ingrese su nombreP: ")
    carrera = input("Ingese su carrera: ")

    print(f"\n{nombre}, bienvenido a FA de {carrera}") 

def ejer2():
    print("\"\"Yordan\"\"")

def ejer3():
    x = int(input("Ingrese el valor de x: "))
    y = int(input("Ingrese el valor de y: "))

    print("Suma: ", (x+y))
    print("Resta: ", (x-y))
    print("Multiplicación: ", (x*y))
    print("División: ", (x/y))

import math #importando la libreria math

def ejer4():
    num = float(input("Ingrese un número decimal: "))

    print("Raiz 2: ", math.sqrt(num))
    print("redondeado: ", round(num,0))
    print("al cubo: ",math.pow(num,3))
    print("raiz 3: ", num ** (1/3))

def ejer5():
    num = input("Ingrese número: ")

    entero = int(num)
    deci = float(num)

    print("Resto: ", (entero%2))
    print("División: ", (deci/3))

ejer5()
