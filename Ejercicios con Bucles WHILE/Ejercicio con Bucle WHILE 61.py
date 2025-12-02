#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.

numero = int(input("Introduce un número entero, por favor: "))
multi = 1
num = 0

while multi < 11 and num < 40:
    num = numero * multi
    print(num)
    multi += 1

print("Fin del programa. ")