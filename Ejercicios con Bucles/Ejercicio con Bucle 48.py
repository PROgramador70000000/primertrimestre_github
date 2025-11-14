#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario tenga x oportunidades para ver si letra introducida está en esa palabra

palabra = input("Introduce la palabra secreta: ")

for i in range(len(palabra)):
    letra = input("Introduce una letra: ")
    if letra in palabra:
        print("La letra está en la palabra secreta. ")
    else:
        print("La letra no está en la palabra secreta. ")

print("Se te han acabado los intentos. ")