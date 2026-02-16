"""
Best Practices Lab
==================

Apply type hinting best practices.
Complete the TODO sections below.
"""

from typing import List, Dict, Optional, Union, Generic, TypeVar

# TODO: Define type aliases
# UserId = str
# ProductId = int
# Email = str
# Price = float

# TODO: Create User class
class User:
    def __init__(self, user_id, name: str, email):
        # TODO: Initialize user attributes
        pass

    def is_valid(self) -> bool:
        """Check if user data is valid."""
        # TODO: Implement validation
        pass

# TODO: Create Product class
class Product:
    def __init__(self, product_id, name: str, price):
        # TODO: Initialize product attributes
        pass

# TODO: Create generic Repository
T = TypeVar('T')

class Repository(Generic[T]):
    """Generic repository for data storage."""

    def __init__(self):
        self.items = {}

    def save(self, key, item: T):
        """Save an item."""
        # TODO: Implement save
        pass

    def get(self, key):
        """Get an item by key."""
        # TODO: Implement get
        pass

    def get_all(self):
        """Get all items."""
        # TODO: Implement get_all
        pass

# TODO: Create UserManager class
class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, name: str, email):
        """Create a new user."""
        # TODO: Create and store user
        pass

    def find_user(self, user_id):
        """Find user by ID."""
        # TODO: Find and return user
        pass

# TODO: Create ProductRepository class
class ProductRepository(Repository[Product]):
    """Repository for products."""
    pass

def calculate_order_total(products: List[Product]) -> float:
    """Calculate total price of products."""
    # TODO: Sum product prices
    pass

def create_order(user, products: List[Product]):
    """Create an order for a user."""
    # TODO: Create order dict with user and products
    pass

def main():
    """Test your implementations."""
    # TODO: Test UserManager
    # user_manager = UserManager()
    # user = user_manager.create_user("alice", "alice@example.com")
    # print(f"Created user: {user.name}")

    # TODO: Test ProductRepository
    # product_repo = ProductRepository()
    # product = Product(1, "Laptop", 999.99)
    # product_repo.save(1, product)
    # retrieved = product_repo.get(1)
    # print(f"Retrieved product: {retrieved.name}")

    # TODO: Test order creation
    # order = create_order(user, [product])
    # total = calculate_order_total([product])
    # print(f"Order total: ${total}")

if __name__ == "__main__":
    main()
