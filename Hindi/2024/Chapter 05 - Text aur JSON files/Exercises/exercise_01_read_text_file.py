# Exercise 1: Text file read karna


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File nahi mili.")
    except PermissionError:
        print("Is file ko read karne ki permission nahi hai.")
    except Exception as error:
        print(f"Unexpected error aaya: {error}")


read_file("diary.txt")
