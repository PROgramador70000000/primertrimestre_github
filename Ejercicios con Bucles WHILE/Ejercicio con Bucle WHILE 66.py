#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos. 

import time
import random

inicio = time.time()
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

while (time.time() - inicio) < 3:
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

print("RESUMEN")
print(f"Tiempo: {time.time() - inicio}")
print(f"Uno: {uno}")
print(f"Dos: {dos}")
print(f"Tres: {tres}")
print(f"Cuatro: {cuatro}")
print(f"Cinco: {cinco}")
print(f"Seis: {seis}")