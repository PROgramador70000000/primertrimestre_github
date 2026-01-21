#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra

import random
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
palabra = lista[random.randint(0,7)]
respuesta = ""

print("Vas a tener que averiguar una palabra aleatoria de esta lista: ")
print(lista)

while respuesta != palabra:
    respuesta = input("Introduce la palabra secreta: ")
    if respuesta != palabra:
        print("SIGUE JUGANDO")

print("ACERTASTE")