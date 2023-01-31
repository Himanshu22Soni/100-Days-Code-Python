# Exercise 06 Library Management System.

class Library:
    def __init__(self, no_of_books, books):
        self.books = books
        self.no_of_books = no_of_books

    def add_book(self, book_name):
        if len(self.books) == self.no_of_books:
            self.books.append(book_name)
            self.no_of_books += 1
        else:
            print("Mismatch error.No function is allowed to call.")

    def remove_book(self, book_name):
        if len(self.books) == self.no_of_books:
            self.books.remove(book_name)
            self.no_of_books -= 1
        else:
            print("Mismatch error.No function is allowed to call.")

    def get_books(self):
        if len(self.books) == self.no_of_books:
            for book in self.books:
                print(book, end=" ")
            print("\n")
        else:
            print("Mismatch error.No function is allowed to call.")

    def number_of_books(self):
        if len(self.books) == self.no_of_books:
            print(f"Length of Library is {len(self.books)}")
        else:
            print("Mismatch error.No function is allowed to call.")


lis = []
n = int(input("Enter no. of books: "))
for i in range(n):
    book = input(f"Enter {i+1} book: ")
    lis.append(book)
lib1 = Library(n, lis)
lib1.get_books()
lib1.add_book("Socio")
lib1.remove_book("Arts")
lib1.get_books()
