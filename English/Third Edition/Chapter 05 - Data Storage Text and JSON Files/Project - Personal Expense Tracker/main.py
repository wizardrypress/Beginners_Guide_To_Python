# Personal Expense Tracker

import json
from pathlib import Path


EXPENSES_FILE = Path("expenses.json")


def load_expenses():
    if not EXPENSES_FILE.exists():
        return []

    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("The expense file is empty or damaged. Starting a new list.")
        return []


def save_expenses(expenses):
    with open(EXPENSES_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def ask_amount():
    while True:
        try:
            amount = float(input("Expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_expense(expenses):
    date = input("Expense date (YYYY-MM-DD): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = ask_amount()

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses have been recorded yet.")
        return

    print("\nRecorded expenses:")
    print("-" * 60)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['date']} | "
            f"{expense['category']} | "
            f"${expense['amount']:.2f}"
        )
        print(f"   {expense['description']}")

    print("-" * 60)


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: ${total:.2f}")


def show_menu():
    print("""
Personal Expense Tracker

1. Add expense
2. View expenses
3. View total
4. Exit
""")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
