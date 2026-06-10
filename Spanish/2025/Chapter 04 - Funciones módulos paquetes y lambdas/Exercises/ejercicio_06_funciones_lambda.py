# Ejercicio 6: Funciones lambda
# Ordena una lista de tuplas usando el segundo elemento de cada tupla.

datos = [(1, "b"), (3, "a"), (2, "c")]

datos_ordenados = sorted(datos, key=lambda elemento: elemento[1])

print(datos_ordenados)
