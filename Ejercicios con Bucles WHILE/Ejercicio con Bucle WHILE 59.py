#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random

numero = random.randint(0, 1000)
intentos = 0
respuesta = -1

print("Hay un número aleatorio entre 0 y 1000 que tienes que adivinar. ¡Buena suerte!")

while respuesta != numero:
    respuesta = int(input("Introduce tu número: "))
    if respuesta <= 1000 and respuesta >= 0:
        if respuesta != numero:
            if respuesta < numero:
                print(f"Has fallado, el número secreto es mayor que {respuesta}")
            elif respuesta > numero:
                print(f"Has fallado, el número secreto es menor que {respuesta}")
    else:
        print(f"El {respuesta} no está entre 0 y 1000... ¡Vuelve a intentarlo! ")
    intentos += 1

print(f"¡Felicidades! El número secreto era {numero}")
if intentos == 1:
    print(f"¡Increíble! Has averiguado el {numero} en {intentos} intento. ")
else:
    print(f"Has necesitado {intentos} intentos para averiguarlo. ")