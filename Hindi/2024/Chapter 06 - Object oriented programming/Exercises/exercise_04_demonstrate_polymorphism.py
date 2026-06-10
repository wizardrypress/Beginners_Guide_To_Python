# Exercise 4: Polymorphism dikhana


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")


class Ebook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def show_details(self):
        print(
            f"Title: {self.title}, Author: {self.author}, "
            f"Year: {self.year}, File size: {self.file_size} MB"
        )


def show_book_details(book):
    book.show_details()


# Book aur Ebook objects banana.
book_1 = Book("1984", "George Orwell", 1949)
ebook_1 = Ebook("1984", "George Orwell", 1949, 2)

# Polymorphism dikhana.
show_book_details(book_1)
show_book_details(ebook_1)
