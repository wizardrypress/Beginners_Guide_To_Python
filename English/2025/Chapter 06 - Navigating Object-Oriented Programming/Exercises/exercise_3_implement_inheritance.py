# Exercise 3: Implement Inheritance

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, File Size: {self.file_size}MB")

# Creating instances of EBook
ebook1 = EBook("1984", "George Orwell", 1949, 2)
ebook2 = EBook("To Kill a Mockingbird", "Harper Lee", 1960, 1.5)

# Displaying details
ebook1.display_details()
ebook2.display_details()
