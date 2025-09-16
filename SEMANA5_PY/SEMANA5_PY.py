def ejer1():
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("Puede votar.")

        if edad >=25:
            print("Candidato para un cargo politico")
        else:
            print("No es candidato para un cargo politico")

    else:
        print("No puede votar.")
        print("No puede ejercer un cargo politico.")

def ejer2():
    lado1 = int(input("Ingrese lado1: "))
    lado2 = int(input("Ingrese lado2: "))
    lado3 = int(input("Ingrese lado3: "))

    if(lado1 == lado2 ==lado3):
        print("EQUILATERO")
    elif lado1 == lado2 or lado1==lado3 or lado2==lado3:
        print("ISOSCELES")
    else:
        print("ESCALENO")
ejer2()
