# Enhanced expense tracker with OOP

import json
from pathlib import Path


EXPENSES_FILE = Path("expenses.json")


class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def to_dictionary(self):
        return {
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount,
        }

    @classmethod
    def from_dictionary(cls, data):
        return cls(
            data["date"],
            data["category"],
            data["description"],
            data["amount"],
        )


class ExpenseTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if not self.file_path.exists():
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Expense.from_dictionary(expense) for expense in data]
        except json.JSONDecodeError:
            print("Expense file khali ya damaged hai. Nayi list start ki ja rahi hai.")
            return []

    def save_expenses(self):
        data = [
            expense.to_dictionary()
            for expense in self.expenses
        ]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def show_expenses(self):
        if not self.expenses:
            print("Abhi koi expense recorded nahi hai.")
            return

        print("\nRecorded expenses:")
        print("-" * 60)

        for index, expense in enumerate(self.expenses, start=1):
            print(
                f"{index}. {expense.date} | "
                f"{expense.category} | "
                f"Rs {expense.amount:.2f}"
            )
            print(f"   {expense.description}")

        print("-" * 60)

    def show_total(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total spent: Rs {total:.2f}")


def ask_amount():
    while True:
        try:
            amount = float(input("Expense amount: "))

            if amount <= 0:
                print("Amount zero se bada hona chahiye.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Ek number enter karo.")


def create_expense_from_input():
    date = input("Expense date (YYYY-MM-DD): ")
    category = input("Category enter karo: ")
    description = input("Description: ")
    amount = ask_amount()

    return Expense(date, category, description, amount)


def show_menu():
    print("""
Personal expense tracker with OOP

1. Add expense
2. View expenses
3. View total
4. Exit
""")


def main():
    tracker = ExpenseTracker(EXPENSES_FILE)

    while True:
        show_menu()
        choice = input("Option choose karo: ")

        if choice == "1":
            expense = create_expense_from_input()
            tracker.add_expense(expense)
            print("Expense successfully add ho gaya.")
        elif choice == "2":
            tracker.show_expenses()
        elif choice == "3":
            tracker.show_total()
        elif choice == "4":
            print("Phir milenge.")
            break
        else:
            print("Invalid option. 1, 2, 3, ya 4 choose karo.")


if __name__ == "__main__":
    main()
