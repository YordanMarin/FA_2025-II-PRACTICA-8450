while True:
    suma = 0
    num = int(input("Ingrese un número positivo: "))

    for i in range(1,num+1):
        suma += i
        print(i, end=" ")

    print("\nSuma: ",suma)
    opc = input("\n¿Desea continuar?(S/N): ")

    if(opc =="N"): break
