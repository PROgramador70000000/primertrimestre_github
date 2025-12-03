#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
respuesta = 0
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
suma = 0

while respuesta != -99:
    respuesta = int(input("Introduce un número: "))
    if respuesta != -99:
        if respuesta % 2 == 0:
            pares += 1
        else:
            impares += 1
        if respuesta > 0:
            positivos += 1
        elif respuesta == 0:
            ceros += 1
        elif respuesta < 0:
            negativos += 1
        suma += respuesta 

print("RESUMEN")
print(f"El número de pares es {pares}")
print(f"El número de impares es {impares}")
print(f"El número de positivos es {positivos}")
print(f"El número de negativos es {negativos}")
print(f"La suma total de los números es {suma}")