#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:

palabra = input("Introduce una palabra, por favor: ")
vocal = "aeiouáéíóúü"
vocales = ""
consonantes = ""

for i in range(len(palabra)):
    if palabra[i] in vocal:
        vocales = vocales + f"{palabra[i]}"
    else:
        consonantes = consonantes + f"{palabra[i]}"

print(f"Las vocales son {vocales} y las consonantes {consonantes}. ")