#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida

import math

primero = int(input("Introduce el primer intervalo, por favor: "))
segundo = int(input("Introduce el segundo intervalo, por favor: "))

longitud = primero - segundo 
longitud = longitud ** 2
longitud = math.sqrt(longitud) + 1
longitud = int(longitud)

suma_resta = (primero - segundo) / ((longitud - 1) * -1)
suma_resta = int(suma_resta)

previo = ""
salida = ""

for i in range(longitud):
    previo = previo + f"{primero + (i * suma_resta)}" + "-"

for i in range(len(previo) - 1):
    salida = salida + f"{previo[i]}"

print(salida)