# Exercise 3: Dictionary operations
# Ek book ke baare me dictionary banao.

book_info = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
}

# Genre add karo aur year update karo.
book_info["genre"] = "Dystopian"
book_info["year"] = 1950

# Saari keys aur values print karo.
for key, value in book_info.items():
    print(f"{key}: {value}")
