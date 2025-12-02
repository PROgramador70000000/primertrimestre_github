#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random

numero = random.randint(1,5)
respuesta = 0

print("Hay un número aleatorio entre 1 y 5 que tienes que adivinar. ")

respuesta = int(input("Introduce tu número: "))
if respuesta <= 5 and respuesta >= 1:
    if respuesta == numero: 
        print(f"¡Has acretado! El número secreto era {numero}")
    else: 
        print(f"El número {respuesta} no es el número secreto. ")
        print(f"El numero secreto era {numero}")
else:
    print("El número que has introducido no está entre 1 y 5... ¡Vuelve a intentarlo!")

