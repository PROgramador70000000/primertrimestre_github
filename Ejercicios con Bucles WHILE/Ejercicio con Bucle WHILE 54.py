#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While

total = 0
repeticiones = 0

while total < 50:
    repeticiones += 1

    primero = int(input("Introduce el primer número entero: "))
    segundo = int(input("Introduce el segundo número entero: "))
    suma = segundo + primero

    total += suma

    print(f"La suma de {primero} y {segundo} es {suma}. ")
    
    if repeticiones == 1:
        print(f"El total acumulado es de {total} y llevas {repeticiones} repetición realizada. ")
    else:
        print(f"El total acumulado es de {total} y llevas {repeticiones} repeticiones realizadas. ")
