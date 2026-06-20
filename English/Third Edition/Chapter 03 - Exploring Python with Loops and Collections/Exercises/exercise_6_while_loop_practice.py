# Exercise 6: While Loop Practice
# Write a while loop to reverse a string

original_string = "hello"
reversed_string = ""
index = len(original_string) - 1

while index >= 0:
    reversed_string += original_string[index]
    index -= 1

print(reversed_string)  # Output: 'olleh'
