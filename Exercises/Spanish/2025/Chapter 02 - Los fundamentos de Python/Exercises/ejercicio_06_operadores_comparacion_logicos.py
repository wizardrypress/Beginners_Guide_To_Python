# Ejercicio 6: Operadores de comparación y operadores lógicos
# Determina la categoría de edad de una persona.

edad = int(input("Ingresa tu edad: "))

if edad < 13:
    print("Eres un niño.")
elif edad >= 13 and edad < 18:
    print("Eres un adolescente.")
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")
else:
    print("Eres una persona mayor.")
