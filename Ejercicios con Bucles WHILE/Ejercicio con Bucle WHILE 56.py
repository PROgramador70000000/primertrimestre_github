#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.

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

while respuesta == "s":
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