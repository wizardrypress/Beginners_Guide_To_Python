# Exercise 3: Dictionary Operations
# Create a dictionary with information about a book

book_info = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
}

# Add a key for genre and update the year
book_info["genre"] = "Dystopian"
book_info["year"] = 1950

# Print all keys and values
for key, value in book_info.items():
    print(f"{key}: {value}")
