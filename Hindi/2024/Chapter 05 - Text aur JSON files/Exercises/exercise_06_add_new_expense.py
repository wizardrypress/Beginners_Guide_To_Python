# Exercise 6: JSON file me naya expense add karna

import json


def add_expense(file_path, new_expense):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    except json.JSONDecodeError:
        print("JSON file decode nahi ho paayi.")
        expenses = []
    except Exception as error:
        print(f"Unexpected error aaya: {error}")
        return

    expenses.append(new_expense)

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f"Error aaya: {error}")


new_expense = {
    "date": "2024-05-27",
    "amount": 75.20,
    "category": "Entertainment",
    "description": "Movie tickets",
}

add_expense("expenses.json", new_expense)
