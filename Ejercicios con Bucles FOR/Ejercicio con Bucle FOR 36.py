#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

n = int(input("Introduce cuantos de los primeros números naturales quieres que sume: "))
suma = 0

if n < 0:
    print("Por favor, introduce un número entero positivo. ")

for i in range(1, n + 1):
    suma += i

print(f"La suma de los primeros {n} números naturales es {suma}. ")