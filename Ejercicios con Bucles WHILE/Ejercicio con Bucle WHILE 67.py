#67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes consideraciones:
#Debe tener una longitud entre 6 y 8 caracteres.
#Debe contener como mínimo:
#2 números mayores o iguales que 1 y menor o igual que 5
#2 letras minúsculas
#1 letra mayúscula
#2 símbolos (*, _, @, &,/,#)
#1 número mayor o igual que 6 y menor o igual que 5

print("CONTRASEÑA SEGURA - JUEGO")
print("Para este ejercicio, vas a tener que introducir una contraseña segura. ")
print("----------------------------------------------------------------------")
print("LAS CONDICIONES SON:")
print("1. La contraseña debe tener entre 6 y 8 carácteres. ")
print("2. Debe tener dos números mayores o iguales que 1 y menores o iguales que 5. ")
print("3. Debe tener dos letras minúsculas. ")
print("4. Debe tener una letra mayúscula. ")
print("5. Debe tener dos símbolos de estos: *, _, @, &, /, #. ")
print("6. Debe tener un número mayor o igual que 6 y menor o igual que 5. ")

contraseña = input("Introduce tu contraseña: ")
condicion1 = 0
condicion2 = 0
condicion3 = 0
condicion4 = 0
condicion5 = 0

if not len(contraseña) >= 6 and len(contraseña) <= 8:
    print(f"La longitud de tu contraseña es de {len(contraseña)}, así que no cumple con los requisitos. ¡Vuelve a intentarlo! ")
    exit()

for i in range(5):
    for j in range(len(contraseña)):
        if i == 1:
            if contraseña[j] <= 5 and contraseña[j] >= 1:
                condicion1 += 1
        if i == 2: 
            if contraseña[j].islower:
                condicion2 += 1
        if i == 3:
            if contraseña[j].isupper:
                condicion3 += 1
        if i == 4:
            if contraseña[j] in "*_@&/#":
                condicion4 += 1
        if i == 5:
            if contraseña[j] <= 5 or contraseña[j] >= 6:
                condicion5 +=1

if condicion1 == 2 and condicion2 == 2 and condicion3 == 1 and condicion4 == 2 and condicion5 == 1:
    print("¡Contraseña correcta! ")
else:
    print("Contraseña incorrecta. ")