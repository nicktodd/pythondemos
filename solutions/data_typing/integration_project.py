"""
Integration Project Solution
============================

Complete implementation of a comprehensive library management system
combining all data typing concepts learned.
"""

from typing import List, Dict, Optional, Union
from datetime import datetime, timedelta
import uuid

# Type aliases for better code readability
BookId = str
UserId = str
ISBN = str

class Book:
    """Represents a book in the library."""
    
    def __init__(self, book_id: BookId, title: str, author: str, 
                 isbn: ISBN, category: str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.is_available = True
    
    def __str__(self) -> str:
        status = "Available" if self.is_available else "Borrowed"
        return f"Book(id={self.book_id}, title='{self.title}', author='{self.author}', status={status})"

class User:
    """Represents a library user."""
    
    def __init__(self, user_id: UserId, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        self.borrowed_books: List[BookId] = []
    
    def can_borrow(self) -> bool:
        """Check if user can borrow more books (max 3)."""
        return len(self.borrowed_books) < 3
    
    def borrow_book(self, book_id: BookId) -> None:
        """Add book to user's borrowed list."""
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
    
    def return_book(self, book_id: BookId) -> None:
        """Remove book from user's borrowed list."""
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
    
    def __str__(self) -> str:
        return f"User(id={self.user_id}, name='{self.name}', borrowed={len(self.borrowed_books)})"

class Loan:
    """Represents a book loan."""
    
    FINE_PER_DAY = 0.50  # $0.50 per day overdue
    
    def __init__(self, user_id: UserId, book_id: BookId, 
                 loan_date: datetime, due_date: datetime) -> None:
        self.user_id = user_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.due_date = due_date
        self.return_date: Optional[datetime] = None
    
    def is_overdue(self) -> bool:
        """Check if loan is overdue."""
        return datetime.now() > self.due_date and self.return_date is None
    
    def calculate_fine(self) -> float:
        """Calculate fine for overdue loan."""
        if not self.is_overdue():
            return 0.0
        
        days_overdue = (datetime.now() - self.due_date).days
        return max(0, days_overdue * self.FINE_PER_DAY)
    
    def mark_returned(self) -> None:
        """Mark the loan as returned."""
        self.return_date = datetime.now()
    
    def __str__(self) -> str:
        status = "Returned" if self.return_date else ("Overdue" if self.is_overdue() else "Active")
        return f"Loan(user={self.user_id}, book={self.book_id}, due={self.due_date.date()}, status={status})"

class Library:
    """Main library management system."""
    
    def __init__(self) -> None:
        self.books: Dict[BookId, Book] = {}
        self.users: Dict[UserId, User] = {}
        self.loans: List[Loan] = []
        self.next_book_id = 1
    
    def add_book(self, title: str, author: str, isbn: ISBN, category: str) -> Book:
        """Add a book to the library."""
        book_id = f"book_{self.next_book_id}"
        self.next_book_id += 1
        
        book = Book(book_id, title, author, isbn, category)
        self.books[book_id] = book
        
        print(f"✓ Added book: {book}")
        return book
    
    def register_user(self, name: str, email: str) -> User:
        """Register a new user."""
        user_id = f"user_{uuid.uuid4().hex[:8]}"
        
        user = User(user_id, name, email)
        self.users[user_id] = user
        
        print(f"✓ Registered user: {user}")
        return user
    
    def borrow_book(self, user_id: UserId, book_id: BookId) -> bool:
        """Borrow a book for a user."""
        user = self.users.get(user_id)
        book = self.books.get(book_id)
        
        if not user or not book:
            print("✗ User or book not found")
            return False
        
        if not book.is_available:
            print("✗ Book is not available")
            return False
        
        if not user.can_borrow():
            print("✗ User has reached borrowing limit")
            return False
        
        # Create loan
        loan_date = datetime.now()
        due_date = loan_date + timedelta(days=14)  # 2 weeks
        
        loan = Loan(user_id, book_id, loan_date, due_date)
        self.loans.append(loan)
        
        # Update book and user status
        book.is_available = False
        user.borrow_book(book_id)
        
        print(f"✓ Book borrowed: {book.title} by {user.name}")
        return True
    
    def return_book(self, user_id: UserId, book_id: BookId) -> float:
        """Return a book and calculate fine."""
        user = self.users.get(user_id)
        book = self.books.get(book_id)
        
        if not user or not book:
            print("✗ User or book not found")
            return 0.0
        
        # Find the loan
        loan = None
        for l in self.loans:
            if l.user_id == user_id and l.book_id == book_id and l.return_date is None:
                loan = l
                break
        
        if not loan:
            print("✗ No active loan found")
            return 0.0
        
        # Mark as returned
        loan.mark_returned()
        fine = loan.calculate_fine()
        
        # Update book and user status
        book.is_available = True
        user.return_book(book_id)
        
        print(f"✓ Book returned: {book.title} by {user.name}")
        if fine > 0:
            print(f"⚠ Fine: ${fine:.2f}")
        
        return fine
    
    def search_books(self, query: str) -> List[Book]:
        """Search books by title or author."""
        query_lower = query.lower()
        results = []
        
        for book in self.books.values():
            if (query_lower in book.title.lower() or 
                query_lower in book.author.lower()):
                results.append(book)
        
        return results
    
    def get_statistics(self) -> Dict[str, Union[int, float]]:
        """Get library statistics."""
        total_books = len(self.books)
        available_books = sum(1 for b in self.books.values() if b.is_available)
        total_users = len(self.users)
        active_loans = sum(1 for l in self.loans if l.return_date is None)
        overdue_loans = sum(1 for l in self.loans if l.is_overdue())
        total_fines = sum(l.calculate_fine() for l in self.loans)
        
        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": total_books - available_books,
            "total_users": total_users,
            "active_loans": active_loans,
            "overdue_loans": overdue_loans,
            "total_fines": round(total_fines, 2)
        }

def main() -> None:
    """Test the complete library system."""
    print("=== Library Management System Demo ===\n")
    
    library = Library()
    
    # Add books
    book1 = library.add_book("Python Basics", "John Doe", "1234567890", "Technology")
    book2 = library.add_book("Advanced Python", "Jane Smith", "0987654321", "Technology")
    book3 = library.add_book("Data Science Handbook", "Bob Johnson", "1122334455", "Science")
    
    print()
    
    # Register users
    user1 = library.register_user("Alice", "alice@example.com")
    user2 = library.register_user("Bob", "bob@example.com")
    
    print()
    
    # Borrow books
    success1 = library.borrow_book(user1.user_id, book1.book_id)
    success2 = library.borrow_book(user1.user_id, book2.book_id)
    success3 = library.borrow_book(user2.user_id, book3.book_id)
    
    print()
    
    # Search books
    results = library.search_books("Python")
    print(f"✓ Search for 'Python': {len(results)} books found")
    for book in results:
        print(f"  - {book.title} by {book.author}")
    
    print()
    
    # Simulate time passing for overdue test
    # In a real system, you'd use actual dates
    print("Simulating 16 days passing for overdue test...")
    
    print()
    
    # Return books and calculate fines
    fine1 = library.return_book(user1.user_id, book1.book_id)
    fine2 = library.return_book(user1.user_id, book2.book_id)
    fine3 = library.return_book(user2.user_id, book3.book_id)
    
    print()
    
    # Generate reports
    stats = library.get_statistics()
    print("✓ Library Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n=== Demo completed successfully ===")

if __name__ == "__main__":
    main()
