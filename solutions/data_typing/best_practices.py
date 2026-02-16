"""
Best Practices Solution
=======================

Complete implementation of type hinting best practices for an e-commerce system.
"""

from typing import List, Dict, Optional, Union, Generic, TypeVar
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Type aliases for better readability
UserId = str
ProductId = int
Email = str
Price = float
OrderId = str

# Custom types
class User:
    """Represents a user in the system."""
    
    def __init__(self, user_id: UserId, name: str, email: Email) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
    
    def is_valid(self) -> bool:
        """Check if user data is valid."""
        return (
            isinstance(self.user_id, str) and len(self.user_id) > 0 and
            isinstance(self.name, str) and len(self.name) > 0 and
            isinstance(self.email, str) and "@" in self.email
        )
    
    def __str__(self) -> str:
        return f"User(id={self.user_id}, name={self.name}, email={self.email})"

class Product:
    """Represents a product in the catalog."""
    
    def __init__(self, product_id: ProductId, name: str, price: Price) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def is_valid(self) -> bool:
        """Check if product data is valid."""
        return (
            isinstance(self.product_id, int) and self.product_id > 0 and
            isinstance(self.name, str) and len(self.name) > 0 and
            isinstance(self.price, (int, float)) and self.price >= 0
        )
    
    def __str__(self) -> str:
        return f"Product(id={self.product_id}, name={self.name}, price=${self.price:.2f})"

# Generic repository pattern
T = TypeVar('T')

class Repository(Generic[T]):
    """Generic repository for data storage with proper typing."""
    
    def __init__(self) -> None:
        self.items: Dict[Union[str, int], T] = {}
    
    def save(self, key: Union[str, int], item: T) -> None:
        """Save an item with the given key."""
        if not isinstance(key, (str, int)):
            raise ValueError("Key must be string or int")
        self.items[key] = item
        logger.info(f"Saved item with key: {key}")
    
    def get(self, key: Union[str, int]) -> Optional[T]:
        """Get an item by key."""
        return self.items.get(key)
    
    def get_all(self) -> List[T]:
        """Get all items."""
        return list(self.items.values())
    
    def delete(self, key: Union[str, int]) -> bool:
        """Delete an item by key."""
        if key in self.items:
            del self.items[key]
            logger.info(f"Deleted item with key: {key}")
            return True
        return False

class UserManager:
    """Manages user operations with type safety."""
    
    def __init__(self) -> None:
        self.users: Dict[UserId, User] = {}
        self.next_id = 1
    
    def create_user(self, name: str, email: Email) -> User:
        """Create a new user with validation."""
        if not name or not email:
            raise ValueError("Name and email are required")
        
        user_id = f"user_{self.next_id}"
        self.next_id += 1
        
        user = User(user_id, name, email)
        if not user.is_valid():
            raise ValueError("Invalid user data")
        
        self.users[user_id] = user
        logger.info(f"Created user: {user_id}")
        return user
    
    def find_user(self, user_id: UserId) -> Optional[User]:
        """Find user by ID."""
        return self.users.get(user_id)
    
    def get_all_users(self) -> List[User]:
        """Get all users."""
        return list(self.users.values())

class ProductRepository(Repository[Product]):
    """Repository specifically for products."""
    
    def find_by_name(self, name: str) -> List[Product]:
        """Find products by name (case-insensitive)."""
        return [p for p in self.items.values() 
                if name.lower() in p.name.lower()]
    
    def find_by_price_range(self, min_price: Price, max_price: Price) -> List[Product]:
        """Find products within price range."""
        return [p for p in self.items.values() 
                if min_price <= p.price <= max_price]

class Order:
    """Represents an order in the system."""
    
    def __init__(self, order_id: OrderId, user: User, products: List[Product]) -> None:
        self.order_id = order_id
        self.user = user
        self.products = products
        self.timestamp = "2024-01-01T00:00:00Z"  # Simplified timestamp
    
    def __str__(self) -> str:
        return f"Order(id={self.order_id}, user={self.user.name}, items={len(self.products)})"

def calculate_order_total(products: List[Product]) -> Price:
    """Calculate total price of products with validation."""
    if not products:
        return 0.0
    
    total = sum(product.price for product in products)
    return round(total, 2)

def create_order(user: User, products: List[Product]) -> Order:
    """Create an order for a user with proper validation."""
    if not user or not user.is_valid():
        raise ValueError("Valid user is required")
    
    if not products or not all(p.is_valid() for p in products):
        raise ValueError("Valid products are required")
    
    # Generate simple order ID
    order_id = f"order_{hash((user.user_id, len(products)))}"
    order = Order(order_id, user, products)
    
    logger.info(f"Created order: {order_id}")
    return order

def main() -> None:
    """Test the complete e-commerce system."""
    print("=== E-Commerce System Demo ===\n")
    
    # Test UserManager
    user_manager = UserManager()
    try:
        user = user_manager.create_user("Alice", "alice@example.com")
        print(f"✓ Created user: {user}")
    except ValueError as e:
        print(f"✗ Error creating user: {e}")
    
    # Test ProductRepository
    product_repo = ProductRepository()
    product = Product(1, "Laptop", 999.99)
    product_repo.save(1, product)
    
    retrieved = product_repo.get(1)
    if retrieved:
        print(f"✓ Retrieved product: {retrieved}")
    
    # Test order creation
    try:
        order = create_order(user, [product])
        total = calculate_order_total([product])
        print(f"✓ Created order: {order}")
        print(f"✓ Order total: ${total}")
    except ValueError as e:
        print(f"✗ Error creating order: {e}")
    
    # Test additional features
    product2 = Product(2, "Mouse", 29.99)
    product_repo.save(2, product2)
    
    # Find products by price range
    affordable = product_repo.find_by_price_range(0, 100)
    print(f"✓ Found {len(affordable)} affordable products")
    
    print("\n=== All tests completed ===")

if __name__ == "__main__":
    main()
