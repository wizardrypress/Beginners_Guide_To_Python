# Exercise 5: Writing to a JSON File

import json

expenses = [
    {"date": "2024-05-25", "amount": 50.75, "category": "Grocery", "description": "Weekly groceries"},
    {"date": "2024-05-26", "amount": 120.00, "category": "Utilities", "description": "Electricity bill"}
]

def write_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")

write_json('expenses.json', expenses)
