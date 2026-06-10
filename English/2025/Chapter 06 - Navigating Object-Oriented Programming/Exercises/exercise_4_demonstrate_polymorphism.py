# Exercise 4: Demonstrate Polymorphism

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

def display_book_details(book):
    book.display_details()

# Creating instances of Book and EBook
book1 = Book("1984", "George Orwell", 1949)
ebook1 = EBook("1984", "George Orwell", 1949, 2)

# Demonstrating polymorphism
display_book_details(book1)
display_book_details(ebook1)
