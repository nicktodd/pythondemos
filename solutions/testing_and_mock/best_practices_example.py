"""
Best Practices Testing Solution

Complete implementation of testing best practices for a complex system.
"""

import pytest
import time
from unittest.mock import Mock, patch


class UserManager:
    """User management system for testing best practices."""

    def __init__(self, database):
        self.database = database

    def create_user(self, username, email, password):
        """Create a new user."""
        if self.database.user_exists(username):
            raise ValueError("User already exists")
        if not self._validate_email(email):
            raise ValueError("Invalid email")
        if not self._validate_password(password):
            raise ValueError("Invalid password")

        user_id = self.database.save_user(username, email, password)
        return user_id

    def get_user(self, user_id):
        """Get user by ID."""
        return self.database.get_user(user_id)

    def update_user(self, user_id, **updates):
        """Update user information."""
        return self.database.update_user(user_id, **updates)

    def delete_user(self, user_id):
        """Delete a user."""
        return self.database.delete_user(user_id)

    def _validate_email(self, email):
        """Validate email format."""
        return "@" in email and "." in email

    def _validate_password(self, password):
        """Validate password strength."""
        return len(password) >= 8


class OrderProcessor:
    """Order processing system."""

    def __init__(self, database, payment_service, email_service):
        self.database = database
        self.payment_service = payment_service
        self.email_service = email_service

    def process_order(self, user_id, items, payment_info):
        """Process a complete order."""
        # Validate user
        user = self.database.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        # Calculate total
        total = sum(item['price'] * item['quantity'] for item in items)

        # Process payment
        payment_result = self.payment_service.charge(payment_info, total)
        if not payment_result['success']:
            raise ValueError("Payment failed")

        # Save order
        order_id = self.database.save_order(user_id, items, total, payment_result['transaction_id'])

        # Send confirmation email
        self.email_service.send_order_confirmation(user['email'], order_id, items, total)

        return order_id


class UserBuilder:
    """Test data builder for users."""

    def __init__(self):
        self.username = "testuser"
        self.email = "test@example.com"
        self.password = "password123"

    def with_username(self, username):
        self.username = username
        return self

    def with_email(self, email):
        self.email = email
        return self

    def with_password(self, password):
        self.password = password
        return self

    def build(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }


class TestUserManagement:
    """Test user management functionality."""

    @pytest.fixture
    def mock_database(self):
        """Mock database for testing."""
        db = Mock()
        db.user_exists.return_value = False
        db.save_user.return_value = 1
        db.get_user.return_value = {"id": 1, "username": "testuser", "email": "test@example.com"}
        db.update_user.return_value = True
        db.delete_user.return_value = True
        return db

    @pytest.fixture
    def user_manager(self, mock_database):
        """User manager instance."""
        return UserManager(mock_database)

    @pytest.fixture
    def user_builder(self):
        """User builder for test data."""
        return UserBuilder()

    def test_user_creation_success(self, user_manager, user_builder, mock_database):
        """Test successful user creation."""
        user_data = user_builder.with_email("john@example.com").build()
        user_id = user_manager.create_user(user_data['username'], user_data['email'], user_data['password'])
        assert user_id == 1
        mock_database.user_exists.assert_called_once_with(user_data['username'])
        mock_database.save_user.assert_called_once_with(user_data['username'], user_data['email'], user_data['password'])

    def test_user_creation_duplicate_username(self, user_manager, user_builder, mock_database):
        """Test user creation with duplicate username."""
        mock_database.user_exists.return_value = True
        user_data = user_builder.build()

        with pytest.raises(ValueError, match="User already exists"):
            user_manager.create_user(user_data['username'], user_data['email'], user_data['password'])

        mock_database.user_exists.assert_called_once_with(user_data['username'])
        mock_database.save_user.assert_not_called()

    def test_user_creation_invalid_email(self, user_manager, user_builder):
        """Test user creation with invalid email."""
        user_data = user_builder.with_email("invalid-email").build()

        with pytest.raises(ValueError, match="Invalid email"):
            user_manager.create_user(user_data['username'], user_data['email'], user_data['password'])

    def test_user_creation_weak_password(self, user_manager, user_builder):
        """Test user creation with weak password."""
        user_data = user_builder.with_password("weak").build()

        with pytest.raises(ValueError, match="Invalid password"):
            user_manager.create_user(user_data['username'], user_data['email'], user_data['password'])

    def test_get_user(self, user_manager, mock_database):
        """Test getting user by ID."""
        user = user_manager.get_user(1)
        assert user["username"] == "testuser"
        assert user["email"] == "test@example.com"
        mock_database.get_user.assert_called_once_with(1)

    def test_update_user(self, user_manager, mock_database):
        """Test updating user information."""
        result = user_manager.update_user(1, email="new@example.com")
        assert result is True
        mock_database.update_user.assert_called_once_with(1, email="new@example.com")

    def test_delete_user(self, user_manager, mock_database):
        """Test deleting a user."""
        result = user_manager.delete_user(1)
        assert result is True
        mock_database.delete_user.assert_called_once_with(1)


