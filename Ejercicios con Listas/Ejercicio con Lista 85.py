#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos

estudiantes = []
ingles = []
castellano = []
catalan = []
respuesta = "s"
no_estudiantes = 0

while respuesta == "s":
    no_estudiantes += 1
    estudiante = input(f"Introduce el nombre del alumno {no_estudiantes}: ")
    estudiantes.append(estudiante)
    nota_ingles = float(input(f"Nota inglés de {estudiantes[no_estudiantes - 1]}: "))
    nota_castellano = float(input(f"Nota castellano de {estudiantes[no_estudiantes - 1]}: "))
    nota_catalan = float(input(f"Nota catalán de {estudiantes[no_estudiantes - 1]}: "))
    ingles.append(nota_ingles)
    castellano.append(nota_castellano)
    catalan.append(nota_catalan)

    respuesta = input("¿Quieres introducir otro estudiante? (s/n): ")

media_ingles = format(sum(ingles) / len(ingles), ".2f")
media_castellano = format(sum(castellano) / len(castellano), ".2f")
media_catalan = format(sum(catalan) / len(catalan), ".2f")

if len(ingles) % 2 == 0:
    mediana_ingles = format((ingles[int(len(ingles) / 2) - 1] + (ingles[int((len(ingles) / 2))])) / 2, ".2f")
    mediana_castellano = format((castellano[int(len(castellano) / 2) - 1] + (castellano[int((len(ingles) / 2))])) / 2, ".2f")
    mediana_catalan = format((catalan[int(len(catalan) / 2) - 1] + (catalan[int((len(catalan) / 2))])) / 2, ".2f")
else:
    mediana_ingles = format(ingles[round(len(ingles) / 2) - 1], ".2f")
    mediana_castellano = format(castellano[round(len(castellano) / 2) - 1], ".2f")
    mediana_catalan = format(catalan[round(len(catalan) / 2) - 1], ".2f")

print(f"La media en inglés es {media_ingles}")
print(f"La media en castellano es {media_castellano}")
print(f"La media en catalán es {media_catalan}")
print(f"La mediana en inglés es {mediana_ingles}")
print(f"La mediana en castellano es {mediana_castellano}")
print(f"Y la mediana en catalán es {mediana_catalan}")