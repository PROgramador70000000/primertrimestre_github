#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 

import random
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
palabra = lista[random.randint(0,len(lista) - 1)]
desorden = []
respuesta = ""

for i in range(len(palabra)):
    desorden.append(palabra[i])

random.shuffle(desorden)

print("Se te va a mostrar una palabra desordenada, y vas a tener 3 intentos para averiguarla. ")
print("Las posibles opciones son: ")
print(lista)
print("La palabra desordenada es: ")
print(desorden)

intentos = 0

while respuesta != palabra and intentos < 3:
    respuesta = input("Introduce la palabra: ")
    if respuesta != palabra:
        print(f"{respuesta} no es la palabra. Te quedan {2 - intentos} intentos. ")
    intentos += 1

if respuesta == palabra:
    print("¡Felicidades! Has acertado la palabra. ")
else:
    print("Te has quedado sin intentos. ¡Vuelve a intentarlo! ")