# Exercise 2: Use Composition

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display_details()

# Creating instances of Book
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Creating an instance of Library and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)

# Displaying all books in the library
library.display_books()
