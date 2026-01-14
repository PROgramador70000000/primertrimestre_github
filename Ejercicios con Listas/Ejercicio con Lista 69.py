#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.

veces = int(input("Cuántos números vas a introducir? "))
lista = []

for i in range(veces):
    numero = int(input(f"Introduce el número {i + 1}: "))
    lista.append(numero)

lista.sort()
print(lista)