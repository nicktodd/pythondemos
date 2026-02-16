# filepath: d:\GitRepos\Courses\pythondemos\labs\testing_and_mock\user_service_tests.py
"""
User Service Tests Lab

Implement tests using fixtures for a user management system.
Complete the TODO items to create working tests with fixtures.
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


# TODO: Create mock database fixture
@pytest.fixture
def mock_database():
    """Mock database for testing."""
    # TODO: Create a mock database with necessary methods
    # db = Mock()
    # Set up default return values
    # return db
    pass


# TODO: Create user service fixture
@pytest.fixture
def user_service(mock_database):
    """UserService instance with mocked database."""
    # TODO: Create UserService with mock database
    pass


# TODO: Implement comprehensive tests for UserService
def test_create_user_success(user_service, mock_database):
    """Test successful user creation."""
    # TODO: Test user creation with valid data
    # Verify database calls
    pass


def test_create_user_username_exists(user_service, mock_database):
    """Test user creation when username already exists."""
    # TODO: Test error when username exists
    pass


def test_get_user(user_service, mock_database):
    """Test getting user by ID."""
    # TODO: Test retrieving user data
    pass


def test_update_user_success(user_service, mock_database):
    """Test successful user update."""
    # TODO: Test updating user email
    pass


def test_update_user_not_found(user_service, mock_database):
    """Test updating non-existent user."""
    # TODO: Test error when user doesn't exist
    pass


def test_delete_user_success(user_service, mock_database):
    """Test successful user deletion."""
    # TODO: Test deleting existing user
    pass


def test_delete_user_not_found(user_service, mock_database):
    """Test deleting non-existent user."""
    # TODO: Test deleting user that doesn't exist
    pass


# TODO: Add module-scoped fixture example
@pytest.fixture(scope="module")
def shared_database():
    """Module-scoped database fixture."""
    # TODO: Create a shared mock database for multiple tests
    pass


# TODO: Add tests that use the module-scoped fixture
