#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While

respuesta = "s"
total = 0
repeticiones = 0

while respuesta == "s":
    repeticiones += 1

    primero = int(input("Introduce el primer número entero: "))
    segundo = int(input("Introduce el segundo número entero: "))
    suma = segundo + primero

    total += suma

    print(f"La suma de {primero} y {segundo} es {suma}. ")
    respuesta = input("¿Quieres volver a introducir dos números? (s/n): ")

print(f"Resumen: has repetido el programa {repeticiones} veces, y la suma total de los números que has introducido es {total}. ")