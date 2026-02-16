# filepath: d:\GitRepos\Courses\pythondemos\demos\testing_and_mock\integration_testing.py
"""
Integration Testing Demo

This module demonstrates integration testing concepts:
- Testing multiple components together
- Database integration tests
- API integration tests
- File system integration
- External service integration
- Setup and teardown for integration tests
"""

import pytest
import sqlite3
import tempfile
import os
import json
from pathlib import Path
from unittest.mock import Mock, patch
import requests
from contextlib import contextmanager


# Sample application components for integration testing
class DatabaseManager:
    """Database manager for user data."""

    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Connect to database."""
        self.connection = sqlite3.connect(self.db_path)
        self._create_tables()

    def disconnect(self):
        """Disconnect from database."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def _create_tables(self):
        """Create necessary tables."""
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product TEXT NOT NULL,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        self.connection.commit()

    def create_user(self, name, email, age=None):
        """Create a new user."""
        cursor = self.connection.cursor()
        cursor.execute(
            'INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
            (name, email, age)
        )
        self.connection.commit()
        return cursor.lastrowid

    def get_user(self, user_id):
        """Get user by ID."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'age': row[3]
            }
        return None

    def create_order(self, user_id, product, quantity, price):
        """Create an order for a user."""
        cursor = self.connection.cursor()
        cursor.execute(
            'INSERT INTO orders (user_id, product, quantity, price) VALUES (?, ?, ?, ?)',
            (user_id, product, quantity, price)
        )
        self.connection.commit()
        return cursor.lastrowid

    def get_user_orders(self, user_id):
        """Get all orders for a user."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM orders WHERE user_id = ?', (user_id,))
        rows = cursor.fetchall()
        return [{
            'id': row[0],
            'user_id': row[1],
            'product': row[2],
            'quantity': row[3],
            'price': row[4]
        } for row in rows]


class EmailService:
    """Service for sending emails."""

    def __init__(self, smtp_server="smtp.example.com"):
        self.smtp_server = smtp_server
        self.sent_emails = []  # For testing purposes

    def send_welcome_email(self, email, name):
        """Send welcome email to new user."""
        subject = f"Welcome {name}!"
        body = f"Hello {name},\n\nWelcome to our platform!\n\nBest regards,\nThe Team"

        # In real implementation, this would connect to SMTP server
        self.sent_emails.append({
            'to': email,
            'subject': subject,
            'body': body
        })
        return True

    def send_order_confirmation(self, email, order_details):
        """Send order confirmation email."""
        subject = "Order Confirmation"
        body = "Your order for {} has been placed.\nQuantity: {}\nPrice: ${:.2f}\nThank you for your business!".format(order_details['product'], order_details['quantity'], order_details['price'])

        self.sent_emails.append({
            'to': email,
            'subject': subject,
            'body': body
        })
        return True


class UserService:
    """Service that coordinates user operations."""

    def __init__(self, db_manager, email_service):
        self.db = db_manager
        self.email = email_service

    def register_user(self, name, email, age=None):
        """Register a new user with database and email."""
        # Create user in database
        user_id = self.db.create_user(name, email, age)

        # Send welcome email
        self.email.send_welcome_email(email, name)

        return user_id

    def place_order(self, user_id, product, quantity, price):
        """Place an order for a user."""
        # Verify user exists
        user = self.db.get_user(user_id)
        if not user:
            raise ValueError(f"User {user_id} not found")

        # Create order
        order_id = self.db.create_order(user_id, product, quantity, price)

        # Send confirmation email
        order_details = {
            'product': product,
            'quantity': quantity,
            'price': price
        }
        self.email.send_order_confirmation(user['email'], order_details)

        return order_id


class FileProcessor:
    """Process files and store results."""

    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def process_data_file(self, input_file, output_filename):
        """Process a data file and save results."""
        # Read input file
        with open(input_file, 'r') as f:
            data = json.load(f)

        # Process data (simple example: calculate statistics)
        if 'numbers' in data:
            numbers = data['numbers']
            result = {
                'count': len(numbers),
                'sum': sum(numbers),
                'average': sum(numbers) / len(numbers) if numbers else 0,
                'min': min(numbers) if numbers else None,
                'max': max(numbers) if numbers else None
            }
        else:
            result = {'error': 'No numbers field in data'}

        # Save result
        output_path = self.output_dir / output_filename
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2)

        return str(output_path)

    def get_processed_files(self):
        """Get list of processed files."""
        return list(self.output_dir.glob("*.json"))


