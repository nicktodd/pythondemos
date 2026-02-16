"""
Type Hints Best Practices Demo
==============================

This demo shows best practices for using type hints effectively in Python.
It covers when to use types, how to write clean type annotations, and common patterns.
"""

from typing import List, Dict, Optional, Union, Any, Callable, TypeVar, Generic
import logging
from functools import wraps

# Setup logging for error demonstration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TypeVar for generics
T = TypeVar('T')

# Best Practice 1: Use descriptive type aliases
UserId = str
ProductId = int
EmailAddress = str
Price = float

# Best Practice 2: Define clear data structures
class User:
    def __init__(self, user_id: UserId, name: str, email: EmailAddress):
        self.user_id = user_id
        self.name = name
        self.email = email

class Product:
    def __init__(self, product_id: ProductId, name: str, price: Price):
        self.product_id = product_id
        self.name = name
        self.price = price

# Best Practice 3: Use Union for multiple possible types
def process_payment(amount: Union[int, float, str]) -> bool:
    """Process payment with flexible amount types."""
    try:
        # Convert to float for processing
        numeric_amount = float(amount)
        if numeric_amount <= 0:
            logger.error(f"Invalid payment amount: {amount}")
            return False

        logger.info(f"Processing payment of ${numeric_amount:.2f}")
        return True
    except (ValueError, TypeError) as e:
        logger.error(f"Payment processing failed: {e}")
        return False

# Best Practice 4: Use Optional for nullable values
def find_user_by_email(email: EmailAddress, users: List[User]) -> Optional[User]:
    """Find user by email address."""
    for user in users:
        if user.email.lower() == email.lower():
            return user
    return None

# Best Practice 5: Use Callable for function parameters
def apply_discount(products: List[Product], discount_func: Callable[[Product], Price]) -> List[Product]:
    """Apply discount to products using a custom function."""
    discounted_products = []
    for product in products:
        new_price = discount_func(product)
        # Create new product with discounted price
        discounted_product = Product(
            product_id=product.product_id,
            name=f"{product.name} (Discounted)",
            price=new_price
        )
        discounted_products.append(discounted_product)
    return discounted_products

# Best Practice 6: Use Generic types when appropriate
class Repository(Generic[T]):
    """Generic repository for data storage."""

    def __init__(self):
        self.items: Dict[Any, T] = {}

    def save(self, key: Any, item: T) -> None:
        """Save an item."""
        self.items[key] = item

    def get(self, key: Any) -> Optional[T]:
        """Get an item by key."""
        return self.items.get(key)

    def get_all(self) -> List[T]:
        """Get all items."""
        return list(self.items.values())

# Best Practice 7: Type complex return values
def get_user_statistics(users: List[User]) -> Dict[str, Union[int, float, List[str]]]:
    """Calculate statistics about users."""
    if not users:
        return {
            "total_users": 0,
            "average_name_length": 0.0,
            "domains": []
        }

    total_users = len(users)
    name_lengths = [len(user.name) for user in users]
    average_name_length = sum(name_lengths) / len(name_lengths)

    # Extract email domains
    domains = []
    for user in users:
        try:
            domain = user.email.split('@')[1]
            if domain not in domains:
                domains.append(domain)
        except IndexError:
            continue  # Skip invalid emails

    return {
        "total_users": total_users,
        "average_name_length": round(average_name_length, 2),
        "domains": domains
    }

# Best Practice 8: Use type comments for older Python versions
def legacy_function(value):
    # type: (str) -> str
    """Function with type comments for Python < 3.5 compatibility."""
    return value.upper()

# Best Practice 9: Avoid over-typing - use Any when appropriate
def process_unknown_data(data: Any) -> Any:
    """Process data of unknown type."""
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, (int, float)):
        return data * 2
    elif isinstance(data, list):
        return [process_unknown_data(item) for item in data]
    else:
        return str(data)

# Best Practice 10: Document complex type decisions
def validate_and_convert_age(age_input: Union[str, int, float]) -> Optional[int]:
    """
    Validate and convert age input to integer.

    Args:
        age_input: Age as string, int, or float

    Returns:
        Valid age as integer, or None if invalid

    Note:
        - String ages are converted using int()
        - Float ages are truncated to integers
        - Negative ages are considered invalid
        - Ages over 150 are considered invalid
    """
    try:
        if isinstance(age_input, str):
            age = int(age_input)
        elif isinstance(age_input, float):
            age = int(age_input)  # Truncate float
        elif isinstance(age_input, int):
            age = age_input
        else:
            return None

        if 0 <= age <= 150:
            return age
        return None
    except (ValueError, TypeError):
        return None

