#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

palabra = input("Introduce la palabra secreta: ")

for i in range(len(palabra)):
    letra = input("Introduce una letra, por favor: ")
    if letra in palabra:
        for j in range(len(palabra)):
            if letra is palabra[j]:
                print(f"La {letra} se encuentra en la posición {j + 1} de la palabra secreta. ")
    else: 
        print(f"La {letra} no está en la palabra secreta. ") 
print("Se te han acabado los intentos. ")