#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10

notas = int(input("¿Cuántas notas vas a introducir? "))

for i in range(1, notas + 1):
    nota = float(input(f"Introduce la nota {i}: "))
    
    if nota <= 10 and nota >= 0:
        if nota < 5:
            print(f"La nota {i} está suspendida con un {nota}. ")
        elif nota >= 5:
            print(f"La nota {i} está aprobada con un {nota}. ¡Felicidades! ")
    else:
        print("La nota no está entre 1 y 10. ")