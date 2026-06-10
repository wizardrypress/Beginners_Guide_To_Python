# Exercise 3: Appending to a Text File

def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")

append_to_file('journal.txt', '2024-05-26: Practiced writing and reading files.\n')
