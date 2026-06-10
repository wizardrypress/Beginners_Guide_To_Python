# Exercise 3: Inheritance implement karna


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


# Ebook objects banana.
ebook_1 = Ebook("1984", "George Orwell", 1949, 2)
ebook_2 = Ebook("To Kill a Mockingbird", "Harper Lee", 1960, 1.5)

# Details dikhana.
ebook_1.show_details()
ebook_2.show_details()
