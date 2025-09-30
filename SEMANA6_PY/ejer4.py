g = input("Genere una contraseña: ")

print("\n---------------------------------------------")
print("|           Válida tu contraseña            |")
print("|                                           |")
print("|  1. Ud. tiene 3 intentos                  |")
print("---------------------------------------------")

intentos = 3

while(intentos > 0):
    c = input("\nIngrese la contraseña: ")

    if g == c:
        print("\nAcceso concedido. Bienvenido al sistema.")
        break
    else:
        intentos-=1
        print("Contraseña incorrecta. Intentos restantes ",intentos)

else: print("\nAcceso denegado! cerrando sistema.")