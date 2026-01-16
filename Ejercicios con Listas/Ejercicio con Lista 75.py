#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos

lista1 = ["a","b","D","x","r","X","3","h","w","2","i"]
num_valores = len(lista1)
num_numeros = 0
num_letras = 0
num_mayusculas = 0
suma = 0

for i in range(len(lista1)):
    if lista1[i].isnumeric():
        num_numeros += 1
        suma += int(lista1[i])
    if lista1[i].isalpha():
        num_letras += 1
        if lista1[i].isupper():
            num_mayusculas += 1

print(f"Número de valores: {num_valores}")
print(f"Cantidad de números: {num_numeros}")
print(f"Cantidad de letras: {num_letras}")
print(f"Cantidad de mayúsculas: {num_mayusculas}")
print(f"Suma total de números: {suma}")