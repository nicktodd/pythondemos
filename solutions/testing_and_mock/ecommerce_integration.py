"""
E-commerce Integration Tests Solution

Complete implementation of integration tests for an e-commerce system.
"""

import pytest
import tempfile
import os
import sqlite3
from unittest.mock import Mock


class UserManager:
    """User management for e-commerce."""

    def __init__(self, db_connection):
        self.db = db_connection

    def register_user(self, name, email):
        """Register a new user."""
        # Check if user exists
        if self.db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone():
            raise ValueError("User already exists")

        # Save to database
        cursor = self.db.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
        self.db.commit()
        return cursor.lastrowid

    def get_user(self, user_id):
        """Get user by ID."""
        row = self.db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        if row:
            return {"id": row[0], "name": row[1], "email": row[2]}
        return None


class ProductCatalog:
    """Product catalog management."""

    def __init__(self, db_connection):
        self.db = db_connection

    def add_product(self, name, price, stock):
        """Add a new product."""
        cursor = self.db.execute(
            "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
            (name, price, stock)
        )
        self.db.commit()
        return cursor.lastrowid

    def get_product(self, product_id):
        """Get product by ID."""
        row = self.db.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
        if row:
            return {"id": row[0], "name": row[1], "price": row[2], "stock": row[3]}
        return None

    def check_stock(self, product_id, quantity):
        """Check if product has sufficient stock."""
        row = self.db.execute("SELECT stock FROM products WHERE id = ?", (product_id,)).fetchone()
        if row:
            return row[0] >= quantity
        return False

    def reduce_stock(self, product_id, quantity):
        """Reduce product stock."""
        self.db.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (quantity, product_id)
        )
        self.db.commit()


class OrderProcessor:
    """Order processing system."""

    def __init__(self, db_connection, payment_service=None, email_service=None):
        self.db = db_connection
        self.payment = payment_service or Mock()
        self.email = email_service or Mock()

    def create_order(self, user_id, items):
        """Create a new order."""
        # Validate user exists
        user = self.db.execute("SELECT id FROM users WHERE id = ?", (user_id,)).fetchone()
        if not user:
            raise ValueError("User not found")

        # Check product availability and calculate total
        total = 0
        for item in items:
            product = self.db.execute(
                "SELECT price, stock FROM products WHERE id = ?",
                (item["product_id"],)
            ).fetchone()
            if not product:
                raise ValueError(f"Product {item['product_id']} not found")
            if product[1] < item["quantity"]:
                raise ValueError(f"Insufficient stock for product {item['product_id']}")
            total += product[0] * item["quantity"]

        # Process payment
        payment_result = self.payment.charge(total)
        if not payment_result["success"]:
            raise ValueError("Payment failed")

        # Save order
        cursor = self.db.execute(
            "INSERT INTO orders (user_id, total, payment_id) VALUES (?, ?, ?)",
            (user_id, total, payment_result["transaction_id"])
        )
        order_id = cursor.lastrowid

        # Save order items
        for item in items:
            self.db.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)",
                (order_id, item["product_id"], item["quantity"],
                 self.db.execute("SELECT price FROM products WHERE id = ?", (item["product_id"],)).fetchone()[0])
            )
            # Reduce stock
            self.db.execute(
                "UPDATE products SET stock = stock - ? WHERE id = ?",
                (item["quantity"], item["product_id"])
            )

        self.db.commit()

        # Send confirmation
        order_details = {
            "order_id": order_id,
            "total": total,
            "items": items
        }
        self.email.send_order_confirmation(user_id, order_details)

        return order_id

    def get_order(self, order_id):
        """Get order by ID."""
        row = self.db.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
        if row:
            return {"id": row[0], "user_id": row[1], "total": row[2], "payment_id": row[3]}
        return None


class EmailService:
    """Email service for notifications."""

    def __init__(self):
        self.sent_emails = []

    def send_order_confirmation(self, user_email, order_details):
        """Send order confirmation email."""
        self.sent_emails.append({
            "to": user_email,
            "subject": f"Order Confirmation #{order_details['order_id']}",
            "order_details": order_details
        })


@pytest.fixture
def temp_db():
    """Temporary database for integration tests."""
    # Create temporary database
    db_fd, db_path = tempfile.mkstemp()
    db = sqlite3.connect(db_path)

    # Create tables
    db.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    db.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    db.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            total REAL NOT NULL,
            payment_id TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    db.execute("""
        CREATE TABLE order_items (
            id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    """)

    db.commit()

    yield db

    # Cleanup
    db.close()
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def user_manager(temp_db):
    """UserManager with real database."""
    return UserManager(temp_db)


@pytest.fixture
def product_catalog(temp_db):
    """ProductCatalog with real database."""
    return ProductCatalog(temp_db)


@pytest.fixture
def email_service():
    """Email service for testing."""
    return EmailService()


@pytest.fixture
def order_processor(temp_db, email_service):
    """OrderProcessor with real database and mocked services."""
    payment_service = Mock()
    payment_service.charge.return_value = {"success": True, "transaction_id": "txn_123"}
    return OrderProcessor(temp_db, payment_service, email_service)


def test_user_registration_integration(user_manager):
    """Test complete user registration flow."""
    user_id = user_manager.register_user("John Doe", "john@example.com")
    assert user_id is not None

    user = user_manager.get_user(user_id)
    assert user["name"] == "John Doe"
    assert user["email"] == "john@example.com"


def test_user_registration_duplicate_email(user_manager):
    """Test user registration with duplicate email."""
    user_manager.register_user("John Doe", "john@example.com")

    with pytest.raises(ValueError, match="User already exists"):
        user_manager.register_user("Jane Doe", "john@example.com")


