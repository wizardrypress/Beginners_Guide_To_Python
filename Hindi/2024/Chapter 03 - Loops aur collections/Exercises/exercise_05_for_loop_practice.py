# Exercise 5: For loop practice
# Fibonacci sequence ke pehle 10 numbers print karne ke liye for loop likho.

a, b = 0, 1

for _ in range(10):
    print(a)
    a, b = b, a + b
