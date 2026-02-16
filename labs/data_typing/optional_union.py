"""
Optional and Union Types Lab
============================

Implement functions using Optional and Union types.
Complete the TODO sections below.
"""

from typing import Optional, Union, List

def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Safely divide a by b, returning None if division by zero."""
    # TODO: Implement safe division
    # Return None if b is 0, otherwise return a / b
    pass

def parse_number(value: str) -> Optional[Union[int, float]]:
    """Parse a string to a number (int or float)."""
    # TODO: Try to parse as int first, then as float
    # Return None if parsing fails
    pass

def find_in_list(items: List[str], target: str) -> Optional[int]:
    """Find the index of target in items list."""
    # TODO: Return index if found, None if not found
    pass

def validate_email(email: Union[str, None]) -> bool:
    """Validate email format (basic validation)."""
    # TODO: Check if email is not None and contains @ and .
    pass

def main():
    """Test your implementations."""
    # TODO: Test safe_divide
    # print(safe_divide(10, 2))  # Should be 5.0
    # print(safe_divide(10, 0))  # Should be None

    # TODO: Test parse_number
    # print(parse_number("42"))    # Should be 42
    # print(parse_number("3.14"))  # Should be 3.14
    # print(parse_number("hello")) # Should be None

    # TODO: Test find_in_list
    # print(find_in_list(["a", "b", "c"], "b"))  # Should be 1
    # print(find_in_list(["a", "b", "c"], "z"))  # Should be None

    # TODO: Test validate_email
    # print(validate_email("alice@example.com"))  # Should be True
    # print(validate_email("invalid-email"))      # Should be False
    # print(validate_email(None))                 # Should be False

if __name__ == "__main__":
    main()
