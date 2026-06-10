first_shelf = [
    "Bilkul Beginners ke liye Python Programming Guide",
    "The Blue Umbrella",
    "Malgudi Days",
    "Frankenstein",
    "The Guide",
]

print(first_shelf[3])  # Output: Frankenstein

second_shelf = [
    "The Adventures of Huckleberry Finn",
    "Little Women",
    "Sense and Sensibility",
]

third_shelf = [
    "Les Miserables",
    "The Jungle",
    "Persuasion",
    "The Secret Garden",
    "The Wind in the Willows",
    "The Metamorphosis",
    "Dubliners",
    "Beyond Good and Evil",
]

bookcase = [first_shelf, second_shelf, third_shelf]

print(bookcase[2][3])  # Output: The Secret Garden

# Nayi book add karni hai.
new_book = "The Great Gatsby"

# Nayi book ko second shelf me add karo.
bookcase[1].append(new_book)

print(f"Updated second shelf: {bookcase[1]}")

# Bookcase ki har shelf par loop chalana.
for shelf_number, shelf in enumerate(bookcase, start=1):
    print(f"Shelf {shelf_number} me ye books hain:")

    # Current shelf ki har book print karna.
    for book in shelf:
        print(f" - {book}")

    print()
