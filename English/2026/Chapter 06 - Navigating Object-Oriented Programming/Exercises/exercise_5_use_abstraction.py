# Exercise 5: Use Abstraction

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

# Creating instances and calling methods
circle = Circle(5)
rectangle = Rectangle(4, 7)

print(f"Circle Area: {circle.calculate_area()}, Perimeter: {circle.calculate_perimeter()}")
print(f"Rectangle Area: {rectangle.calculate_area()}, Perimeter: {rectangle.calculate_perimeter()}")
