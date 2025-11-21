#56b.Opcional. Haz alguna o todas las mejoras en el programa anterior que a continuación se indican:
#- Cuando se pregunta “si desea realizar otro pedido”, el encargado puede introducir s ó n en mayúscula o minúscula.
#- Si el encargado introduce otro valor distinto a S o N, el programa debe repetir la pregunta e informar de que ha introducido un valor equivocado.
#- El lugar de almacenar los precios en variables, utiliza una biblioteca (busca información) e investiga como moverte por los índices.
#- Un pedido puede estar formado por 3, 2 o 1 componentes. Ej. Un usuario puede pedir únicamente una bebida.

pedidos = 0
total = 0
total_iva = 0
total_descuento = 0
respuesta = "s"

print("BIENVENIDO A BAR PEPERETE")
print("Puedes pedir menús que incluyen bocadillo, acompañamiento y bebida. ")
print("")
print("BOCADILLOS")
print("1. Bocadillo de calamares - 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("")
print("ACOMPAÑAMIENTOS")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Aquarius - 1.5 €")
print("3. Agua - 1 €")

while respuesta in "sS":
    pedidos += 1

    bocadillo = int(input(f"Introduce el bocadillo para el menú {pedidos} (introduce el número): "))
    acompañamiento = int(input(f"Introduce el acompañamiento para el menú {pedidos}: "))
    bebida = int(input(f"Introduce la bebida para el menú {pedidos}: "))

    if bocadillo == 1:
        total += 9
    elif bocadillo == 2:
        total += 4.5
    elif bocadillo == 3:
        total += 2.5
    else:
        print(f"En el pedido {pedidos} has seleccionado un número de bocadillo inexistente")

    if acompañamiento == 1:
        total += 1.5
    elif acompañamiento == 2:
        total += 1.75
    elif acompañamiento == 3:
        total += 2
    else:
        print(f"En el pedido {pedidos} has seleccionado un número de acompañamiento inexistente. ")

    if bebida == 1:
        total += 2
    elif bebida == 2:
        total += 1.5
    elif bebida == 3:
        total += 1
    else:
        print(f"En el pedido {pedidos} has seleccionado un número de bebida inexistente. ")

    respuesta = input("¿Quieres hacer otro pedido? (s/n): ")

    if not respuesta in "snSN":
        while not respuesta in "snSN":
            respuesta = input("La respuesta no es un valor aceptado. Por favor, vuelve a intentarlo: ")

total_iva = ((total / 100) * 10) + total

print(f"Número de pedidos: {pedidos}")
print(f"Total a pagar: {total}")
print(f"Total con IVA: {total_iva}")

if total_iva >= 20 and total_iva <= 30:
    total_descuento = total_iva - ((total_iva / 100) * 5)
    print(f"Precio total con descuento del 5%: {total_descuento}")
elif total_iva > 30:
    total_descuento = total_iva - ((total_iva / 100) * 15)
    print(f"Precio total con descuento del 15%: {total_descuento}")