# Ejercicio 7: Tipos de datos combinados
# Crea una lista de diccionarios. Cada diccionario representa
# a un estudiante con su nombre y calificación.

estudiantes = [
    {"nombre": "Alicia", "calificacion": 90},
    {"nombre": "Roberto", "calificacion": 85},
    {"nombre": "Carlos", "calificacion": 95},
]

# Imprime el nombre y la calificación de cada estudiante.
for estudiante in estudiantes:
    print(
        f"Nombre: {estudiante['nombre']}, "
        f"Calificación: {estudiante['calificacion']}"
    )