class APIService:
    """Service that makes external API calls."""

    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def get_post(self, post_id):
        """Get a post from the API."""
        response = requests.get(f"{self.base_url}/posts/{post_id}")
        response.raise_for_status()
        return response.json()

    def create_post(self, title, body, user_id):
        """Create a new post."""
        data = {
            'title': title,
            'body': body,
            'userId': user_id
        }
        response = requests.post(f"{self.base_url}/posts", json=data)
        response.raise_for_status()
        return response.json()


class EmailService:
    """Service for sending emails (test version that stores sent emails)."""

    def __init__(self):
        self.sent_emails = []

    def send_welcome_email(self, to_email, name):
        """Send welcome email."""
        subject = f"Welcome {name}!"
        body = f"Hello {name},\n\nWelcome to our service!\n\nBest regards,\nThe Team"
        self.sent_emails.append({
            'to': to_email,
            'subject': subject,
            'body': body
        })
        return True

    def send_order_confirmation(self, to_email, order_details):
        """Send order confirmation email."""
        subject = "Order Confirmation"
        body = "Your order for {} has been placed.\nQuantity: {}\nPrice: ${:.2f}\nThank you for your business!".format(order_details['product'], order_details['quantity'], order_details['price'])
        self.sent_emails.append({
            'to': to_email,
            'subject': subject,
            'body': body
        })
        return True


# Integration test fixtures
@pytest.fixture
def temp_db():
    """Create a temporary database for testing."""
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        db_path = f.name

    db = DatabaseManager(db_path)
    db.connect()

    yield db

    # Cleanup
    db.disconnect()
    os.unlink(db_path)


@pytest.fixture
def email_service():
    """Create email service for testing."""
    return EmailService()


@pytest.fixture
def user_service(temp_db, email_service):
    """Create user service with real dependencies."""
    return UserService(temp_db, email_service)


@pytest.fixture
def temp_dir():
    """Create temporary directory for file processing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def file_processor(temp_dir):
    """Create file processor with temporary directory."""
    return FileProcessor(temp_dir)


# Integration tests
def test_user_registration_integration(user_service, email_service):
    """Test complete user registration flow."""
    # Register a user
    user_id = user_service.register_user("Alice Johnson", "alice@example.com", 28)

    # Verify user was created in database
    user = user_service.db.get_user(user_id)
    assert user is not None
    assert user['name'] == "Alice Johnson"
    assert user['email'] == "alice@example.com"
    assert user['age'] == 28

    # Verify welcome email was sent
    assert len(email_service.sent_emails) == 1
    email = email_service.sent_emails[0]
    assert email['to'] == "alice@example.com"
    assert "Welcome Alice Johnson!" in email['subject']
    assert "Hello Alice Johnson" in email['body']


def test_order_placement_integration(user_service, email_service):
    """Test complete order placement flow."""
    # First create a user
    user_id = user_service.register_user("Bob Smith", "bob@example.com", 35)

    # Clear previous emails
    email_service.sent_emails.clear()

    # Place an order
    order_id = user_service.place_order(user_id, "Laptop", 1, 999.99)

    # Verify order was created
    orders = user_service.db.get_user_orders(user_id)
    assert len(orders) == 1
    order = orders[0]
    assert order['product'] == "Laptop"
    assert order['quantity'] == 1
    assert order['price'] == 999.99

    # Verify confirmation email was sent
    assert len(email_service.sent_emails) == 1
    email = email_service.sent_emails[0]
    assert email['to'] == "bob@example.com"
    assert email['subject'] == "Order Confirmation"
    assert "Laptop" in email['body']
    assert "999.99" in email['body']


def test_multiple_orders_integration(user_service):
    """Test placing multiple orders for the same user."""
    # Create user
    user_id = user_service.register_user("Charlie Brown", "charlie@example.com")

    # Place multiple orders
    order1_id = user_service.place_order(user_id, "Book", 2, 29.98)
    order2_id = user_service.place_order(user_id, "Pen", 5, 4.95)

    # Verify both orders exist
    orders = user_service.db.get_user_orders(user_id)
    assert len(orders) == 2

    products = [order['product'] for order in orders]
    assert "Book" in products
    assert "Pen" in products


def test_order_for_nonexistent_user(user_service):
    """Test placing order for user that doesn't exist."""
    with pytest.raises(ValueError, match="User 999 not found"):
        user_service.place_order(999, "Product", 1, 10.00)


