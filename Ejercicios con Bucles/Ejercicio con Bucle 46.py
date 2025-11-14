#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.

palabra = input("Introduce una palabra, por favor: ")
vocal = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
vocales = ""
consonantes = ""

for i in range(len(palabra)):
    if palabra[i] in vocal:
        vocales = vocales + f"{palabra[i]}"
    else:
        consonantes = consonantes + f"{palabra[i]}"

print(f"Las vocales son {vocales} y las consonantes {consonantes}. ")