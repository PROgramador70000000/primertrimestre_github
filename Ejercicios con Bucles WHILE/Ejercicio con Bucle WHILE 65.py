#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
respuesta = 0
mayor = 0
menor = 0

while respuesta != -99:
    respuesta = int(input("Introduce un número: "))
    if respuesta != -99:
        if respuesta < menor:
            menor = respuesta
        if respuesta > mayor:
            mayor = respuesta

print("RESUMEN")
print(f"El número más grande introducido es el {mayor}")
print(f"El número más pequeño introducido es el {menor}")