def test_file_processing_integration(file_processor, tmp_path):
    """Test file processing workflow."""
    # Create input data file
    input_data = {
        "numbers": [10, 20, 30, 40, 50]
    }
    input_file = tmp_path / "input.json"
    with open(input_file, 'w') as f:
        json.dump(input_data, f)

    # Process the file
    output_path = file_processor.process_data_file(str(input_file), "stats.json")

    # Verify output file was created
    assert os.path.exists(output_path)

    # Verify output content
    with open(output_path, 'r') as f:
        result = json.load(f)

    assert result['count'] == 5
    assert result['sum'] == 150
    assert result['average'] == 30.0
    assert result['min'] == 10
    assert result['max'] == 50

    # Verify file is listed in processed files
    processed_files = file_processor.get_processed_files()
    assert len(processed_files) == 1
    assert processed_files[0].name == "stats.json"


def test_file_processing_invalid_data(file_processor, tmp_path):
    """Test file processing with invalid data."""
    # Create input file without numbers field
    input_data = {"invalid": "data"}
    input_file = tmp_path / "invalid.json"
    with open(input_file, 'w') as f:
        json.dump(input_data, f)

    # Process the file
    output_path = file_processor.process_data_file(str(input_file), "result.json")

    # Verify error handling
    with open(output_path, 'r') as f:
        result = json.load(f)

    assert 'error' in result
    assert 'No numbers field' in result['error']


@pytest.mark.integration
def test_api_service_integration():
    """Test API service integration with real external API."""
    api = APIService()

    # Test getting a post
    post = api.get_post(1)
    assert post['id'] == 1
    assert 'title' in post
    assert 'body' in post
    assert 'userId' in post

    # Test creating a post
    new_post = api.create_post("Test Title", "Test Body", 1)
    assert new_post['title'] == "Test Title"
    assert new_post['body'] == "Test Body"
    assert new_post['userId'] == 1
    # Note: JSONPlaceholder returns an id for created posts


def test_database_relationships(temp_db):
    """Test database relationships between users and orders."""
    # Create users
    user1_id = temp_db.create_user("User One", "user1@test.com")
    user2_id = temp_db.create_user("User Two", "user2@test.com")

    # Create orders for each user
    temp_db.create_order(user1_id, "Product A", 2, 20.00)
    temp_db.create_order(user1_id, "Product B", 1, 15.00)
    temp_db.create_order(user2_id, "Product C", 3, 30.00)

    # Verify orders are correctly associated
    user1_orders = temp_db.get_user_orders(user1_id)
    user2_orders = temp_db.get_user_orders(user2_id)

    assert len(user1_orders) == 2
    assert len(user2_orders) == 1

    # Check order details
    assert user1_orders[0]['product'] in ["Product A", "Product B"]
    assert user1_orders[1]['product'] in ["Product A", "Product B"]
    assert user2_orders[0]['product'] == "Product C"


def test_email_service_multiple_emails(email_service):
    """Test email service sending multiple emails."""
    # Send multiple emails
    email_service.send_welcome_email("user1@test.com", "User One")
    email_service.send_welcome_email("user2@test.com", "User Two")
    email_service.send_order_confirmation("user3@test.com", {
        'product': 'Test Product',
        'quantity': 1,
        'price': 10.00
    })

    # Verify all emails were sent
    assert len(email_service.sent_emails) == 3

    # Check email contents
    emails = email_service.sent_emails
    assert emails[0]['to'] == "user1@test.com"
    assert emails[1]['to'] == "user2@test.com"
    assert emails[2]['to'] == "user3@test.com"
    assert "Order Confirmation" in emails[2]['subject']


# End-to-end test combining multiple components
def test_complete_ecommerce_flow(user_service, email_service, file_processor, tmp_path):
    """End-to-end test of complete ecommerce flow."""
    # 1. Register user
    user_id = user_service.register_user("E2E User", "e2e@test.com", 25)

    # 2. Place orders
    user_service.place_order(user_id, "Widget", 2, 19.98)
    user_service.place_order(user_id, "Gadget", 1, 49.99)

    # 3. Export order data to file
    orders = user_service.db.get_user_orders(user_id)
    order_data = {
        "user_id": user_id,
        "orders": orders,
        "total_value": sum(order['price'] * order['quantity'] for order in orders)
    }

    export_file = tmp_path / "orders_export.json"
    with open(export_file, 'w') as f:
        json.dump(order_data, f)

    # 4. Process the exported file
    processed_file = file_processor.process_data_file(str(export_file), "processed_orders.json")

    # 5. Verify everything worked
    # Check user was created
    user = user_service.db.get_user(user_id)
    assert user['name'] == "E2E User"

    # Check orders were created
    assert len(orders) == 2

    # Check emails were sent (1 welcome + 2 confirmations)
    assert len(email_service.sent_emails) == 3

    # Check file processing worked
    assert os.path.exists(processed_file)

    print("End-to-end test completed successfully!")


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
