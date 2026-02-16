"""
Custom Types and Type Aliases Demo
==================================

This demo shows how to create custom types and type aliases for better code organization
and reusability. This includes type aliases, custom classes, and advanced typing features.
"""

from typing import List, Dict, Tuple, Optional, Union, NewType, NamedTuple, TypedDict
from enum import Enum

# Type aliases for better readability
UserId = str
Email = str
PhoneNumber = str
Address = str

# NewType for type safety (creates distinct types)
ProductId = NewType('ProductId', int)
OrderId = NewType('OrderId', str)

# NamedTuple for structured data
class Person(NamedTuple):
    name: str
    age: int
    email: Email  # Using type alias

# TypedDict for dictionaries with known structure
class UserProfile(TypedDict):
    user_id: UserId
    name: str
    email: Email
    phone: Optional[PhoneNumber]
    address: Optional[Address]

class Product(TypedDict):
    id: ProductId
    name: str
    price: float
    in_stock: bool

# Enum for restricted values
class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

# Complex type aliases
Contacts = List[Person]
ProductCatalog = Dict[ProductId, Product]
OrderHistory = List[Tuple[OrderId, OrderStatus, float]]

# Custom classes with type hints
class User:
    def __init__(self, user_id: UserId, name: str, email: Email, role: UserRole = UserRole.USER):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

    def get_profile(self) -> UserProfile:
        """Return user profile as typed dictionary."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone": None,
            "address": None
        }

    def can_access_admin(self) -> bool:
        """Check if user has admin access."""
        return self.role == UserRole.ADMIN

class ShoppingCart:
    def __init__(self):
        self.items: Dict[ProductId, int] = {}  # product_id -> quantity

    def add_item(self, product_id: ProductId, quantity: int = 1) -> None:
        """Add item to cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items[product_id] = self.items.get(product_id, 0) + quantity

    def get_total_items(self) -> int:
        """Get total number of items in cart."""
        return sum(self.items.values())

    def get_items(self) -> Dict[ProductId, int]:
        """Get all items in cart."""
        return self.items.copy()

# Functions using custom types
def create_user(user_id: UserId, name: str, email: Email) -> User:
    """Create a new user."""
    return User(user_id, name, email)

def find_user_by_id(user_id: UserId, users: List[User]) -> Optional[User]:
    """Find user by ID."""
    for user in users:
        if user.user_id == user_id:
            return user
    return None

def create_person(name: str, age: int, email: str) -> Person:
    """Create a Person namedtuple."""
    return Person(name=name, age=age, email=email)

def validate_email(email: Email) -> bool:
    """Simple email validation."""
    return '@' in email and '.' in email

def format_contacts(contacts: Contacts) -> str:
    """Format contacts list for display."""
    if not contacts:
        return "No contacts"

    lines = []
    for contact in contacts:
        lines.append(f"- {contact.name} ({contact.age}) - {contact.email}")
    return "\n".join(lines)

def calculate_order_total(order_items: Dict[ProductId, int], catalog: ProductCatalog) -> float:
    """Calculate total price for order items."""
    total = 0.0
    for product_id, quantity in order_items.items():
        if product_id in catalog:
            product = catalog[product_id]
            if product['in_stock']:
                total += product['price'] * quantity
    return total

def main():
    """Demonstrate custom types and type aliases."""
    print("=== Custom Types and Type Aliases Demo ===\n")

    # Using type aliases and NewType
    print("--- Type Aliases and NewType ---")
    user_id: UserId = "user123"
    email: Email = "alice@example.com"
    product_id: ProductId = ProductId(101)  # Using NewType

    print(f"User ID: {user_id} (type: {type(user_id).__name__})")
    print(f"Email: {email} (type: {type(email).__name__})")
    print(f"Product ID: {product_id} (type: {type(product_id).__name__})\n")

    # Using NamedTuple
    print("--- NamedTuple ---")
    person = create_person("Alice Johnson", 30, "alice@example.com")
    print(f"Person: {person}")
    print(f"Name: {person.name}, Age: {person.age}, Email: {person.email}\n")

    # Using TypedDict
    print("--- TypedDict ---")
    profile: UserProfile = {
        "user_id": "user456",
        "name": "Bob Smith",
        "email": "bob@example.com",
        "phone": "+1-555-0123",
        "address": "123 Main St"
    }
    print(f"User profile: {profile}\n")

    # Using custom classes
    print("--- Custom Classes ---")
    user = create_user("user789", "Charlie Brown", "charlie@example.com")
    print(f"Created user: {user.name} ({user.user_id})")
    print(f"User profile: {user.get_profile()}")
    print(f"Can access admin: {user.can_access_admin()}\n")

    # Using shopping cart
    print("--- Shopping Cart ---")
    cart = ShoppingCart()
    cart.add_item(ProductId(101), 2)
    cart.add_item(ProductId(102), 1)
    print(f"Cart items: {cart.get_items()}")
    print(f"Total items: {cart.get_total_items()}\n")

    # Using complex type aliases
    print("--- Complex Type Aliases ---")
    contacts: Contacts = [
        create_person("Alice", 30, "alice@example.com"),
        create_person("Bob", 25, "bob@example.com"),
        create_person("Charlie", 35, "charlie@example.com")
    ]
    print("Contacts:")
    print(format_contacts(contacts))
    print()

    # Product catalog example
    catalog: ProductCatalog = {
        ProductId(101): {"id": ProductId(101), "name": "Laptop", "price": 999.99, "in_stock": True},
        ProductId(102): {"id": ProductId(102), "name": "Mouse", "price": 29.99, "in_stock": True},
        ProductId(103): {"id": ProductId(103), "name": "Keyboard", "price": 79.99, "in_stock": False}
    }

    order_items = {ProductId(101): 1, ProductId(102): 2}
    total = calculate_order_total(order_items, catalog)
    print(f"Order total: ${total:.2f}")

    # Enum usage
    print("\n--- Enums ---")
    admin_user = User("admin001", "Admin User", "admin@example.com", UserRole.ADMIN)
    regular_user = User("user001", "Regular User", "user@example.com", UserRole.USER)

    print(f"Admin user can access admin: {admin_user.can_access_admin()}")
    print(f"Regular user can access admin: {regular_user.can_access_admin()}")

if __name__ == "__main__":
    main()
