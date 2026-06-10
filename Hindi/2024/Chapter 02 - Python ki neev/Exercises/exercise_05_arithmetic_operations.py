# Exercise 05: Arithmetic operations

first_number = float(input("Pehla number enter karein: "))
second_number = float(input("Doosra number enter karein: "))

print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")

if second_number != 0:
    print(f"Division: {first_number / second_number}")
else:
    print("Division possible nahi hai kyunki doosra number zero hai.")

print(f"Exponentiation: {first_number ** second_number}")
