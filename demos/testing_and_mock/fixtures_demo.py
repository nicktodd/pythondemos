"""
Pytest Fixtures Demo

This module demonstrates pytest fixtures for setup and teardown:
- Function-level fixtures
- Module-level fixtures
- Class-level fixtures
- Session-level fixtures
- Fixture dependencies
- Setup and teardown
"""

import pytest
import tempfile
import os
import json


# Sample application code
class UserService:
    """Service for managing users."""

    def __init__(self, db_connection=None):
        self.db_connection = db_connection or {}
        self.users = {}

    def create_user(self, user_id, name, email):
        """Create a new user."""
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists")
        self.users[user_id] = {"name": name, "email": email}
        return user_id

    def get_user(self, user_id):
        """Get user by ID."""
        return self.users.get(user_id)

    def update_user(self, user_id, **updates):
        """Update user information."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        self.users[user_id].update(updates)
        return self.users[user_id]

    def delete_user(self, user_id):
        """Delete a user."""
        if user_id not in self.users:
            return False
        del self.users[user_id]
        return True


class FileStorage:
    """Simple file-based storage."""

    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        """Save data to file."""
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load(self):
        """Load data from file."""
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r') as f:
            return json.load(f)

    def clear(self):
        """Clear the storage file."""
        if os.path.exists(self.filename):
            os.remove(self.filename)


# Fixtures

@pytest.fixture
def calculator():
    """Fixture that provides a Calculator instance."""
    from basic_pytest import Calculator
    return Calculator()


@pytest.fixture(scope="function")
def user_service():
    """Function-scoped fixture for UserService."""
    service = UserService()
    yield service
    # Teardown: clean up any created users
    service.users.clear()


@pytest.fixture(scope="module")
def temp_file():
    """Module-scoped fixture for temporary file."""
    # Setup: create temporary file
    fd, filename = tempfile.mkstemp()
    os.close(fd)  # Close the file descriptor

    yield filename

    # Teardown: remove temporary file
    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture(scope="session")
def session_config():
    """Session-scoped fixture for configuration."""
    config = {
        "database_url": "sqlite:///test.db",
        "debug": True,
        "max_connections": 10
    }
    print(f"Setting up session config: {config}")
    yield config
    print("Tearing down session config")


@pytest.fixture
def file_storage(temp_file):
    """Fixture that depends on temp_file fixture."""
    storage = FileStorage(temp_file)
    yield storage
    # Cleanup
    storage.clear()


@pytest.fixture
def sample_users():
    """Fixture providing sample user data."""
    return [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ]


# Tests using fixtures

def test_calculator_add(calculator):
    """Test calculator addition using fixture."""
    assert calculator.add(2, 3) == 5
    assert calculator.add(0, 0) == 0


def test_calculator_multiply(calculator):
    """Test calculator multiplication using fixture."""
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10


def test_user_service_create(user_service):
    """Test user creation using UserService fixture."""
    user_id = user_service.create_user(1, "Alice", "alice@example.com")
    assert user_id == 1

    user = user_service.get_user(1)
    assert user["name"] == "Alice"
    assert user["email"] == "alice@example.com"


def test_user_service_update(user_service):
    """Test user update using UserService fixture."""
    user_service.create_user(1, "Alice", "alice@example.com")

    updated = user_service.update_user(1, name="Alice Smith", email="alice.smith@example.com")
    assert updated["name"] == "Alice Smith"
    assert updated["email"] == "alice.smith@example.com"


def test_user_service_delete(user_service):
    """Test user deletion using UserService fixture."""
    user_service.create_user(1, "Alice", "alice@example.com")

    assert user_service.delete_user(1) is True
    assert user_service.get_user(1) is None
    assert user_service.delete_user(999) is False  # Non-existent user


def test_file_storage_save_load(file_storage):
    """Test file storage using fixtures."""
    data = {"key": "value", "number": 42}

    file_storage.save(data)
    loaded = file_storage.load()

    assert loaded == data


def test_file_storage_clear(file_storage):
    """Test file storage clear functionality."""
    data = {"test": "data"}
    file_storage.save(data)

    # Verify data is saved
    assert file_storage.load() == data

    # Clear and verify
    file_storage.clear()
    assert file_storage.load() == {}


def test_multiple_users(user_service, sample_users):
    """Test creating multiple users using fixtures."""
    for user_data in sample_users:
        user_service.create_user(user_data["id"], user_data["name"], user_data["email"])

    # Verify all users were created
    for user_data in sample_users:
        user = user_service.get_user(user_data["id"])
        assert user["name"] == user_data["name"]
        assert user["email"] == user_data["email"]


def test_session_config_usage(session_config):
    """Test using session-scoped configuration."""
    assert session_config["debug"] is True
    assert session_config["max_connections"] == 10
    assert "database_url" in session_config


# Fixture with parameters
@pytest.fixture(params=["small", "medium", "large"])
def data_size(request):
    """Parameterized fixture for different data sizes."""
    sizes = {
        "small": 10,
        "medium": 100,
        "large": 1000
    }
    return sizes[request.param]


def test_data_processing_with_sizes(data_size):
    """Test data processing with different sizes."""
    # Simulate processing data of different sizes
    result = data_size * 2
    assert result == data_size * 2
    assert result > 0


# Autouse fixture
@pytest.fixture(autouse=True)
def log_test_start(request):
    """Automatically log the start of each test."""
    print(f"\nStarting test: {request.node.name}")
    yield
    print(f"Finished test: {request.node.name}")


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v", "-s"])
