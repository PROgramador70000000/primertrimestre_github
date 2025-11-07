#35. Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre

nombre = input("Introduce tu nombre completo: ")
veces = int(input("Introduce el número de veces que quieres repetir tu nombre: "))

for x in range(0,veces):
    print(nombre)