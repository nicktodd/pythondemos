"""
Optional and Union Type Hints Demo
==================================

This demo shows how to use Optional and Union types for more flexible type hints.
Optional indicates a value can be None, while Union allows multiple possible types.
"""

from typing import Optional, Union, List, Dict, Any

# Optional types - can be the specified type or None
def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """Find a user by ID. Returns None if not found."""
    users = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"},
    }
    return users.get(user_id)

def get_config_value(key: str) -> Optional[str]:
    """Get configuration value. Returns None if key doesn't exist."""
    config = {
        "database_url": "sqlite:///app.db",
        "debug": "true",
    }
    return config.get(key)

# Union types - can be any of the specified types
def process_data(data: Union[str, int, float]) -> str:
    """Process data that can be string, int, or float."""
    if isinstance(data, str):
        return f"String: {data.upper()}"
    elif isinstance(data, int):
        return f"Integer: {data * 2}"
    elif isinstance(data, float):
        return f"Float: {data:.2f}"
    else:
        return f"Unknown type: {type(data).__name__}"

def calculate_discount(price: float, discount: Union[int, float, str]) -> float:
    """Calculate discounted price with flexible discount types."""
    if isinstance(discount, str):
        # Assume percentage string like "20%"
        if discount.endswith('%'):
            percentage = float(discount[:-1]) / 100
            return price * (1 - percentage)
        else:
            return price - float(discount)
    elif isinstance(discount, (int, float)):
        if discount < 1:
            # Assume decimal (0.2 = 20%)
            return price * (1 - discount)
        else:
            # Assume absolute amount
            return price - discount
    else:
        return price

# Complex unions
def handle_response(response: Union[Dict[str, Any], List[Dict[str, Any]], str]) -> str:
    """Handle different types of API responses."""
    if isinstance(response, dict):
        return f"Dict response with keys: {list(response.keys())}"
    elif isinstance(response, list):
        return f"List response with {len(response)} items"
    elif isinstance(response, str):
        return f"String response: {response}"
    else:
        return f"Unexpected response type: {type(response).__name__}"

# Optional with Union
def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Safe division that returns None if division by zero."""
    if b == 0:
        return None
    return a / b

def parse_number(value: str) -> Optional[Union[int, float]]:
    """Parse a string to number, returning None if invalid."""
    try:
        # Try int first
        if '.' not in value:
            return int(value)
        else:
            return float(value)
    except ValueError:
        return None

def validate_input(data: Dict[str, Any]) -> Optional[Dict[str, str]]:
    """Validate input data and return errors or None if valid."""
    errors = {}

    name = data.get('name')
    if not name or not isinstance(name, str) or len(name.strip()) == 0:
        errors['name'] = 'Name is required and must be a non-empty string'

    age = data.get('age')
    if age is not None:
        if not isinstance(age, int) or age < 0 or age > 150:
            errors['age'] = 'Age must be an integer between 0 and 150'

    email = data.get('email')
    if email and not isinstance(email, str):
        errors['email'] = 'Email must be a string'

    return errors if errors else None

def main():
    """Demonstrate Optional and Union type hints."""
    print("=== Optional and Union Type Hints Demo ===\n")

    # Optional examples
    print("--- Optional Types ---")
    user = find_user(1)
    print(f"User 1: {user}")

    user = find_user(999)
    print(f"User 999: {user}")

    config = get_config_value("database_url")
    print(f"Database URL: {config}")

    config = get_config_value("missing_key")
    print(f"Missing key: {config}\n")

    # Union examples
    print("--- Union Types ---")
    results = []
    for data in ["hello", 42, 3.14, True]:
        result = process_data(data)
        results.append(result)
        print(f"Processed {data}: {result}")
    print()

    # Discount calculation examples
    price = 100.0
    discounts = [0.2, 20, "15%", "5"]
    for discount in discounts:
        final_price = calculate_discount(price, discount)
        print(f"Price {price} with discount {discount}: {final_price}")
    print()

    # Complex union example
    print("--- Complex Unions ---")
    responses = [
        {"status": "success", "data": [1, 2, 3]},
        [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
        "Operation completed successfully"
    ]

    for i, response in enumerate(responses, 1):
        result = handle_response(response)
        print(f"Response {i}: {result}")
    print()

    # Safe operations
    print("--- Safe Operations ---")
    divisions = [(10, 2), (10, 0), (15, 3)]
    for a, b in divisions:
        result = safe_divide(a, b)
        print(f"{a} / {b} = {result}")

    parses = ["42", "3.14", "hello", "123abc"]
    for value in parses:
        result = parse_number(value)
        print(f"Parse '{value}': {result}")
    print()

    # Validation example
    print("--- Input Validation ---")
    test_inputs = [
        {"name": "Alice", "age": 30, "email": "alice@example.com"},
        {"name": "", "age": 25},
        {"name": "Bob", "age": -5},
        {"name": "Charlie", "age": "thirty"}
    ]

    for i, input_data in enumerate(test_inputs, 1):
        errors = validate_input(input_data)
        if errors:
            print(f"Input {i} validation errors: {errors}")
        else:
            print(f"Input {i} is valid")

if __name__ == "__main__":
    main()
