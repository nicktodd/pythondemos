# filepath: d:\GitRepos\Courses\pythondemos\demos\testing_and_mock\best_practices.py
"""
Testing Best Practices Demo

This module demonstrates best practices for testing:
- Test organization and naming
- Test isolation
- DRY principle in tests
- Test fixtures and parametrization
- Mocking best practices
- Test coverage considerations
- Performance testing
- Continuous integration considerations
"""

import pytest
import tempfile
import os
import time
from unittest.mock import Mock, patch, MagicMock
from contextlib import contextmanager
import json


# Sample application code with good testability
class UserManager:
    """User management system."""

    def __init__(self, db_connection=None, email_service=None):
        self.db = db_connection
        self.email = email_service or Mock()

    def create_user(self, username, email, password):
        """Create a new user."""
        if not username:
            raise ValueError("Username cannot be empty")

        if not self._validate_email(email):
            raise ValueError("Invalid email format")

        if self.db.user_exists(username):
            raise ValueError("Username already exists")

        user_id = self.db.save_user(username, email, password)
        self.email.send_welcome_email(email, username)

        return user_id

    def authenticate_user(self, username, password):
        """Authenticate a user."""
        user = self.db.get_user_by_username(username)
        if not user:
            return False

        if not self._verify_password(password, user['password_hash']):
            return False

        return user

    def update_user_profile(self, user_id, updates):
        """Update user profile."""
        if not self.db.user_exists_by_id(user_id):
            raise ValueError("User not found")

        # Validate updates
        allowed_fields = {'email', 'full_name', 'bio'}
        invalid_fields = set(updates.keys()) - allowed_fields
        if invalid_fields:
            raise ValueError(f"Invalid fields: {invalid_fields}")

        if 'email' in updates and not self._validate_email(updates['email']):
            raise ValueError("Invalid email format")

        self.db.update_user(user_id, updates)
        return True

    def _validate_email(self, email):
        """Validate email format."""
        return '@' in email and '.' in email

    def _verify_password(self, password, password_hash):
        """Verify password against hash."""
        # Simplified for demo
        return password == password_hash


class OrderProcessor:
    """Order processing system."""

    def __init__(self, db_connection=None, payment_service=None, inventory_service=None):
        self.db = db_connection
        self.payment = payment_service or Mock()
        self.inventory = inventory_service or Mock()

    def process_order(self, user_id, items):
        """Process an order."""
        # Validate user
        if not self.db.user_exists_by_id(user_id):
            raise ValueError("User not found")

        # Check inventory
        for item in items:
            if not self.inventory.check_availability(item['product_id'], item['quantity']):
                raise ValueError(f"Insufficient inventory for {item['product_id']}")

        # Calculate total
        total = sum(item['price'] * item['quantity'] for item in items)

        # Process payment
        payment_result = self.payment.charge_card(user_id, total)
        if not payment_result['success']:
            raise ValueError(f"Payment failed: {payment_result['error']}")

        # Create order
        order_id = self.db.create_order(user_id, items, total, payment_result['transaction_id'])

        # Update inventory
        for item in items:
            self.inventory.reduce_stock(item['product_id'], item['quantity'])

        return order_id


# Test fixtures with proper isolation
@pytest.fixture
def mock_db():
    """Mock database with proper isolation."""
    db = Mock()
    # Set up default behaviors
    db.user_exists.return_value = False
    db.user_exists_by_id.return_value = True
    db.save_user.return_value = 123
    db.get_user_by_username.return_value = {'id': 1, 'username': 'testuser', 'password_hash': 'password123'}
    return db


@pytest.fixture
def mock_email():
    """Mock email service."""
    return Mock()


@pytest.fixture
def user_manager(mock_db, mock_email):
    """UserManager with mocked dependencies."""
    return UserManager(mock_db, mock_email)


