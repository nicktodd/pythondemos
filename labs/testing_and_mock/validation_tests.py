# filepath: d:\GitRepos\Courses\pythondemos\labs\testing_and_mock\validation_tests.py
"""
Validation Tests Lab

Create parametrized tests for data validation functions.
Complete the TODO items to implement validation functions and tests.
"""

import pytest


# TODO: Implement validation functions
def validate_email(email):
    """Validate email format."""
    # TODO: Implement email validation logic
    # Should return True for valid emails, False for invalid
    pass


def validate_password(password):
    """Validate password strength."""
    # TODO: Implement password validation
    # Should check minimum length, special characters, etc.
    pass


def validate_age(age):
    """Validate age."""
    # TODO: Implement age validation
    # Should check if age is reasonable (0-150)
    pass


# TODO: Create parametrized tests for email validation
@pytest.mark.parametrize("email,expected", [
    # TODO: Add test cases for valid emails
    # ("user@example.com", True),
    # ("invalid-email", False),
    # TODO: Add more test cases
])
def test_validate_email(email, expected):
    """Test email validation with multiple cases."""
    assert validate_email(email) == expected


# TODO: Create parametrized tests for password validation
@pytest.mark.parametrize("password,expected", [
    # TODO: Add test cases for password validation
    # ("StrongPass123!", True),
    # ("weak", False),
    # TODO: Add more test cases
])
def test_validate_password(password, expected):
    """Test password validation with multiple cases."""
    assert validate_password(password) == expected


# TODO: Create parametrized tests for age validation
@pytest.mark.parametrize("age,expected", [
    # TODO: Add test cases for age validation
    # (25, True),
    # (-5, False),
    # (200, False),
    # TODO: Add more test cases
])
def test_validate_age(age, expected):
    """Test age validation with multiple cases."""
    assert validate_age(age) == expected


# TODO: Add custom test IDs for better readability
@pytest.mark.parametrize("email,expected", [
    pytest.param("user@example.com", True, id="valid_gmail"),
    pytest.param("test.email+tag@domain.co.uk", True, id="valid_complex"),
    pytest.param("invalid-email", False, id="missing_at"),
    pytest.param("user@", False, id="missing_domain"),
    pytest.param("", False, id="empty_string"),
    # TODO: Add more test cases with descriptive IDs
], ids=lambda param: f"email_{param}")
def test_validate_email_with_ids(email, expected):
    """Test email validation with custom test IDs."""
    assert validate_email(email) == expected


# TODO: Add edge case tests
def test_validate_email_edge_cases():
    """Test email validation edge cases."""
    # TODO: Test very long emails, special characters, etc.
    pass


def test_validate_password_edge_cases():
    """Test password validation edge cases."""
    # TODO: Test passwords with only numbers, only special chars, etc.
    pass
