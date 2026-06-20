# Exercise 1: Reading from a Text File

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file('journal.txt')
