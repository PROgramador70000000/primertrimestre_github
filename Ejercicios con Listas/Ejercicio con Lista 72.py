#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista

lista = []
respuesta = "s"
excepciones = "áéíóúàèìòù"
correctas = "aeiouaeiou"

while respuesta == "s":
    letra = input("Introduce una letra: ")
    if len(letra) == 1 and letra.isalpha():
        if letra in excepciones:
            vocal = excepciones.find(letra)
            letra = correctas[vocal]
        if not (letra in lista):
            lista.append(letra)
        respuesta = input("¿Quieres repetir? (s/n): ")

print(lista)