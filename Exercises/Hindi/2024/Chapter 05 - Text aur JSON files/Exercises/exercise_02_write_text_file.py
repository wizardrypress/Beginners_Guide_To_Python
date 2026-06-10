# Exercise 2: Text file me write karna


def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as error:
        print(f"Error aaya: {error}")


write_file(
    "diary.txt",
    "2024-05-25: Aaj maine Python me file handling seekhi.\n",
)
