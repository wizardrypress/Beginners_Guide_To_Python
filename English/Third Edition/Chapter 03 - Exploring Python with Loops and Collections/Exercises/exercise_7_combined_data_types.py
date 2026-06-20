# Exercise 7: Combined Data Types
# Create a list of dictionaries, each representing a student with name and grade

students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 95}
]

# Print each student's name and grade using a loop
for student in students:
    print(f"Name: {student['name']}, Grade: {student['grade']}")
