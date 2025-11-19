#40. Crea un programa que cuente todos los números pares hasta el número 50

pares = 0
impares = 0
tope = 50
#Prueba a cambiar tope. ¡El código sigue funcionando!

for i in range(1, tope + 1):
    if (i % 2) == 0:
        pares += 1
    else:
        impares += 1

print(f"Hay {pares} números pares y {impares} números impares. ")