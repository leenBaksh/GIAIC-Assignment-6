""" 
    Assignment 11:
    Create a class Book with a class variable total_books. 
    Add a class method increment_book_count() to increase the count when a new book is added.

"""

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")

book1 = Book()
book2 = Book()

book1.increment_book_count()
book2.increment_book_count()