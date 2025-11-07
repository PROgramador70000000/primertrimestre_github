#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.

n = int(input("Introduce el número de números que vas a introducir (valga la redundancia): "))
positivos = 0
negativos = 0
ceros = 0

for i in range(1, n + 1):
    numero = int(input(f"Introduce el número {i}: "))
    if numero < 0:
        negativos += 1
    elif numero == 0:
        ceros += 1
    else:
        positivos += 1

print(f"Has introducido {positivos} números positivos, {negativos} números negativos y {ceros} ceros. ")