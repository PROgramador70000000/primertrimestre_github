#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.
import random

uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

print("Un dado va a ser tirado 100 veces, luego veremos cuantas veces sale cada número. ")
respuesta = input("¿Quieres tirar el dado las 100 veces automaticamente? (s/n): ")

if not respuesta in "snSN":
    print("Introduce una respuesta válida, por favor. ")
    exit()

if respuesta in "sS":
    print("Cargando...")
    for i in range(100):
        numero = random.randint(1, 6)
        if numero == 1:
            uno += 1
        elif numero == 2:
            dos += 1
        elif numero == 3:
            tres += 1
        elif numero == 4:
            cuatro += 1
        elif numero == 5:
            cinco += 1
        elif numero == 6:
            seis += 1
    print("¡Listo!")
    print(f"Uno: {uno}")
    print(f"Dos: {dos}")
    print(f"Tres: {tres}")
    print(f"Cuatro: {cuatro}")
    print(f"Cinco: {cinco}")
    print(f"Seis: {seis}")
    exit()
elif respuesta in "nN":
    print("De acuerdo, cada vez que quieras lanzar el dado pulsa intro: ")
    for i in range(100):
        espera = input("")
        numero = random.randint(1, 6)
        print(f"El dado ha sacado un {numero}")
        if numero == 1:
            uno += 1
        elif numero == 2:
            dos += 1
        elif numero == 3:
            tres += 1
        elif numero == 4:
            cuatro += 1
        elif numero == 5:
            cinco += 1
        elif numero == 6:
            seis += 1
        print(f"Te quedan {100 - (i + 1)} intentos. ")
    print(f"Uno: {uno}")
    print(f"Dos: {dos}")
    print(f"Tres: {tres}")
    print(f"Cuatro: {cuatro}")
    print(f"Cinco: {cinco}")
    print(f"Seis: {seis}")
    exit()