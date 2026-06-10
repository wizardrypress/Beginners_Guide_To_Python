# Exercise 6: While loop practice
# while loop se ek string ko reverse karo.

original_text = "hello"
reversed_text = ""
index = len(original_text) - 1

while index >= 0:
    reversed_text += original_text[index]
    index -= 1

print(reversed_text)
