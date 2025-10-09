dolar = 3.78
euro = 4.20
while True:
    soles = float(input("Ingrese el monto en soles: "))

    def conv_d():
        return round(soles / dolar)

    def conv_e():
        return round(soles / euro)

    print("\nBienvenido al sistema de conversión de moneda")
    print("\n1. Dolares")
    print("2. Euros")

    opc = int(input("\nIngrese una opción: "))

    if opc in(1,2):
        if opc == 1: print("\nConversión a dolares: ",conv_d())
        else: print("\nConversión a euros: ",conv_e())
    else: print("Opción no válida!")

    conti = input("¿Desea continuar? presione(y): ")

    if conti != "y":
       print("\nPrograma finalizado!")
       break



