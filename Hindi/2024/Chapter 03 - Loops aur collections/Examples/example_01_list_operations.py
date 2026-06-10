# List banana.
fruits = ["apple", "banana", "cherry"]

# List ke items ko index se access karna.
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# List me naye items add karna.
fruits.append("orange")
fruits.insert(1, "blueberry")

# List se items hatana.
fruits.remove("banana")
returned_fruit = fruits.pop()

# List ke item ko badalna.
fruits[0] = "kiwi"

print(fruits)
print("Wapas aaya fruit:", returned_fruit)
