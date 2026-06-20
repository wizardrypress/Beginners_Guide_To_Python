primer_estante = [
    "Guía Absoluta para Principiantes: Programación en Python",
    "Cien años de soledad",
    "Don Quijote de la Mancha",
    "Frankenstein",
    "Como agua para chocolate",
]

print(primer_estante[3])  # Salida: Frankenstein

segundo_estante = [
    "Las aventuras de Huckleberry Finn",
    "Mujercitas",
    "Sentido y sensibilidad",
]

tercer_estante = [
    "Los miserables",
    "La jungla",
    "Persuasión",
    "El jardín secreto",
    "El viento en los sauces",
    "La metamorfosis",
    "Dublineses",
    "Más allá del bien y del mal",
]

estanteria = [primer_estante, segundo_estante, tercer_estante]

print(estanteria[2][3])  # Salida: El jardín secreto

# Nuevo libro a añadir.
nuevo_libro = "El Gran Gatsby"

# Añade el nuevo libro al segundo estante.
estanteria[1].append(nuevo_libro)

print(f"Segundo estante actualizado: {estanteria[1]}")

# Iterar sobre cada estante de la estantería.
for numero_estante, estante in enumerate(estanteria, start=1):
    print(f"La estantería {numero_estante} contiene:")

    # Iterar sobre cada libro del estante.
    for libro in estante:
        print(f" - {libro}")

    print()
