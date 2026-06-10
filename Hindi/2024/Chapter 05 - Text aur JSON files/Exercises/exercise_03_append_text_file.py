# Exercise 3: Existing text file me append karna


def append_to_file(file_path, content):
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(content)
    except Exception as error:
        print(f"Error aaya: {error}")


append_to_file(
    "diary.txt",
    "2024-05-26: Aaj maine files read aur write karne ki practice ki.\n",
)
