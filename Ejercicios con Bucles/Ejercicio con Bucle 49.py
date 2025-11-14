#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

palabra = input("Introduce la palabra secreta: ")
letra_encontrada = ""
salida = ""

for i in range(len(palabra)):
    letra = input("Introduce una letra: ")
    for j in range(len(palabra)):
        if palabra[j] == letra:
            letra_encontrada = letra_encontrada + f"{j + 1}"
    if letra_encontrada == "":
        salida = f"La {letra} no está en la palabra secreta. "
    else:
        for h in range(len(letra_encontrada)):
            if h == 0:
                salida = f"La {letra} se encuentra en la posición {letra_encontrada[h]} de la palabra secreta"
            elif h < len(letra_encontrada) - 1:
                salida = salida + f", en la posición {letra_encontrada[h]} de la palabra secreta"
            else:
                salida = salida + f" y en la posición {letra_encontrada[h]} de la palabra secreta. "
    print(salida)
    letra_encontrada = ""
    salida = ""
print("Se te han acabado los intentos. ")