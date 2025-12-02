#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random

numero = random.randint(1,5)
respuesta = 0
intentos = 3
correcto = 1

print("Hay un número aleatorio entre 1 y 5 que tienes que adivinar. Tienes tres intentos. ")

while intentos > 0 and respuesta != numero:
    respuesta = int(input("Introduce tu número: "))
    if respuesta >= 1 and respuesta <= 5:
        correcto = 1
    else:
        correcto = 0
        print("Tu respuesta no está entre 1 y 5... ¡Vuelve a intentarlo!")
    if respuesta != numero and correcto == 1:
        print(f"El {respuesta} no es el número secreto. ¡Vuelve a intentarlo!")
    intentos -= 1
    if intentos > 0 and respuesta != numero:
        if intentos == 1:
            print(f"Te queda {intentos} intento. ")
        else:
            print(f"Te quedan {intentos} intentos. ")
    
if intentos == 0:
    print(f"Te has quedado sin intentos. El número secreto era {numero}")
else:
    print(f"¡Has acertado! El número secreto era {numero}")