#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.

abecedario = "abcdefghijklmnñopqrstuvwxyz"
veces = int(input("Introduce el número de palabras: "))
lista = []

for i in range(veces):
    palabra = input(f"Introduce la palabra {i + 1}: ")
    lista.append(palabra)

lista.sort()
print(f"La lista en orden ascendente es: {lista}. ")

lista.sort(reverse = True)
print(f"La lista en orden descendente es. {lista}. ")