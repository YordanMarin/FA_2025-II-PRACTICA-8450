def suma(a,b): print("\nLa suma es: ",a+b)
def resta(a,b): print("\nLa resta es: ",a-b)
def multi(a,b): print("\nLa Multiplicación es: ",a*b)
def divi(a,b): 
    if b != 0: print("\nLa División es: ",a+b)
    else: print("\nError. No se puede dividir entre 0")

def operaciones():
    while True:
        print("Menú de operaciones")
        print("\n1.Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        opc = int(input("\nIngrese una opción: "))

        a = int(input("\nIngrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

        if opc in (1,2,3,4):
            if opc == 1: suma(a,b)
            elif opc == 2: resta(a,b)
            elif opc == 3: multi(a,b)
            elif opc == 4: divi(a,b)
        else: print("Opción no válida!")

        conti = input("¿Desea continuar? presione(y): ")

        if conti != "y":
            print("\nPrograma finalizado!")
            break

operaciones()