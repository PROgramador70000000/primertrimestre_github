#86. Realiza el ejercicio del DNI que encontrarás en el Sway

letras = "TRWAGMYFPDXBNJZSQVHLCKE"
respuesta = "s"
lista_intentos = []
correctos = []
incorrectos = []

while respuesta == "s":

    numeros = input("Introduce los números de tu DNI: ")
    valido = 1
    if not len(numeros) == 8:
        print("La longitud del DNI introducido no es correcta. ¡Vuelve a intentarlo! ")
        valido = 0
        lista_intentos.append(0)
        incorrectos.append(numeros)

    if not numeros.isdigit():
        print("Tus números del DNI no son completamente numéricos. Comprueba cualquier error. ")
        valido = 0
        lista_intentos.append(1)
        incorrectos.append(numeros)
    
    if not int(numeros) % 23 < 23:
        print("El número del DNI no es válido. ¡Vuelve a intentarlo! ")
        valido = 0
        lista_intentos.append(2)
        incorrectos.append(numeros)

    if valido == 1:
        lista_intentos.append(3)
        letra = letras[int(numeros) % 23]
        DNI = f"{numeros}-{letra}"
        print(f"Tu DNI completo es {DNI}")
        correctos.append(numeros)

    respuesta = input("¿Quieres introducir otro DNI? (s/n): ")

correctos = correctos.sort()
incorrectos = incorrectos.sort(reverse = True)
porcentaje_correctos = (len(correctos) / len(lista_intentos)) * 100
porcentaje_incorrectos = (len(incorrectos) / len(lista_intentos)) * 100
porcentaje_longitud = (lista_intentos.count(0) / len(lista_intentos)) * 100
porcentaje_numérico = (lista_intentos.count(1) / len(lista_intentos)) * 100
porcentaje_error = (lista_intentos.count(2) / len(lista_intentos)) * 100

print("-------- RESUMEN --------")
print("-------------------------")
print("DNIs correctos: ")
print(correctos)
print("DNIs incorrectos: ")
print(incorrectos)
print(f"Has introducido {len(incorrectos)} DNIs incorrectos. ")
print(f"Y {len(correctos)} DNIs correctos. ")
print(f"Has introducido un {porcentaje_correctos}% de DNIs correctos. ")
print(f"Un {porcentaje_incorrectos}% de DNIs incorrectos. ")
print(f"Un {porcentaje_longitud}% de errores de longitud. ")
print(f"Un {porcentaje_numérico}% de errores de formato (no has introducido solo números). ")
print(f"Y un {porcentaje_error}% de errores de resto (el número no es correcto). ")