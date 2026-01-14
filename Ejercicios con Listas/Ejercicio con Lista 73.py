#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no

lista1 = []
lista2 = []
iguales = []
diferentes = []
respuesta = "s"

while respuesta == "s":
    palabra = input("Introduce una palabra para la lista 1: ")
    lista1.append(palabra)
    respuesta = input("¿Quieres introducir otra palabra? (s/n): ")

respuesta = "s"

while respuesta == "s":
    palabra = input("Introduce una palabra para la lista 2: ")
    lista2.append(palabra)
    respuesta = input("¿Quieres introducir otra palabra? (s/n): ")

if len(lista1) > len(lista2):
    mayor_longitud = len(lista1)
    lista = 1
else:
    mayor_longitud = len(lista2)
    lista = 2

for i in range(mayor_longitud):
    if lista == 1:
        if lista1[i] in lista2:
            iguales.append(lista1[i])
        else:
            diferentes.append(lista1[i])
    elif lista == 2:
        if lista2[i] in lista1:
            iguales.append(lista2[i])
        else:
            diferentes.append(lista2[i])

print(f"Están repetidas: {iguales}")
print(f"No están repetidas: {diferentes}")