"""
Integration Project Lab
=======================

Create a comprehensive library management system.
Complete the TODO sections below.
"""

from typing import List, Dict, Optional, Union
from datetime import datetime, timedelta

# TODO: Define type aliases
# BookId = str
# UserId = str
# ISBN = str

# TODO: Create Book class
class Book:
    def __init__(self, book_id, title: str, author: str, isbn, category: str):
        # TODO: Initialize book attributes
        pass

# TODO: Create User class
class User:
    def __init__(self, user_id, name: str, email: str):
        # TODO: Initialize user attributes
        pass

# TODO: Create Loan class
class Loan:
    def __init__(self, user_id, book_id, loan_date: datetime, due_date: datetime):
        # TODO: Initialize loan attributes
        pass

    def is_overdue(self) -> bool:
        """Check if loan is overdue."""
        # TODO: Check if current date > due_date
        pass

    def calculate_fine(self) -> float:
        """Calculate fine for overdue loan."""
        # TODO: Calculate fine based on days overdue
        pass

# TODO: Create Library class
class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.loans = []

    def add_book(self, title: str, author: str, isbn, category: str):
        """Add a book to the library."""
        # TODO: Create and store book
        pass

    def register_user(self, name: str, email: str):
        """Register a new user."""
        # TODO: Create and store user
        pass

    def borrow_book(self, user_id, book_id) -> bool:
        """Borrow a book for a user."""
        # TODO: Check if book is available and create loan
        pass

    def return_book(self, user_id, book_id) -> float:
        """Return a book and calculate fine."""
        # TODO: Find loan, remove it, calculate fine
        pass

    def search_books(self, query: str) -> List[Book]:
        """Search books by title or author."""
        # TODO: Search books matching query
        pass

    def get_statistics(self) -> Dict[str, Union[int, float]]:
        """Get library statistics."""
        # TODO: Calculate various statistics
        pass

def main():
    """Test your library system."""
    # TODO: Test Library functionality
    # library = Library()

    # Add books
    # book1 = library.add_book("Python Basics", "John Doe", "1234567890", "Tech")
    # book2 = library.add_book("Advanced Python", "Jane Smith", "0987654321", "Tech")

    # Register users
    # user = library.register_user("Alice", "alice@example.com")

    # Borrow books
    # success = library.borrow_book(user.user_id, book1.book_id)
    # print(f"Borrow successful: {success}")

    # Return books and calculate fines
    # fine = library.return_book(user.user_id, book1.book_id)
    # print(f"Fine: ${fine}")

    # Search books
    # results = library.search_books("Python")
    # print(f"Search results: {len(results)} books found")

    # Generate reports
    # stats = library.get_statistics()
    # print(f"Library stats: {stats}")

if __name__ == "__main__":
    main()
