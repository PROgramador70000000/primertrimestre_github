#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

notas = int(input("¿Cuántas notas vas a introducir? "))

for i in range(1, notas + 1):
    nota = float(input(f"Introduce la nota {i}: "))
    if nota < 5:
        print(f"La nota {i} está suspendida con un {nota}. ")
    elif nota >= 5:
        print(f"La nota {i} está aprobada con un {nota}. ¡Felicidades! ")
        