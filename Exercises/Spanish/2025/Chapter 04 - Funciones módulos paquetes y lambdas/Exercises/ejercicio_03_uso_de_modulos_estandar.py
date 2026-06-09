# Ejercicio 3: Uso de módulos estándar
# Usa el módulo math para calcular el área de un círculo.

import math


def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)


radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)

print("El área del círculo es: {:.2f}".format(area))
