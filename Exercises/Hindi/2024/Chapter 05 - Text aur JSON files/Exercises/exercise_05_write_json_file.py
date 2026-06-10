# Exercise 5: JSON file me write karna

import json


expenses = [
    {
        "date": "2024-05-25",
        "amount": 50.75,
        "category": "Groceries",
        "description": "Weekly shopping",
    },
    {
        "date": "2024-05-26",
        "amount": 120.00,
        "category": "Utilities",
        "description": "Electricity bill",
    },
]


def write_json(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f"Error aaya: {error}")


write_json("expenses.json", expenses)