@pytest.fixture
def temp_file():
    """Create temporary file for testing."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as f:
        yield f.name
    # Cleanup
    os.unlink(f.name)


# Test classes for organization
class TestUserManager:
    """Test suite for UserManager."""

    def test_create_user_success(self, user_manager, mock_db, mock_email):
        """Test successful user creation."""
        user_id = user_manager.create_user("john_doe", "john@example.com", "password123")

        assert user_id == 123
        mock_db.save_user.assert_called_once_with("john_doe", "john@example.com", "password123")
        mock_email.send_welcome_email.assert_called_once_with("john@example.com", "john_doe")

    def test_create_user_invalid_email(self, user_manager):
        """Test user creation with invalid email."""
        with pytest.raises(ValueError, match="Invalid email format"):
            user_manager.create_user("john_doe", "invalid-email", "password123")

    def test_create_user_username_exists(self, user_manager, mock_db):
        """Test user creation when username already exists."""
        mock_db.user_exists.return_value = True

        with pytest.raises(ValueError, match="Username already exists"):
            user_manager.create_user("existing_user", "user@example.com", "password123")

    @pytest.mark.parametrize("username,email,password", [
        ("user1", "user1@test.com", "pass1"),
        ("user2", "user2@test.com", "pass2"),
        ("user3", "user3@test.com", "pass3"),
    ])
    def test_create_user_parametrized(self, user_manager, mock_db, mock_email, username, email, password):
        """Test user creation with multiple test cases."""
        user_id = user_manager.create_user(username, email, password)

        assert user_id == 123
        mock_db.save_user.assert_called_with(username, email, password)
        mock_email.send_welcome_email.assert_called_with(email, username)

    def test_authenticate_user_success(self, user_manager, mock_db):
        """Test successful user authentication."""
        result = user_manager.authenticate_user("testuser", "password123")

        assert result['username'] == 'testuser'
        mock_db.get_user_by_username.assert_called_once_with("testuser")

    def test_authenticate_user_wrong_password(self, user_manager, mock_db):
        """Test authentication with wrong password."""
        result = user_manager.authenticate_user("testuser", "wrongpassword")

        assert result is False

    def test_authenticate_user_not_found(self, user_manager, mock_db):
        """Test authentication for non-existent user."""
        mock_db.get_user_by_username.return_value = None

        result = user_manager.authenticate_user("nonexistent", "password")

        assert result is False

    def test_update_user_profile_success(self, user_manager, mock_db):
        """Test successful profile update."""
        updates = {"full_name": "John Doe", "bio": "Software developer"}

        result = user_manager.update_user_profile(1, updates)

        assert result is True
        mock_db.update_user.assert_called_once_with(1, updates)

    def test_update_user_profile_invalid_fields(self, user_manager):
        """Test profile update with invalid fields."""
        updates = {"invalid_field": "value", "email": "test@example.com"}

        with pytest.raises(ValueError, match="Invalid fields"):
            user_manager.update_user_profile(1, updates)

    def test_update_user_profile_invalid_email(self, user_manager):
        """Test profile update with invalid email."""
        updates = {"email": "invalid-email"}

        with pytest.raises(ValueError, match="Invalid email format"):
            user_manager.update_user_profile(1, updates)


class TestOrderProcessor:
    """Test suite for OrderProcessor."""

    @pytest.fixture
    def mock_payment(self):
        """Mock payment service."""
        payment = Mock()
        payment.charge_card.return_value = {"success": True, "transaction_id": "txn_123"}
        return payment

    @pytest.fixture
    def mock_inventory(self):
        """Mock inventory service."""
        inventory = Mock()
        inventory.check_availability.return_value = True
        return inventory

    @pytest.fixture
    def order_processor(self, mock_db, mock_payment, mock_inventory):
        """OrderProcessor with mocked dependencies."""
        return OrderProcessor(mock_db, mock_payment, mock_inventory)

    def test_process_order_success(self, order_processor, mock_db, mock_payment, mock_inventory):
        """Test successful order processing."""
        items = [
            {"product_id": 1, "quantity": 2, "price": 10.00},
            {"product_id": 2, "quantity": 1, "price": 25.00}
        ]

        order_id = order_processor.process_order(1, items)

        assert order_id is not None
        mock_payment.charge_card.assert_called_once_with(1, 45.00)  # 2*10 + 1*25
        mock_inventory.reduce_stock.assert_any_call(1, 2)
        mock_inventory.reduce_stock.assert_any_call(2, 1)
        mock_db.create_order.assert_called_once()

    def test_process_order_insufficient_inventory(self, order_processor, mock_inventory):
        """Test order processing with insufficient inventory."""
        mock_inventory.check_availability.return_value = False

        items = [{"product_id": 1, "quantity": 1, "price": 10.00}]

        with pytest.raises(ValueError, match="Insufficient inventory"):
            order_processor.process_order(1, items)

    def test_process_order_payment_failure(self, order_processor, mock_payment):
        """Test order processing with payment failure."""
        mock_payment.charge_card.return_value = {"success": False, "error": "Card declined"}

        items = [{"product_id": 1, "quantity": 1, "price": 10.00}]

        with pytest.raises(ValueError, match="Payment failed"):
            order_processor.process_order(1, items)


# Performance testing
def test_user_creation_performance(user_manager, benchmark):
    """Test performance of user creation."""
    def create_user():
        return user_manager.create_user("perf_test", "perf@test.com", "password")

    # Use pytest-benchmark if available
    result = benchmark(create_user)
    assert result is not None


# Test data builders for complex objects
class UserBuilder:
    """Builder for test user data."""

    def __init__(self):
        self.data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
            "full_name": "Test User"
        }

    def with_username(self, username):
        self.data["username"] = username
        return self

    def with_email(self, email):
        self.data["email"] = email
        return self

    def with_password(self, password):
        self.data["password"] = password
        return self

    def build(self):
        return self.data.copy()


@pytest.fixture
def user_builder():
    """Fixture providing user builder."""
    return UserBuilder()


def test_user_builder_usage(user_builder, user_manager):
    """Demonstrate using test data builder."""
    user_data = (user_builder
                 .with_username("builder_test")
                 .with_email("builder@test.com")
                 .build())

    user_id = user_manager.create_user(
        user_data["username"],
        user_data["email"],
        user_data["password"]
    )

    assert user_id is not None


# Context managers for test setup
@contextmanager
def user_context(user_manager, username="context_user", email="context@test.com"):
    """Context manager for user lifecycle in tests."""
    user_id = user_manager.create_user(username, email, "password")
    try:
        yield user_id
    finally:
        # Cleanup if needed
        pass


def test_user_context_manager(user_manager):
    """Test using context manager for user setup."""
    with user_context(user_manager, "context_test", "context@test.com") as user_id:
        assert user_id is not None
        # Test operations with the user
        user = user_manager.db.get_user_by_username("context_test")
        assert user is not None


# Test configuration and environment handling
@pytest.fixture
def test_config():
    """Test configuration."""
    return {
        "database_url": "sqlite:///test.db",
        "email_service_url": "https://test-email-service.com",
        "debug_mode": True
    }


def test_configuration_usage(test_config, user_manager):
    """Test that components use configuration properly."""
    # This is a demonstration - in real code, config would be passed to constructors
    assert test_config["debug_mode"] is True


# Integration test marker
@pytest.mark.integration
def test_full_user_workflow(user_manager):
    """Integration test for complete user workflow."""
    # Create user
    user_id = user_manager.create_user("workflow_user", "workflow@test.com", "password")

    # Authenticate user
    user = user_manager.authenticate_user("workflow_user", "password")
    assert user is not None

    # Update profile
    user_manager.update_user_profile(user_id, {"full_name": "Workflow User"})

    # Verify updates
    updated_user = user_manager.db.get_user_by_username("workflow_user")
    assert updated_user is not None


# Test coverage considerations
def test_error_conditions_coverage(user_manager, mock_db):
    """Test various error conditions for better coverage."""
    # Test all validation paths
    with pytest.raises(ValueError):
        user_manager.create_user("", "test@test.com", "password")  # Empty username

    with pytest.raises(ValueError):
        user_manager.create_user("user", "", "password")  # Empty email

    # Mock non-existent user
    mock_db.user_exists_by_id.return_value = False
    with pytest.raises(ValueError):
        user_manager.update_user_profile(999, {"email": "test@test.com"})  # Non-existent user


# Test isolation verification
def test_mock_isolation(user_manager, mock_db):
    """Verify that mocks are properly isolated between tests."""
    # Each test should start with fresh mocks
    initial_call_count = mock_db.save_user.call_count
    user_manager.create_user("isolation_test", "isolation@test.com", "password")

    # Verify the call was made
    assert mock_db.save_user.call_count == initial_call_count + 1


# Custom test markers
@pytest.mark.slow
def test_slow_operation():
    """Mark slow tests appropriately."""
    time.sleep(0.1)  # Simulate slow operation
    assert True


@pytest.mark.skipif(os.getenv("SKIP_NETWORK_TESTS"), reason="Network tests disabled")
def test_network_operation():
    """Conditionally skip network tests."""
    assert True


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
