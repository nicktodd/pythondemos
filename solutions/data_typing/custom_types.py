"""
Custom Types and Type Aliases Solution
======================================

Complete implementation of custom types and type aliases.
"""

from typing import NamedTuple, TypedDict, List, Dict

# Type aliases
UserId = str
ProductId = int
Email = str
Price = float

# Person NamedTuple
class Person(NamedTuple):
    name: str
    age: int
    email: Email

# Product TypedDict
class Product(TypedDict):
    id: ProductId
    name: str
    price: Price
    in_stock: bool

class ShoppingCart:
    """A shopping cart that uses custom types."""

    def __init__(self):
        self.items: Dict[ProductId, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add a product to the cart."""
        self.items[product['id']] = product

    def remove_product(self, product_id: ProductId) -> bool:
        """Remove a product from the cart. Returns True if removed."""
        if product_id in self.items:
            del self.items[product_id]
            return True
        return False

    def get_total_price(self) -> Price:
        """Calculate total price of items in cart."""
        return sum(product['price'] for product in self.items.values())

    def get_items(self) -> List[Product]:
        """Get all items in the cart."""
        return list(self.items.values())

def create_person(name: str, age: int, email: str) -> Person:
    """Create a Person namedtuple."""
    return Person(name=name, age=age, email=email)

def create_product(product_id: ProductId, name: str, price: Price, in_stock: bool) -> Product:
    """Create a Product typed dict."""
    return {
        "id": product_id,
        "name": name,
        "price": price,
        "in_stock": in_stock
    }

def find_product_by_id(products: List[Product], product_id: ProductId) -> Product:
    """Find a product by ID."""
    for product in products:
        if product['id'] == product_id:
            return product
    raise ValueError(f"Product with ID {product_id} not found")

def main():
    """Test the implementations."""
    # Test create_person
    person = create_person("Alice Johnson", 30, "alice@example.com")
    print(f"Person: {person}")
    print(f"Name: {person.name}, Age: {person.age}, Email: {person.email}")

    # Test create_product
    product = create_product(101, "Wireless Mouse", 29.99, True)
    print(f"\nProduct: {product}")

    # Test ShoppingCart
    cart = ShoppingCart()

    # Add products to cart
    laptop = create_product(201, "Laptop", 999.99, True)
    keyboard = create_product(202, "Keyboard", 79.99, True)
    mouse = create_product(203, "Mouse", 29.99, False)

    cart.add_product(laptop)
    cart.add_product(keyboard)
    cart.add_product(mouse)

    print(f"\nCart items: {len(cart.get_items())}")
    print(f"Cart total: ${cart.get_total_price():.2f}")

    # Remove a product
    removed = cart.remove_product(202)  # Remove keyboard
    print(f"Removed keyboard: {removed}")
    print(f"Cart total after removal: ${cart.get_total_price():.2f}")

    # Test finding products
    products = [laptop, keyboard, mouse]
    try:
        found = find_product_by_id(products, 201)
        print(f"\nFound product: {found['name']} - ${found['price']}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
