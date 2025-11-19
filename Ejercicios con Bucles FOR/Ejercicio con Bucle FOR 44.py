#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’

num = 100
salida = ""

for i in range(3, num + 1, 3):
    salida = salida + (", " + f"{i}")

print("0" + salida)