#42. Imprima el siguiente patrón con el ciclo for. 

num_asteriscos = 1
num = 5
#Prueba a cambiar num. ¡El código sigue funcionando!
salida = ""
sube_baja = 1

for i in range(1, (2 * num)):
    for i in range(1, num_asteriscos + 1):
        salida = salida + "*"
    print(salida)
    salida = ""
    if num_asteriscos >= num and sube_baja == 1:
        sube_baja = -1
    num_asteriscos += 1 * sube_baja