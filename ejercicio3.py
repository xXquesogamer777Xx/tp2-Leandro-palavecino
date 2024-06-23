
fácil 

nombre_personaje = input("Ingrese el nombre de su personaje: ")
num_pociones = int(input("Ingrese el número de pociones mágicas que posee: "))

print(f"{nombre_personaje} tiene {num_pociones} pociones mágicas.")


intermedio 

potencia_hechizo = float(input("Ingrese la potencia del hechizo: "))
resistencia_enemigo = float(input("Ingrese el nivel de resistencia del enemigo: "))


if potencia_hechizo > resistencia_enemigo:
    print("El hechizo es lo suficientemente fuerte para derrotar al enemigo.")
else:
    print("El hechizo no es lo suficientemente fuerte para derrotar al enemigo.")


difícil




n = int(input("Ingrese el número total de personajes: "))
k = int(input("Ingrese el tamaño del equipo: "))


def combinaciones(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


print(f"El número total de combinaciones posibles de equipos de {k} personajes de un grupo de {n} personajes es: {int(combinaciones(n, k))}")