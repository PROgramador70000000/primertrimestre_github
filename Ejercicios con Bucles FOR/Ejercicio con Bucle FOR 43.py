#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra

palabra = input("Introduce una palabra, por favor: ")

for i in range(len(palabra)):
    print(f"La posición {i} hay una {palabra[i]}")