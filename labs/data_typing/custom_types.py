"""
Custom Types and Type Aliases Lab
=================================

Create and use custom types and type aliases.
Complete the TODO sections below.
"""

from typing import NamedTuple, TypedDict, List

# TODO: Define type aliases
# UserId = str
# ProductId = int
# Email = str
# Price = float

# TODO: Create a Person NamedTuple with name, age, and email fields
# class Person(NamedTuple):
#     ...

# TODO: Create a Product TypedDict with id, name, price, and in_stock fields
# class Product(TypedDict):
#     ...

class ShoppingCart:
    """A shopping cart that uses custom types."""

    def __init__(self):
        # TODO: Initialize cart items as a dict
        self.items = {}

    def add_product(self, product_id, product):
        """Add a product to the cart."""
        # TODO: Add product to cart
        pass

    def remove_product(self, product_id):
        """Remove a product from the cart."""
        # TODO: Remove product from cart
        pass

    def get_total_price(self):
        """Calculate total price of items in cart."""
        # TODO: Calculate and return total price
        pass

def create_person(name: str, age: int, email: str):
    """Create a Person namedtuple."""
    # TODO: Return a Person instance
    pass

def create_product(product_id, name: str, price: float, in_stock: bool):
    """Create a Product typed dict."""
    # TODO: Return a Product dict
    pass

def main():
    """Test your implementations."""
    # TODO: Test create_person
    # person = create_person("Alice", 30, "alice@example.com")
    # print(f"Person: {person}")

    # TODO: Test create_product
    # product = create_product(101, "Laptop", 999.99, True)
    # print(f"Product: {product}")

    # TODO: Test ShoppingCart
    # cart = ShoppingCart()
    # cart.add_product(101, product)
    # print(f"Cart total: ${cart.get_total_price()}")

if __name__ == "__main__":
    main()
