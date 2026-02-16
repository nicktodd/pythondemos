"""
Basic Type Hints Solution
=========================

Complete implementation of basic type hints for variables and functions.
"""

from typing import List, Dict, Tuple

# Variables with proper type hints
name: str = "Alice"
age: int = 30
height: float = 5.8
is_student: bool = True

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters."""
    return weight_kg / (height_m ** 2)

def format_person_info(name: str, age: int, city: str) -> str:
    """Format person information into a readable string."""
    return f"{name} is {age} years old and lives in {city}."

def is_adult(age: int) -> bool:
    """Check if a person is an adult (18 or older)."""
    return age >= 18

def main():
    """Test the implementations."""
    # Test calculate_bmi function
    bmi = calculate_bmi(70.0, 1.75)
    print(f"BMI: {bmi:.2f}")

    # Test format_person_info function
    info = format_person_info("Alice", 30, "New York")
    print(info)

    # Test is_adult function
    print(f"Is 25 an adult? {is_adult(25)}")  # Should be True
    print(f"Is 15 an adult? {is_adult(15)}")  # Should be False

    # Demonstrate type hints
    print(f"\nVariable types:")
    print(f"name: {name} (type: {type(name).__name__})")
    print(f"age: {age} (type: {type(age).__name__})")
    print(f"height: {height} (type: {type(height).__name__})")
    print(f"is_student: {is_student} (type: {type(is_student).__name__})")

if __name__ == "__main__":
    main()
