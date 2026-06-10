# Exercise 4: JSON file read karna

import json


def read_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        print("File nahi mili.")
    except json.JSONDecodeError:
        print("JSON file decode nahi ho paayi.")
    except Exception as error:
        print(f"Unexpected error aaya: {error}")


read_json("expenses.json")