# Decorator for type checking (educational - in practice, use mypy)
def type_check(func: Callable) -> Callable:
    """Decorator that performs basic type checking (for demonstration)."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # In a real implementation, you'd check types here
        # For now, just log the call
        logger.info(f"Calling {func.__name__} with {len(args)} args and {len(kwargs)} kwargs")
        return func(*args, **kwargs)
    return wrapper

@type_check
def calculate_total(products: List[Product]) -> Price:
    """Calculate total price of products."""
    return sum(product.price for product in products)

def main():
    """Demonstrate type hints best practices."""
    print("=== Type Hints Best Practices Demo ===\n")

    # Example 1: Type aliases and clear structures
    print("--- Type Aliases and Data Structures ---")
    user = User("user123", "Alice Johnson", "alice@example.com")
    product = Product(101, "Laptop", 999.99)
    print(f"User: {user.name} ({user.email})")
    print(f"Product: {product.name} - ${product.price}")
    print()

    # Example 2: Union types
    print("--- Union Types ---")
    payments = [100, 50.50, "75", -10, "invalid"]
    for payment in payments:
        success = process_payment(payment)
        status = "✓" if success else "✗"
        print(f"{status} Payment of {payment}")
    print()

    # Example 3: Optional and error handling
    print("--- Optional Types and Error Handling ---")
    users = [
        User("u1", "Alice", "alice@gmail.com"),
        User("u2", "Bob", "bob@yahoo.com"),
        User("u3", "Charlie", "charlie@outlook.com")
    ]

    test_emails = ["alice@gmail.com", "nonexistent@example.com", "bob@yahoo.com"]
    for email in test_emails:
        found_user = find_user_by_email(email, users)
        if found_user:
            print(f"✓ Found user: {found_user.name}")
        else:
            print(f"✗ User not found: {email}")
    print()

    # Example 4: Callable types
    print("--- Callable Types ---")
    products = [
        Product(1, "Laptop", 1000),
        Product(2, "Mouse", 50),
        Product(3, "Keyboard", 100)
    ]

    # 10% discount function
    discount_10_percent = lambda p: p.price * 0.9

    # Fixed discount function
    discount_fixed = lambda p: max(p.price - 50, 0)

    discounted_10 = apply_discount(products, discount_10_percent)
    discounted_fixed = apply_discount(products, discount_fixed)

    print("Original products:")
    for p in products:
        print(f"  {p.name}: ${p.price}")

    print("\nWith 10% discount:")
    for p in discounted_10:
        print(f"  {p.name}: ${p.price}")

    print("\nWith $50 fixed discount:")
    for p in discounted_fixed:
        print(f"  {p.name}: ${p.price}")
    print()

    # Example 5: Generic repository
    print("--- Generic Repository ---")
    user_repo = Repository[User]()
    product_repo = Repository[Product]()

    user_repo.save("u1", user)
    product_repo.save(101, product)

    print(f"Users in repository: {len(user_repo.get_all())}")
    print(f"Products in repository: {len(product_repo.get_all())}")
    print()

    # Example 6: Complex return types
    print("--- Complex Return Types ---")
    stats = get_user_statistics(users)
    print("User statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    print()

    # Example 7: Age validation
    print("--- Age Validation ---")
    test_ages = ["25", 30, 25.7, -5, 200, "invalid", None]
    for age_input in test_ages:
        valid_age = validate_and_convert_age(age_input)
        if valid_age is not None:
            print(f"✓ {age_input} -> {valid_age}")
        else:
            print(f"✗ {age_input} -> Invalid")
    print()

    # Example 8: Unknown data processing
    print("--- Processing Unknown Data ---")
    unknown_data = [
        "hello",
        42,
        [1, 2, "three"],
        {"key": "value"},
        True
    ]

    print("Processing unknown data:")
    for data in unknown_data:
        result = process_unknown_data(data)
        print(f"  {data} ({type(data).__name__}) -> {result} ({type(result).__name__})")
    print()

    # Example 9: Decorator usage
    print("--- Type Checking Decorator ---")
    total = calculate_total(products)
    print(f"Total price of all products: ${total}")

    print("\n=== Best Practices Summary ===")
    print("✓ Use descriptive type aliases")
    print("✓ Define clear data structures with classes")
    print("✓ Use Union for multiple possible types")
    print("✓ Use Optional for nullable values")
    print("✓ Use Callable for function parameters")
    print("✓ Use Generic types when appropriate")
    print("✓ Document complex type decisions")
    print("✓ Avoid over-typing - use Any when needed")
    print("✓ Use static type checkers like mypy")
    print("✓ Keep type hints simple and readable")

if __name__ == "__main__":
    main()
