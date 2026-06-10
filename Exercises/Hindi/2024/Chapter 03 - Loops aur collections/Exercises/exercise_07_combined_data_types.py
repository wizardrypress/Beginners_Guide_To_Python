# Exercise 7: Combined data types
# Dictionaries ki ek list banao. Har dictionary ek student ko dikhati hai.

students = [
    {"name": "Asha", "grade": 90},
    {"name": "Ravi", "grade": 85},
    {"name": "Meera", "grade": 95},
]

# Har student ka naam aur grade print karo.
for student in students:
    print(
        f"Name: {student['name']}, "
        f"Grade: {student['grade']}"
    )
