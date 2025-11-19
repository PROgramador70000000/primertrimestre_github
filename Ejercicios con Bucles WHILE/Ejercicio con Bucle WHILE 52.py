#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While

respuesta = "s"

while respuesta == "s":
    primero = int(input("Introduce el primer número entero: "))
    segundo = int(input("Introduce el segundo número entero: "))
    suma = segundo + primero

    print(f"La suma de {primero} y {segundo} es {suma}. ")
    respuesta = input("¿Quieres volver a introducir dos números? (s/n): ")

print("Programa finalizado. ")