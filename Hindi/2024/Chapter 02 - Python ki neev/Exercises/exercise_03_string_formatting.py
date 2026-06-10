# Exercise 03: String formatting

item_name = "Python book"
quantity = 3
price = 499.99

total = quantity * price

print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Price: Rs {price:.2f}")
print(f"Total: Rs {total:.2f}")

print()
print("Using format():")
print("Aapne {0} copies kharidi. Total: Rs {1:.2f}".format(quantity, total))
