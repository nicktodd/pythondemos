"""
Type Checking and Validation Demo
==================================

This demo shows how to use type checking tools and runtime type validation
in Python. It covers mypy static type checking and runtime type validation.
"""

import sys
from typing import List, Dict, Optional, Union, Any, get_type_hints
import inspect

# Runtime type checking utilities
def validate_type(value: Any, expected_type: Any) -> bool:
    """Basic runtime type validation."""
    try:
        # Handle Union types
        if hasattr(expected_type, '__origin__') and expected_type.__origin__ is Union:
            return any(isinstance(value, t) for t in expected_type.__args__)
        # Handle Optional (Union with None)
        elif hasattr(expected_type, '__origin__') and expected_type.__origin__ is Union:
            if type(None) in expected_type.__args__:
                if value is None:
                    return True
                non_none_types = [t for t in expected_type.__args__ if t is not type(None)]
                return any(isinstance(value, t) for t in non_none_types)
        # Regular type checking
        else:
            return isinstance(value, expected_type)
    except:
        return False

def validate_function_args(func, *args, **kwargs) -> List[str]:
    """Validate function arguments against type hints."""
    errors = []
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)

    # Bind arguments
    try:
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
    except TypeError as e:
        errors.append(f"Argument binding error: {e}")
        return errors

    # Check each parameter
    for param_name, param_value in bound_args.arguments.items():
        if param_name in type_hints:
            expected_type = type_hints[param_name]
            if not validate_type(param_value, expected_type):
                errors.append(f"Parameter '{param_name}' has type {type(param_value).__name__}, expected {expected_type}")

    return errors

# Example functions with type hints for validation
def add_numbers(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def greet_user(name: str, age: Optional[int] = None) -> str:
    """Greet a user with optional age."""
    if age is not None:
        return f"Hello, {name}! You are {age} years old."
    return f"Hello, {name}!"

def process_items(items: List[Union[str, int]]) -> str:
    """Process a list of strings or integers."""
    processed = []
    for item in items:
        if isinstance(item, str):
            processed.append(item.upper())
        elif isinstance(item, int):
            processed.append(str(item * 2))
    return ", ".join(processed)

def find_user(users: List[Dict[str, Any]], user_id: int) -> Optional[Dict[str, Any]]:
    """Find user by ID."""
    for user in users:
        if user.get('id') == user_id:
            return user
    return None

# Type-safe wrapper
def type_safe_call(func, *args, **kwargs):
    """Call a function with type checking."""
    errors = validate_function_args(func, *args, **kwargs)
    if errors:
        raise TypeError(f"Type validation failed: {'; '.join(errors)}")

    return func(*args, **kwargs)

# Data validation class
class DataValidator:
    """Runtime data validator using type hints."""

    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema

    def validate(self, data: Dict[str, Any]) -> List[str]:
        """Validate data against schema."""
        errors = []

        for field, expected_type in self.schema.items():
            if field not in data:
                errors.append(f"Missing required field: {field}")
                continue

            value = data[field]
            if not validate_type(value, expected_type):
                errors.append(f"Field '{field}' has type {type(value).__name__}, expected {expected_type}")

        return errors

# Example usage
def create_user_validator():
    """Create a validator for user data."""
    schema = {
        'id': int,
        'name': str,
        'email': str,
        'age': Optional[int],
        'active': bool
    }
    return DataValidator(schema)

def demonstrate_static_typing():
    """Demonstrate concepts that would be caught by static type checkers like mypy."""
    print("=== Static Type Checking Concepts ===\n")

    # These would be caught by mypy but run fine in Python
    print("--- Type Inconsistencies (mypy would warn) ---")

    # Wrong type assignment (mypy would warn)
    user_id: int = "123"  # Should be int, but assigned str
    print(f"User ID (wrong type): {user_id}")

    # Wrong return type (mypy would warn)
    def get_count() -> int:
        return "five"  # Should return int, but returns str

    result = get_count()
    print(f"Count result (wrong type): {result}")

    # Wrong parameter type (mypy would warn)
    def multiply(a: int, b: int) -> int:
        return a * b

    # This call would be flagged by mypy
    wrong_result = multiply("2", 3)  # First arg should be int
    print(f"Multiply result (wrong args): {wrong_result}")
    print()

def main():
    """Demonstrate type checking and validation."""
    print("=== Type Checking and Validation Demo ===\n")

    # Runtime type validation
    print("--- Runtime Type Validation ---")

    # Test function argument validation
    print("Testing function argument validation:")

    # Valid calls
    try:
        result = type_safe_call(add_numbers, 5, 3)
        print(f"✓ add_numbers(5, 3) = {result}")
    except TypeError as e:
        print(f"✗ add_numbers(5, 3) failed: {e}")

    # Invalid calls
    try:
        result = type_safe_call(add_numbers, "5", 3)
        print(f"✓ add_numbers('5', 3) = {result}")
    except TypeError as e:
        print(f"✗ add_numbers('5', 3) failed: {e}")

    try:
        result = type_safe_call(greet_user, "Alice", 30)
        print(f"✓ greet_user('Alice', 30) = {result}")
    except TypeError as e:
        print(f"✗ greet_user('Alice', 30) failed: {e}")

    try:
        result = type_safe_call(greet_user, "Alice", "30")
        print(f"✓ greet_user('Alice', '30') = {result}")
    except TypeError as e:
        print(f"✗ greet_user('Alice', '30') failed: {e}")
    print()

    # Data validation
    print("--- Data Validation ---")
    validator = create_user_validator()

    # Valid data
    valid_user = {
        'id': 1,
        'name': 'Alice',
        'email': 'alice@example.com',
        'age': 30,
        'active': True
    }

    errors = validator.validate(valid_user)
    if errors:
        print(f"✗ Valid user validation failed: {errors}")
    else:
        print("✓ Valid user data passed validation")

    # Invalid data
    invalid_user = {
        'id': '1',  # Should be int
        'name': 123,  # Should be str
        'email': 'alice@example.com',
        'age': '30',  # Should be int or None
        'active': 'yes'  # Should be bool
    }

    errors = validator.validate(invalid_user)
    if errors:
        print(f"✗ Invalid user validation failed as expected: {errors}")
    else:
        print("✗ Invalid user data unexpectedly passed validation")
    print()

    # Complex function validation
    print("--- Complex Function Validation ---")
    test_items = ["hello", 42, "world", 15]
    try:
        result = type_safe_call(process_items, test_items)
        print(f"✓ process_items({test_items}) = {result}")
    except TypeError as e:
        print(f"✗ process_items failed: {e}")

    # Test find_user
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]

    try:
        user = type_safe_call(find_user, users, 2)
        print(f"✓ find_user(users, 2) = {user}")
    except TypeError as e:
        print(f"✗ find_user failed: {e}")
    print()

    # Demonstrate static typing concepts
    demonstrate_static_typing()

    # Type hints introspection
    print("--- Type Hints Introspection ---")
    print(f"add_numbers type hints: {get_type_hints(add_numbers)}")
    print(f"greet_user type hints: {get_type_hints(greet_user)}")
    print(f"process_items type hints: {get_type_hints(process_items)}")

    # Note about mypy
    print("\n=== Note about Static Type Checking ===")
    print("To use static type checking with mypy:")
    print("1. Install mypy: pip install mypy")
    print("2. Run: mypy filename.py")
    print("3. Mypy will catch type inconsistencies at development time")
    print("\nExample mypy command:")
    print("mypy demos/data_typing/type_checking.py")

if __name__ == "__main__":
    main()
