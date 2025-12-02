#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while

numero = int(input("Introduce un número entero, por favor: "))
multi = 1

while multi < 11:
    print(numero * multi)
    multi += 1