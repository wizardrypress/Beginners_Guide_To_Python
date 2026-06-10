# Exercise 6: Adding a New Expense to a JSON File

import json

def add_expense(file_path, new_expense):
    try:
        with open(file_path, 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        expenses = []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    expenses.append(new_expense)

    try:
        with open(file_path, 'w') as file:
            json.dump(expenses, file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")

new_expense = {"date": "2024-05-27", "amount": 75.20, "category": "Entertainment", "description": "Concert tickets"}
add_expense('expenses.json', new_expense)
