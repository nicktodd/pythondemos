"""
Type Checking and Validation Solution
=====================================

Complete implementation of runtime type checking and validation.
"""

from typing import Any, Dict, List, Optional, Union, get_type_hints
import inspect

class TypeValidator:
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
            if not self._validate_type(value, expected_type):
                errors.append(f"Field '{field}' has type {type(value).__name__}, expected {expected_type}")

        return errors

    def _validate_type(self, value: Any, expected_type: Any) -> bool:
        """Validate a single value against an expected type."""
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

def validate_function_call(func, *args, **kwargs):
    """Validate function arguments against type hints."""
    errors = _validate_function_args(func, *args, **kwargs)
    if errors:
        raise TypeError(f"Type validation failed: {'; '.join(errors)}")

    return func(*args, **kwargs)

def _validate_function_args(func, *args, **kwargs) -> List[str]:
    """Validate function arguments against type hints."""
    errors = []
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)

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
            if not _validate_single_type(param_value, expected_type):
                errors.append(f"Parameter '{param_name}' has type {type(param_value).__name__}, expected {expected_type}")

    return errors

def _validate_single_type(value: Any, expected_type: Any) -> bool:
    """Validate a single value against an expected type."""
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

def create_user_validator():
    """Create a validator for user data."""
    from typing import Optional
    schema = {
        'id': int,
        'name': str,
        'email': str,
        'age': Optional[int],
        'active': bool
    }
    return TypeValidator(schema)

def safe_process_data(data: Any) -> Any:
    """Safely process mixed-type data."""
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, (int, float)):
        return data * 2
    elif isinstance(data, list):
        return [safe_process_data(item) for item in data]
    elif isinstance(data, dict):
        return {key: safe_process_data(value) for key, value in data.items()}
    else:
        return str(data)

def main():
    """Test the implementations."""
    # Test TypeValidator
    print("Testing TypeValidator:")
    validator = create_user_validator()

    # Valid user
    valid_user = {
        'id': 1,
        'name': 'Alice',
        'email': 'alice@example.com',
        'age': 30,
        'active': True
    }
    errors = validator.validate(valid_user)
    print(f"Valid user errors: {errors}")

    # Invalid user
    invalid_user = {
        'id': '1',  # Should be int
        'name': 123,  # Should be str
        'email': 'alice@example.com',
        'age': '30',  # Should be int or None
        'active': 'yes'  # Should be bool
    }
    errors = validator.validate(invalid_user)
    print(f"Invalid user errors: {errors}")

    # Test validate_function_call
    print("\nTesting validate_function_call:")
    def add(a: int, b: int) -> int:
        return a + b

    def greet(name: str, age: Optional[int] = None) -> str:
        if age is not None:
            return f"Hello, {name}! You are {age}."
        return f"Hello, {name}!"

    try:
        result = validate_function_call(add, 5, 3)
        print(f"add(5, 3) = {result}")
    except TypeError as e:
        print(f"add(5, 3) failed: {e}")

    try:
        result = validate_function_call(add, "5", 3)
        print(f"add('5', 3) = {result}")
    except TypeError as e:
        print(f"add('5', 3) failed: {e}")

    try:
        result = validate_function_call(greet, "Alice", 30)
        print(f"greet('Alice', 30) = {result}")
    except TypeError as e:
        print(f"greet('Alice', 30) failed: {e}")

    try:
        result = validate_function_call(greet, "Alice", "30")
        print(f"greet('Alice', '30') = {result}")
    except TypeError as e:
        print(f"greet('Alice', '30') failed: {e}")

    # Test safe_process_data
    print("\nTesting safe_process_data:")
    test_data = [
        "hello",
        42,
        [1, 2, "three"],
        {"key": "value", "number": 123},
        True
    ]

    for data in test_data:
        result = safe_process_data(data)
        print(f"Processed {data} ({type(data).__name__}) -> {result} ({type(result).__name__})")

if __name__ == "__main__":
    main()
