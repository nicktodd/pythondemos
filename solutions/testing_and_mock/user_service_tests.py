"""
User Service Tests Solution

Complete implementation of tests using fixtures for a user management system.
"""

import pytest
from unittest.mock import Mock


class UserService:
    """User management service."""

    def __init__(self, database):
        self.db = database

    def create_user(self, username, email):
        """Create a new user."""
        if self.db.user_exists(username):
            raise ValueError(f"Username {username} already exists")

        user_id = self.db.save_user(username, email)
        return user_id

    def get_user(self, user_id):
        """Get user by ID."""
        return self.db.get_user(user_id)

    def update_user(self, user_id, email):
        """Update user email."""
        if not self.db.user_exists_by_id(user_id):
            raise ValueError(f"User {user_id} not found")

        self.db.update_user(user_id, email)
        return True

    def delete_user(self, user_id):
        """Delete a user."""
        if not self.db.user_exists_by_id(user_id):
            return False

        self.db.delete_user(user_id)
        return True


@pytest.fixture
def mock_database():
    """Mock database for testing."""
    db = Mock()
    # Set up default return values
    db.user_exists.return_value = False
    db.user_exists_by_id.return_value = True
    db.save_user.return_value = 1
    db.get_user.return_value = {"id": 1, "username": "john", "email": "john@example.com"}
    db.update_user.return_value = None
    db.delete_user.return_value = None
    return db


@pytest.fixture
def user_service(mock_database):
    """UserService instance with mocked database."""
    return UserService(mock_database)


def test_create_user_success(user_service, mock_database):
    """Test successful user creation."""
    user_id = user_service.create_user("john", "john@example.com")
    assert user_id == 1
    mock_database.user_exists.assert_called_once_with("john")
    mock_database.save_user.assert_called_once_with("john", "john@example.com")


def test_create_user_username_exists(user_service, mock_database):
    """Test user creation when username already exists."""
    mock_database.user_exists.return_value = True
    with pytest.raises(ValueError, match="Username john already exists"):
        user_service.create_user("john", "john@example.com")
    mock_database.user_exists.assert_called_once_with("john")
    mock_database.save_user.assert_not_called()


def test_get_user(user_service, mock_database):
    """Test getting user by ID."""
    user = user_service.get_user(1)
    assert user == {"id": 1, "username": "john", "email": "john@example.com"}
    mock_database.get_user.assert_called_once_with(1)


def test_update_user_success(user_service, mock_database):
    """Test successful user update."""
    result = user_service.update_user(1, "newemail@example.com")
    assert result is True
    mock_database.user_exists_by_id.assert_called_once_with(1)
    mock_database.update_user.assert_called_once_with(1, "newemail@example.com")


def test_update_user_not_found(user_service, mock_database):
    """Test updating non-existent user."""
    mock_database.user_exists_by_id.return_value = False
    with pytest.raises(ValueError, match="User 1 not found"):
        user_service.update_user(1, "newemail@example.com")
    mock_database.user_exists_by_id.assert_called_once_with(1)
    mock_database.update_user.assert_not_called()


def test_delete_user_success(user_service, mock_database):
    """Test successful user deletion."""
    result = user_service.delete_user(1)
    assert result is True
    mock_database.user_exists_by_id.assert_called_once_with(1)
    mock_database.delete_user.assert_called_once_with(1)


def test_delete_user_not_found(user_service, mock_database):
    """Test deleting non-existent user."""
    mock_database.user_exists_by_id.return_value = False
    result = user_service.delete_user(1)
    assert result is False
    mock_database.user_exists_by_id.assert_called_once_with(1)
    mock_database.delete_user.assert_not_called()


@pytest.fixture(scope="module")
def shared_database():
    """Module-scoped database fixture."""
    db = Mock()
    db.user_exists.return_value = False
    db.save_user.return_value = 42
    return db


def test_create_user_with_shared_fixture(shared_database):
    """Test user creation using module-scoped fixture."""
    service = UserService(shared_database)
    user_id = service.create_user("shared_user", "shared@example.com")
    assert user_id == 42
    shared_database.user_exists.assert_called_with("shared_user")
    shared_database.save_user.assert_called_with("shared_user", "shared@example.com")


def test_another_test_with_shared_fixture(shared_database):
    """Another test using the same module-scoped fixture."""
    service = UserService(shared_database)
    user_id = service.create_user("another_user", "another@example.com")
    assert user_id == 42
    # Verify the mock was called again
    assert shared_database.user_exists.call_count == 2
    assert shared_database.save_user.call_count == 2
