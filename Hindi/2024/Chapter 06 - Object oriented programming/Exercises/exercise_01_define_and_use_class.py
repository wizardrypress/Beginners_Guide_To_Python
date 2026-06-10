# Exercise 1: Class define aur use karna


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")


# Objects banana.
book_1 = Book("1984", "George Orwell", 1949)
book_2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Details dikhana.
book_1.show_details()
book_2.show_details()
