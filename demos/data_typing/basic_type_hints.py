"""
Basic Type Hints Demo
=====================

This demo shows how to use basic type hints in Python for variables and functions.
Type hints help improve code readability and enable static type checking.
"""

from typing import List, Dict, Tuple

# Basic type hints for variables
name: str = "Alice"
age: int = 30
height: float = 5.8
is_student: bool = True

def greet_person(name: str, age: int) -> str:
    """Function with type hints for parameters and return value."""
    return f"Hello, {name}! You are {age} years old."

def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area with type hints."""
    return length * width

def get_user_info() -> Tuple[str, int, bool]:
    """Return multiple values with tuple type hint."""
    return "Bob", 25, False

def process_numbers(numbers: List[int]) -> Dict[str, int]:
    """Process a list of numbers and return statistics."""
    if not numbers:
        return {"count": 0, "sum": 0, "average": 0}

    total = sum(numbers)
    count = len(numbers)
    average = total // count  # Integer division for demo

    return {
        "count": count,
        "sum": total,
        "average": average
    }

def main():
    """Demonstrate basic type hints usage."""
    print("=== Basic Type Hints Demo ===\n")

    # Using typed variables
    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")
    print(f"Is student: {is_student} (type: {type(is_student).__name__})\n")

    # Using typed functions
    greeting = greet_person("Charlie", 35)
    print(f"Greeting: {greeting}")

    area = calculate_area(10.5, 20.3)
    print(f"Area: {area}")

    # Using function that returns tuple
    user_name, user_age, user_status = get_user_info()
    print(f"User info: {user_name}, {user_age}, {user_status}\n")

    # Using function with complex types
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stats = process_numbers(numbers)
    print(f"Number statistics: {stats}")

    # Demonstrate type hints don't enforce types at runtime
    print("\n=== Runtime Type Flexibility ===")
    # This works despite type hints suggesting int
    mixed_list: List[int] = [1, "hello", 3.14]  # Type hint ignored at runtime
    print(f"Mixed list (type hint says List[int]): {mixed_list}")

if __name__ == "__main__":
    main()
