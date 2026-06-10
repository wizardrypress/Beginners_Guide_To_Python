# Exercise 4: Reading from a JSON File

import json

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        print("The file was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_json('expenses.json')
