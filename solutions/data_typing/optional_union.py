"""
Optional and Union Types Solution
=================================

Complete implementation of functions using Optional and Union types.
"""

from typing import Optional, Union, List

def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Safely divide a by b, returning None if division by zero."""
    if b == 0:
        return None
    return float(a) / float(b)

def parse_number(value: str) -> Optional[Union[int, float]]:
    """Parse a string to a number (int or float)."""
    try:
        # Try int first
        if '.' not in value and 'e' not in value.lower():
            return int(value)
        else:
            return float(value)
    except ValueError:
        return None

def find_in_list(items: List[str], target: str) -> Optional[int]:
    """Find the index of target in items list."""
    try:
        return items.index(target)
    except ValueError:
        return None

def validate_email(email: Union[str, None]) -> bool:
    """Validate email format (basic validation)."""
    if email is None:
        return False

    email = email.strip()
    if not email or '@' not in email or '.' not in email:
        return False

    # Basic check: @ and . exist, and @ comes before .
    at_index = email.find('@')
    dot_index = email.rfind('.')

    return at_index > 0 and dot_index > at_index + 1

def main():
    """Test the implementations."""
    # Test safe_divide
    print("Testing safe_divide:")
    print(f"10 / 2 = {safe_divide(10, 2)}")  # Should be 5.0
    print(f"10 / 0 = {safe_divide(10, 0)}")  # Should be None
    print(f"7.5 / 3 = {safe_divide(7.5, 3)}")  # Should be 2.5

    # Test parse_number
    print("\nTesting parse_number:")
    test_values = ["42", "3.14", "hello", "123abc", "1e10"]
    for value in test_values:
        result = parse_number(value)
        print(f"'{value}' -> {result} (type: {type(result).__name__ if result is not None else 'None'})")

    # Test find_in_list
    print("\nTesting find_in_list:")
    items = ["apple", "banana", "cherry", "date"]
    targets = ["banana", "grape", "apple", "cherry"]
    for target in targets:
        index = find_in_list(items, target)
        print(f"Find '{target}' in {items}: index {index}")

    # Test validate_email
    print("\nTesting validate_email:")
    emails = [
        "alice@example.com",
        "bob.smith@company.org",
        "invalid-email",
        "missing@dot",
        "@missinguser.com",
        None,
        "",
        "user@domain"
    ]
    for email in emails:
        is_valid = validate_email(email)
        print(f"'{email}' -> {'Valid' if is_valid else 'Invalid'}")

if __name__ == "__main__":
    main()
