#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir

lista1 = ["a","b","D","x","r","X","3","h","w","2","i"]
respuesta = "s"

while respuesta == "s":
    eliminar = input("Introduce el valor que quieres eliminar (solo se aceptan números): ")
    if not len(eliminar) == 1:
        print("Introduce solo un valor, por favor. ")
        respuesta = input("Quieres eliminar otro valor? (s/n): ")
    if not eliminar.isnumeric():
        print("Introduce un número, por favor. ")
        respuesta = input("Quieres eliminar otro valor? (s/n): ")
    else:
        esta = 0
        for i in range(len(lista1) - 1):
            if lista1[i] == eliminar:
                lista1.pop(i)
                esta = 1
        if esta == 0:
            print(f"El {eliminar} no está en la lista. ") 
        respuesta = input("Quieres eliminar otro valor? (s/n): ")
    if not respuesta in "sn":
        while not respuesta in "sn":
            print("La respuesta no es correcta. ")
            respuesta = input("Quieres eliminar otro valor? (s/n): ")

print(f"Lista final: {lista1}")