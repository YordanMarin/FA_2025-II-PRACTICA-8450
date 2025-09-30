import random

print("**********************************************")
print("*        Bienvenido al juego adivinador      *")
print("*                                            *")
print("* 1. Adivinar el número entre 1 y 20         *")
print("* 2. Tienes 3 intentos                       *")
print("**********************************************")

intentos = 3
secreto = random.randint(1,20)

while intentos>0:
    num = int(input("\nIngrese número: "))

    if secreto == num:
        print("\nCorrecto! Adivinaste el número.")
        break
    else:
        intentos-=1
        if num < secreto: print(f"\nPista: El número es mayor. te quedan {intentos} intentos")
        else: print(f"\nPista: El número es menor. te quedan {intentos} intentos")
else: print("\nNo lograste adivinar el número ", secreto)