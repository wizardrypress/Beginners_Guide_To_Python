# Exercise 2: Composition use karna


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.show_details()


# Book objects banana.
book_1 = Book("1984", "George Orwell", 1949)
book_2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Library object banao aur books add karo.
library = Library()
library.add_book(book_1)
library.add_book(book_2)

# Library ki saari books dikhana.
library.show_books()
