# Exercise 5: Abstraction use karna

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Objects banao aur methods call karo.
circle = Circle(5)
rectangle = Rectangle(4, 7)

print(
    f"Circle area: {circle.calculate_area():.2f}, "
    f"Perimeter: {circle.calculate_perimeter():.2f}"
)

print(
    f"Rectangle area: {rectangle.calculate_area():.2f}, "
    f"Perimeter: {rectangle.calculate_perimeter():.2f}"
)
