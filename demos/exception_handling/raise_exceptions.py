# Raising Exceptions

def validate_age(age):
    """Demonstrate raising exceptions for validation"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot be greater than 150")

    print(f"Age {age} is valid")
    return True

def divide_with_validation(a, b):
    """Demonstrate raising exceptions with custom messages"""
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be a number, got {type(a)}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be a number, got {type(b)}")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    result = a / b
    print(f"{a} / {b} = {result}")
    return result

def check_password_strength(password):
    """Demonstrate raising exceptions for business logic"""
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit")

    print("Password is strong enough")
    return True

def re_raise_exception():
    """Demonstrate re-raising exceptions"""
    try:
        risky_operation()
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        # Add context and re-raise
        raise ValueError(f"Operation failed due to: {e}") from e

def risky_operation():
    """Helper function that raises an exception"""
    raise ValueError("Something went wrong in risky operation")

# Test the functions
if __name__ == "__main__":
    print("=== Raising Exceptions Demo ===\n")

    # Age validation
    try:
        validate_age(25)
        validate_age(-5)
    except (TypeError, ValueError) as e:
        print(f"Validation error: {e}")

    try:
        validate_age("twenty")
    except (TypeError, ValueError) as e:
        print(f"Validation error: {e}")

    print()

    # Division with validation
    try:
        divide_with_validation(10, 2)
        divide_with_validation(10, 0)
    except (TypeError, ZeroDivisionError) as e:
        print(f"Division error: {e}")

    print()

    # Password strength
    passwords = ["weak", "Strong123", "weakpass"]
    for pwd in passwords:
        try:
            check_password_strength(pwd)
        except ValueError as e:
            print(f"Password '{pwd}' failed: {e}")

    print()

    # Re-raising
    try:
        re_raise_exception()
    except ValueError as e:
        print(f"Re-raised error: {e}")
