# Crear una lista.
frutas = ["manzana", "plátano", "cereza"]

# Acceder a los elementos de la lista.
print(frutas[0])  # Salida: manzana
print(frutas[1])  # Salida: plátano
print(frutas[2])  # Salida: cereza

# Añadir elementos a la lista.
frutas.append("naranja")
frutas.insert(1, "arándano")

# Eliminar elementos de la lista.
frutas.remove("plátano")
fruta_devuelta = frutas.pop()

# Modificar elementos de la lista.
frutas[0] = "kiwi"

print(frutas)
print("Fruta devuelta:", fruta_devuelta)
