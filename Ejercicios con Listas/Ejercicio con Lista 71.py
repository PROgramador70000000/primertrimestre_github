#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.

lista = []
respuesta = "s"

while respuesta == "s":
    letra = input("Introduce una letra: ")
    if len(letra) == 1 and letra.isalpha():
        if not (letra in lista):
            lista.append(letra)
        respuesta = input("¿Quieres repetir? (s/n): ")

print(lista)