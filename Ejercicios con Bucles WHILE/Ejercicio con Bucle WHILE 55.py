#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

total = 0
repeticiones = 0

while total < 50 or total % 2 == 0:
    repeticiones += 1

    primero = int(input("Introduce el primer número entero: "))
    segundo = int(input("Introduce el segundo número entero: "))
    suma = segundo + primero

    total += suma

    print(f"La suma de {primero} y {segundo} es {suma}. ")
    
    if repeticiones == 1:
        print(f"El total acumulado es de {total} y llevas {repeticiones} repetición realizada. ")
    else:
        print(f"El total acumulado es de {total} y llevas {repeticiones} repeticiones realizadas. ")

print("El total ya suma 50; fin del programa. ")