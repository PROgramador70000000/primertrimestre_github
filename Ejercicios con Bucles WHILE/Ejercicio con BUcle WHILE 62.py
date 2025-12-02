#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.

prim = int(input("Introduce el primer número: "))
seg = int(input("Introduce el segundo número: "))
salidapar = ""
salidaimpar = ""
numeropar = 1
numeroimpar = 1

if prim < seg:
    primero = prim
    segundo = seg
elif prim > seg:
    primero = seg
    segundo = prim
elif prim == seg:
    print("Los dos números son iguales. ¡Vuelve a intentarlo! ")
    exit()

for i in range(primero, segundo + 1):
    if i % 2 == 0:
        if numeropar == 1:
            principiopar = str(i)
        else:
            salidapar = salidapar + ("-" + str(i))
        numeropar += 1
    elif i % 2 != 0:
        if numeroimpar == 1:
            principioimpar = str(i)
        else:
            salidaimpar = salidaimpar + ("-" + str(i))
        numeroimpar += 1

salidapar = principiopar + salidapar
salidaimpar = principioimpar + salidaimpar

print(f"Los números pares son {salidapar}")
print(f"Los números impares son {salidaimpar}")