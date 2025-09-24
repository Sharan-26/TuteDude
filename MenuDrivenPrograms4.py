#Create a library system that keeps track of books, borrowers, and availability. Allow borrowing, returning, and viewing available books.

#Include due dates, penalties for late returns, and unique IDs for books and users.
#Focus on class relationships and method responsibilities.

import datetime
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrower_id = None
        self.due_date = None

    def borrow(self, borrower_id):
        if self.is_available:
            self.is_available = False # Mark the book as borrowed
            self.borrower_id = borrower_id # Assign the borrower ID
            self.due_date = datetime.datetime.now() + datetime.timedelta(days=14)  # 2 weeks from now
            return True # Successfully borrowed
        return False # Book is not available

    def return_book(self):
        if not self.is_available: # Only return if the book is currently borrowed
            self.is_available = True # Mark the book as available
            self.borrower_id = None # Clear borrower ID
            self.due_date = None # Clear due date
            return True # Successfully returned
        return False # Book was not borrowed

    def is_overdue(self):
        if not self.is_available and datetime.datetime.now() > self.due_date: # Check if the book is overdue
            return True # Overdue
        return False # Not overdue

    def __str__(self): # String representation of the book
        status = "Available" if self.is_available else f"Borrowed by {self.borrower_id}, Due on {self.due_date.strftime('%Y-%m-%d')}"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"
    
class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}

    def add_book(self, book: Book): # Add a new book to the library
        self.books[book.book_id] = book # Add book to the collection

    def register_borrower(self, borrower_id, name): # Register a new borrower
        self.borrowers[borrower_id] = name # Add borrower to the registry

    def borrow_book(self, book_id, borrower_id):
        if book_id in self.books and borrower_id in self.borrowers:
            if self.books[book_id].borrow(borrower_id):
                print(f"Book '{self.books[book_id].title}' borrowed successfully by {self.borrowers[borrower_id]}.")
            else:
                print(f"Book '{self.books[book_id].title}' is currently unavailable.")
        else:
            print("Invalid book ID or borrower ID.")

    def return_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id].return_book():
                print(f"Book '{self.books[book_id].title}' returned successfully.")
            else:
                print(f"Book '{self.books[book_id].title}' was not borrowed.")
        else:
            print("Invalid book ID.")

    def view_available_books(self):
        print("Available Books:")
        for book in self.books.values():
            if book.is_available:
                print(book)

    def view_all_books(self):
        print("All Books:")
        for book in self.books.values():
            print(book)
            
# Example usage
library = Library()
library.add_book(Book(1, "1984", "George Orwell"))
library.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee"))
library.register_borrower(101, "Alice")
library.register_borrower(102, "Bob")
library.view_available_books()
library.borrow_book(1, 101)
library.view_available_books()
# library.view_all_books()
# library.return_book(1)
# library.view_available_books()

