#41. Imprime el siguiente patrón utilizando for:

num = 6
max_num = num
#Prueba a cambiar num. ¡El código sigue funcionando!
salida = ""

for x in range(1, num):
    for i in range(1, num):
        i = (max_num - i) - (x - 1)
        salida = salida + f"{i}"
    print(salida)
    num -= 1
    salida = ""