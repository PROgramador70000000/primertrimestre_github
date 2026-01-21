#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe algún método que permita sumar el contenido de una lista?

import random
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"]
vuelve = "s"
veces = 0
puntuaciones = []
total = 0

while vuelve == "s":
    palabra = lista[random.randint(0,7)]
    intentos = 0
    respuesta = ""
    print("Tienes que acertar una palabra aleatoria de esta lista: ")
    print(lista)
    while respuesta != palabra:
        respuesta = input("Introduce la palabra secreta: ")
        intentos += 1
        if respuesta != palabra:
            print(f"{respuesta} no era la palabra secreta. Llevas {intentos} intentos. ")
    print(f"¡Felicidades! {respuesta} era la palabra secreta. ")
    puntos = 9 - intentos
    print(f"Has necesitado {intentos} intentos, así que has obtenido {puntos} puntos. ")
    puntuaciones.append(puntos)
    veces += 1

    vuelve = input("¿Quieres volver a jugar? (s/n): ")

print(f"Puntuaciones: {puntuaciones}")
for i in range(len(puntuaciones)):
    total += puntuaciones[i]
print(f"Tu puntuación es de {total}")
media = veces * 4
print(f"La media de las partidas realizadas es de {media}")

if media <= total:
    print("Tienes buena suerte; ¡tu total es mayor a la media!")
else:
    print("Dedícate al parchís... Tu puntuación es inferior a la media. ")