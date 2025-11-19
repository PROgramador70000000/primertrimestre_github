#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While

veces = int(input("Introduce el número de veces que quieres que diga Buenos días: "))
cuenta = 0

while cuenta < veces:
    print("¡Buenos días!")
    cuenta += 1