# Exercise 3: Using standard modules
# Circle ka area calculate karne ke liye math module use karo.

import math


def calculate_circle_area(radius):
    return math.pi * (radius ** 2)


radius = float(input("Circle ka radius enter karo: "))
area = calculate_circle_area(radius)

print("Circle ka area hai: {:.2f}".format(area))
