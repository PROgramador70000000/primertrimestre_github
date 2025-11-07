#41. Imprime el siguiente patrón utilizando for:

num = 6
#Prueba a cambiar num. ¡El código sigue funcionando!
salida = ""

for i in range(1, num):
    for i in range(1, num):
        salida = salida + f"{i}"
    print(salida)
    num -= 1
    salida = ""