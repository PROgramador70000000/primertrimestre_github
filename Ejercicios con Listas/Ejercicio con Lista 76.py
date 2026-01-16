#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.

lista1 = ["a","b","D","x","r","X","3","h","w","2","i"]
letras = []
numeros = []

for i in range(len(lista1)):
    if lista1[i].isalpha():
        if lista1[i].isupper():
            letra = lista1[i].casefold()
        else:
            letra = lista1[i]
        letras.append(letra)
    elif lista1[i].isnumeric():
        numeros.append(lista1[i])

respuesta = input("Introduce 1 para visualizar en orden ascendente o 2 descendente: ")

if respuesta == "1":
    letras.sort()
    numeros.sort()
    print(letras)
    print(numeros)
elif respuesta == "2":
    letras.sort(reverse = True)
    numeros.sort(reverse = True)
    print(letras)
    print(numeros)
else:
    print("La respuesta no es uno de los valores comprendidos. ")