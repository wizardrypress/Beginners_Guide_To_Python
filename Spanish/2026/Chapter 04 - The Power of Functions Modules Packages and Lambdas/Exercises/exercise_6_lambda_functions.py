# Exercise 6: Lambda Functions

data = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # [(3, 'a'), (1, 'b'), (2, 'c')]
