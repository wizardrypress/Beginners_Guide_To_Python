# Ejercicio 5: Usar abstracción

from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.largo + self.ancho)


# Crear instancias y llamar métodos.
circulo = Circulo(5)
rectangulo = Rectangulo(4, 7)

print(
    f"Área del círculo: {circulo.calcular_area():.2f}, "
    f"Perímetro: {circulo.calcular_perimetro():.2f}"
)

print(
    f"Área del rectángulo: {rectangulo.calcular_area():.2f}, "
    f"Perímetro: {rectangulo.calcular_perimetro():.2f}"
)
