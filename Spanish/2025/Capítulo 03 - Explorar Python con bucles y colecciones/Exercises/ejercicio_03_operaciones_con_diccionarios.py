# Ejercicio 3: Operaciones con diccionarios
# Crea un diccionario con información sobre un libro.

informacion_libro = {
    "titulo": "1984",
    "autor": "George Orwell",
    "anio": 1949,
}

# Agrega una clave para el género y actualiza el año.
informacion_libro["genero"] = "Distopía"
informacion_libro["anio"] = 1950

# Imprime todas las claves y valores.
for clave, valor in informacion_libro.items():
    print(f"{clave}: {valor}")
