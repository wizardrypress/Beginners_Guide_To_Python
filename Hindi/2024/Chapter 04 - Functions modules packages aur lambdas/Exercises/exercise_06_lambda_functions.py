# Exercise 6: Lambda functions
# Tuples ki list ko har tuple ke second item ke basis par sort karo.

data = [(1, "b"), (3, "a"), (2, "c")]

sorted_data = sorted(data, key=lambda item: item[1])

print(sorted_data)