def test_product_management_integration(product_catalog):
    """Test product catalog operations."""
    product_id = product_catalog.add_product("Laptop", 999.99, 10)
    assert product_id is not None

    product = product_catalog.get_product(product_id)
    assert product["name"] == "Laptop"
    assert product["price"] == 999.99
    assert product["stock"] == 10

    assert product_catalog.check_stock(product_id, 5) is True
    assert product_catalog.check_stock(product_id, 15) is False

    product_catalog.reduce_stock(product_id, 3)
    product = product_catalog.get_product(product_id)
    assert product["stock"] == 7


def test_order_creation_integration(user_manager, product_catalog, order_processor, email_service):
    """Test complete order creation flow."""
    # Register user
    user_id = user_manager.register_user("Alice", "alice@example.com")

    # Add products
    product1_id = product_catalog.add_product("Book", 20.00, 5)
    product2_id = product_catalog.add_product("Pen", 2.00, 10)

    # Create order
    items = [
        {"product_id": product1_id, "quantity": 2},
        {"product_id": product2_id, "quantity": 3}
    ]
    order_id = order_processor.create_order(user_id, items)

    # Verify order was saved
    order = order_processor.get_order(order_id)
    assert order is not None
    assert order["user_id"] == user_id
    assert order["total"] == 46.00  # (2*20) + (3*2)

    # Verify stock was reduced
    book = product_catalog.get_product(product1_id)
    pen = product_catalog.get_product(product2_id)
    assert book["stock"] == 3  # 5 - 2
    assert pen["stock"] == 7   # 10 - 3

    # Verify email was sent
    assert len(email_service.sent_emails) == 1
    email = email_service.sent_emails[0]
    assert email["to"] == user_id  # Note: simplified for testing
    assert "Order Confirmation" in email["subject"]


def test_order_with_insufficient_stock(user_manager, product_catalog, order_processor):
    """Test order creation with insufficient stock."""
    user_id = user_manager.register_user("Bob", "bob@example.com")
    product_id = product_catalog.add_product("Rare Item", 100.00, 1)

    items = [{"product_id": product_id, "quantity": 5}]

    with pytest.raises(ValueError, match="Insufficient stock"):
        order_processor.create_order(user_id, items)


def test_payment_failure_integration(user_manager, product_catalog, order_processor):
    """Test order creation with payment failure."""
    user_id = user_manager.register_user("Charlie", "charlie@example.com")
    product_id = product_catalog.add_product("Expensive Item", 500.00, 5)

    # Mock payment failure
    order_processor.payment.charge.return_value = {"success": False, "error": "Card declined"}

    items = [{"product_id": product_id, "quantity": 1}]

    with pytest.raises(ValueError, match="Payment failed"):
        order_processor.create_order(user_id, items)

    # Verify stock was not reduced
    product = product_catalog.get_product(product_id)
    assert product["stock"] == 5


def test_multiple_orders_integration(user_manager, product_catalog, order_processor):
    """Test creating multiple orders."""
    user_id = user_manager.register_user("David", "david@example.com")
    product_id = product_catalog.add_product("Widget", 10.00, 20)

    # Create first order
    items1 = [{"product_id": product_id, "quantity": 2}]
    order1_id = order_processor.create_order(user_id, items1)

    # Create second order
    items2 = [{"product_id": product_id, "quantity": 3}]
    order2_id = order_processor.create_order(user_id, items2)

    # Verify both orders exist
    order1 = order_processor.get_order(order1_id)
    order2 = order_processor.get_order(order2_id)
    assert order1 is not None
    assert order2 is not None

    # Verify stock levels
    product = product_catalog.get_product(product_id)
    assert product["stock"] == 15  # 20 - 2 - 3


def test_complete_ecommerce_workflow(user_manager, product_catalog, order_processor, email_service):
    """End-to-end test of complete ecommerce workflow."""
    # Register user
    user_id = user_manager.register_user("Eve", "eve@example.com")

    # Add multiple products
    laptop_id = product_catalog.add_product("Laptop", 1000.00, 5)
    mouse_id = product_catalog.add_product("Mouse", 25.00, 10)
    keyboard_id = product_catalog.add_product("Keyboard", 75.00, 8)

    # Create order with multiple items
    items = [
        {"product_id": laptop_id, "quantity": 1},
        {"product_id": mouse_id, "quantity": 2},
        {"product_id": keyboard_id, "quantity": 1}
    ]
    order_id = order_processor.create_order(user_id, items)

    # Verify order
    order = order_processor.get_order(order_id)
    expected_total = 1000.00 + (2 * 25.00) + 75.00  # 1125.00
    assert order["total"] == expected_total

    # Verify stock updates
    laptop = product_catalog.get_product(laptop_id)
    mouse = product_catalog.get_product(mouse_id)
    keyboard = product_catalog.get_product(keyboard_id)
    assert laptop["stock"] == 4
    assert mouse["stock"] == 8
    assert keyboard["stock"] == 7

    # Verify email notification
    assert len(email_service.sent_emails) == 1


def test_integration_error_handling(user_manager, order_processor):
    """Test error handling in integration scenarios."""
    # Test invalid user ID
    with pytest.raises(ValueError, match="User not found"):
        order_processor.create_order(999, [])

    # Test non-existent product
    user_id = user_manager.register_user("Frank", "frank@example.com")
    items = [{"product_id": 999, "quantity": 1}]
    with pytest.raises(ValueError, match="Product 999 not found"):
        order_processor.create_order(user_id, items)
