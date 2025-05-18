"""
Create a class Book with a class variable total_books.
Add a class method increment_book_count() to increase 
the count when a new book is added.
"""

# This code defines a class Book with a class variable total_books.
class Book():
    total_books = 0
    
    # The __init__ method initializes the title and author of the book.
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
        print(f"Book '{self.title}' by {self.author} added.")
    
    # The class method increment_book_count() increases the total_books count.    
    @classmethod
    # This method is called when a new book is added.
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books: {cls.total_books}")
        

new_book1 = Book("To Kill a Mockingbird", "Harper Lee")
new_book2 = Book("1984", "George Orwell")
new_book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Print the total number of books after adding new books.
print(f"Total books after adding '{new_book1.title}': {Book.total_books}")        
        