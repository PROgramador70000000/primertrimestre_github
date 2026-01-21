#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.

lista = []

while True:
    valor = input("Introduce un valor: ")
    lista = valor.split(".")
    if len(lista) == 2:
        if lista[0].isnumeric() and lista[1].isnumeric():
            print("Es un número con decimales. ")
        else:
            print("No es un número con decimales. ")
    else:
        print("No es un número con decimales")