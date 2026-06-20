# Exercise 5: For Loop Practice
# Write a for loop to print the first 10 numbers in the Fibonacci sequence

a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b
