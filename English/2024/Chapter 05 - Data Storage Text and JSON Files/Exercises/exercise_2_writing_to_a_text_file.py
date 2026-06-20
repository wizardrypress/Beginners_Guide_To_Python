# Exercise 2: Writing to a Text File

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")

write_to_file('journal.txt', '2024-05-25: Learned about file handling in Python.\n')
