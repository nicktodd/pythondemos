"""
Basic Type Hints Lab
====================

Implement basic type hints for variables and functions.
Complete the TODO sections below.
"""

from typing import List, Dict, Tuple

# TODO: Create variables with proper type hints for different data types
# name: str = ...
# age: int = ...
# height: float = ...
# is_student: bool = ...

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters."""
    # TODO: Implement BMI calculation
    # BMI = weight / (height ^ 2)
    pass

def format_person_info(name: str, age: int, city: str) -> str:
    """Format person information into a readable string."""
    # TODO: Format the person information nicely
    pass

def is_adult(age: int) -> bool:
    """Check if a person is an adult (18 or older)."""
    # TODO: Return True if age >= 18, False otherwise
    pass

def main():
    """Test your implementations."""
    # TODO: Test calculate_bmi function
    # bmi = calculate_bmi(70.0, 1.75)
    # print(f"BMI: {bmi:.2f}")

    # TODO: Test format_person_info function
    # info = format_person_info("Alice", 30, "New York")
    # print(info)

    # TODO: Test is_adult function
    # print(is_adult(25))  # Should be True
    # print(is_adult(15))  # Should be False

if __name__ == "__main__":
    main()