class TestOrderProcessing:
    """Test order processing functionality."""

    @pytest.fixture
    def mock_database(self):
        """Mock database for testing."""
        db = Mock()
        db.get_user.return_value = {'id': 1, 'email': 'test@example.com'}
        db.save_order.return_value = 100
        return db

    @pytest.fixture
    def mock_payment_service(self):
        """Mock payment service."""
        payment = Mock()
        payment.charge.return_value = {'success': True, 'transaction_id': 'txn_123'}
        return payment

    @pytest.fixture
    def mock_email_service(self):
        """Mock email service."""
        return Mock()

    @pytest.fixture
    def order_processor(self, mock_database, mock_payment_service, mock_email_service):
        """Order processor instance."""
        return OrderProcessor(mock_database, mock_payment_service, mock_email_service)

    def test_successful_order_processing(self, order_processor, mock_database, mock_payment_service, mock_email_service):
        """Test successful order processing."""
        items = [
            {'price': 10.0, 'quantity': 2},
            {'price': 5.0, 'quantity': 1}
        ]
        payment_info = {'card_number': '4111111111111111'}

        order_id = order_processor.process_order(1, items, payment_info)

        assert order_id == 100
        mock_database.get_user.assert_called_once_with(1)
        mock_payment_service.charge.assert_called_once_with(payment_info, 25.0)  # (2*10) + (1*5)
        mock_database.save_order.assert_called_once_with(1, items, 25.0, 'txn_123')
        mock_email_service.send_order_confirmation.assert_called_once_with('test@example.com', 100, items, 25.0)

    def test_order_processing_user_not_found(self, order_processor, mock_database):
        """Test order processing when user not found."""
        mock_database.get_user.return_value = None
        items = [{'price': 10.0, 'quantity': 1}]
        payment_info = {'card_number': '4111111111111111'}

        with pytest.raises(ValueError, match="User not found"):
            order_processor.process_order(999, items, payment_info)

        mock_database.get_user.assert_called_once_with(999)
        mock_database.save_order.assert_not_called()

    def test_order_processing_payment_failed(self, order_processor, mock_payment_service):
        """Test order processing when payment fails."""
        mock_payment_service.charge.return_value = {'success': False, 'error': 'Insufficient funds'}
        items = [{'price': 100.0, 'quantity': 1}]
        payment_info = {'card_number': '4000000000000002'}

        with pytest.raises(ValueError, match="Payment failed"):
            order_processor.process_order(1, items, payment_info)

        mock_payment_service.charge.assert_called_once_with(payment_info, 100.0)


@pytest.mark.performance
def test_bulk_operations_performance():
    """Test performance of bulk operations."""
    # Mock database for performance testing
    db = Mock()
    db.user_exists.return_value = False
    db.save_user.return_value = 1

    user_manager = UserManager(db)

    # Test creating multiple users
    start_time = time.time()
    users_created = 0
    for i in range(100):
        try:
            user_manager.create_user(f"user_{i}", f"user_{i}@example.com", "password123")
            users_created += 1
        except:
            pass

    end_time = time.time()
    duration = end_time - start_time

    # Should create 100 users quickly (less than 1 second)
    assert users_created == 100
    assert duration < 1.0, f"Bulk operations took {duration:.2f} seconds, expected < 1.0"


@pytest.mark.integration
def test_end_to_end_user_workflow():
    """Test end-to-end user workflow."""
    # Create mock services
    db = Mock()
    db.user_exists.return_value = False
    db.save_user.return_value = 1
    db.get_user.return_value = {"id": 1, "username": "e2e_user", "email": "e2e@example.com"}

    payment_service = Mock()
    payment_service.charge.return_value = {"success": True, "transaction_id": "e2e_txn_123"}

    email_service = Mock()

    # Create components
    user_manager = UserManager(db)
    order_processor = OrderProcessor(db, payment_service, email_service)

    # End-to-end workflow
    # 1. Create user
    user_id = user_manager.create_user("e2e_user", "e2e@example.com", "securepass123")
    assert user_id == 1

    # 2. Retrieve user
    user = user_manager.get_user(user_id)
    assert user["username"] == "e2e_user"

    # 3. Process order
    items = [{"price": 50.0, "quantity": 2}, {"price": 25.0, "quantity": 1}]
    payment_info = {"card_number": "4111111111111111"}

    order_id = order_processor.process_order(user_id, items, payment_info)
    assert order_id == 100

    # 4. Verify all interactions
    assert db.user_exists.call_count >= 1
    assert db.save_user.call_count == 1
    assert db.get_user.call_count >= 2  # Once in user_manager, once in order_processor
    assert payment_service.charge.call_count == 1
    assert email_service.send_order_confirmation.call_count == 1


@pytest.mark.slow
def test_comprehensive_error_handling():
    """Test comprehensive error handling scenarios."""
    db = Mock()
    payment_service = Mock()
    email_service = Mock()

    user_manager = UserManager(db)
    order_processor = OrderProcessor(db, payment_service, email_service)

    # Test multiple error scenarios
    error_scenarios = [
        # (user_exists, email_valid, password_valid, expected_error)
        (True, True, True, "User already exists"),
        (False, False, True, "Invalid email"),
        (False, True, False, "Invalid password"),
    ]

    for user_exists, email_valid, password_valid, expected_error in error_scenarios:
        db.reset_mock()
        db.user_exists.return_value = user_exists

        email = "valid@example.com" if email_valid else "invalid"
        password = "validpassword123" if password_valid else "weak"

        with pytest.raises(ValueError, match=expected_error):
            user_manager.create_user("testuser", email, password)


@pytest.mark.parametrize("username,email,password,should_succeed", [
    ("validuser", "valid@example.com", "strongpass123", True),
    ("user2", "user2@test.com", "anotherpass456", True),
    ("edge_case", "a@b.co", "12345678", True),
])
def test_parametrized_user_creation(username, email, password, should_succeed):
    """Test user creation with parametrized inputs."""
    db = Mock()
    db.user_exists.return_value = False
    db.save_user.return_value = 1

    user_manager = UserManager(db)

    if should_succeed:
        user_id = user_manager.create_user(username, email, password)
        assert user_id == 1
    else:
        with pytest.raises(ValueError):
            user_manager.create_user(username, email, password)
