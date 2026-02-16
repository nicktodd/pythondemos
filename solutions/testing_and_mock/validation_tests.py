"""
Validation Tests Solution

Complete implementation of parametrized tests for data validation functions.
"""

import pytest


def validate_email(email):
    """Validate email format."""
    if not email or "@" not in email:
        return False
    local, domain = email.split("@", 1)
    if not local or not domain or "." not in domain:
        return False
    return True


def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_upper and has_lower and has_digit and has_special


def validate_age(age):
    """Validate age."""
    try:
        age_num = int(age)
        return 0 <= age_num <= 150
    except (ValueError, TypeError):
        return False


@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("test.email+tag@domain.co.uk", True),
    ("user.name@subdomain.example.org", True),
    ("invalid-email", False),
    ("user@", False),
    ("@domain.com", False),
    ("", False),
    ("user@.com", False),
    ("user..double@domain.com", False),
])
def test_validate_email(email, expected):
    """Test email validation with multiple cases."""
    assert validate_email(email) == expected


@pytest.mark.parametrize("password,expected", [
    ("StrongPass123!", True),
    ("Password123!", True),
    ("MySecure789#", True),
    ("weak", False),
    ("password", False),
    ("PASSWORD", False),
    ("12345678", False),
    ("!@#$%^&*", False),
    ("Short1!", False),
    ("nouppercase123!", False),
    ("NOLOWERCASE123!", False),
    ("NoDigits!", False),
    ("NoSpecial123", False),
])
def test_validate_password(password, expected):
    """Test password validation with multiple cases."""
    assert validate_password(password) == expected


@pytest.mark.parametrize("age,expected", [
    (25, True),
    (0, True),
    (150, True),
    (18, True),
    (65, True),
    (-5, False),
    (200, False),
    (-1, False),
    (151, False),
    ("25", True),
    ("0", True),
    ("150", True),
    ("not_a_number", False),
    ("", False),
    (None, False),
])
def test_validate_age(age, expected):
    """Test age validation with multiple cases."""
    assert validate_age(age) == expected


@pytest.mark.parametrize("email,expected", [
    pytest.param("user@example.com", True, id="valid_gmail"),
    pytest.param("test.email+tag@domain.co.uk", True, id="valid_complex"),
    pytest.param("user.name@subdomain.example.org", True, id="valid_subdomain"),
    pytest.param("invalid-email", False, id="missing_at"),
    pytest.param("user@", False, id="missing_domain"),
    pytest.param("@domain.com", False, id="missing_local"),
    pytest.param("", False, id="empty_string"),
    pytest.param("user@.com", False, id="invalid_domain"),
    pytest.param("user..double@domain.com", False, id="double_dot"),
    pytest.param("very.long.email.address@very.long.domain.name.com", True, id="very_long_valid"),
], ids=lambda param: f"email_{param}")
def test_validate_email_with_ids(email, expected):
    """Test email validation with custom test IDs."""
    assert validate_email(email) == expected


def test_validate_email_edge_cases():
    """Test email validation edge cases."""
    # Very long email
    long_email = "a" * 64 + "@" + "b" * 63 + ".com"
    assert validate_email(long_email) == True

    # Email with special characters
    assert validate_email("user+tag@example.com") == True
    assert validate_email("user-tag@example.com") == True
    assert validate_email("user_tag@example.com") == True

    # Invalid special characters
    assert validate_email("user space@example.com") == False
    assert validate_email("user<test>@example.com") == False


def test_validate_password_edge_cases():
    """Test password validation edge cases."""
    # Passwords with only numbers
    assert validate_password("12345678") == False

    # Passwords with only special characters
    assert validate_password("!@#$%^&*") == False

    # Passwords with only uppercase
    assert validate_password("UPPERCASE") == False

    # Passwords with only lowercase
    assert validate_password("lowercase") == False

    # Valid passwords with different special characters
    assert validate_password("Password1@") == True
    assert validate_password("Password1#") == True
    assert validate_password("Password1$") == True

    # Exactly 8 characters
    assert validate_password("Pass123!") == True

    # Very long password
    long_password = "A" + "a" * 6 + "1!"
    assert validate_password(long_password) == True
