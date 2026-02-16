"""
Collections Type Hints Demo
===========================

This demo shows how to use type hints with collections like List, Dict, Tuple, and Set.
These are generic types that allow you to specify the types of elements they contain.
"""

from typing import List, Dict, Tuple, Set, Optional

# List type hints
names: List[str] = ["Alice", "Bob", "Charlie"]
numbers: List[int] = [1, 2, 3, 4, 5]
mixed_list: List[object] = ["hello", 42, 3.14]  # Can hold any type

# Dict type hints - specify key and value types
person: Dict[str, str] = {
    "name": "Alice",
    "age": "30",
    "city": "New York"
}

scores: Dict[str, int] = {
    "math": 95,
    "science": 87,
    "english": 92
}

# Nested dict
student_records: Dict[str, Dict[str, int]] = {
    "alice": {"math": 95, "science": 87},
    "bob": {"math": 78, "science": 92}
}

# Tuple type hints - specify types for each position
coordinates: Tuple[int, int] = (10, 20)
person_info: Tuple[str, int, str] = ("Alice", 30, "Engineer")
rgb_color: Tuple[int, int, int] = (255, 0, 128)

# Set type hints
unique_numbers: Set[int] = {1, 2, 3, 4, 5}
tags: Set[str] = {"python", "typing", "demo"}

def process_names(names: List[str]) -> List[str]:
    """Process a list of names and return capitalized versions."""
    return [name.upper() for name in names]

def calculate_average(scores: Dict[str, int]) -> float:
    """Calculate average from a dictionary of scores."""
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)

def get_coordinates() -> Tuple[float, float, float]:
    """Return 3D coordinates as a tuple."""
    return (10.5, 20.3, 5.7)

def find_common_elements(set1: Set[int], set2: Set[int]) -> Set[int]:
    """Find intersection of two sets."""
    return set1.intersection(set2)

def create_person_record(name: str, age: int, city: str) -> Dict[str, str]:
    """Create a person record dictionary."""
    return {
        "name": name,
        "age": str(age),
        "city": city
    }

def analyze_data(data: List[Dict[str, int]]) -> Dict[str, float]:
    """Analyze a list of dictionaries containing numeric data."""
    if not data:
        return {}

    # Extract all keys
    all_keys = set()
    for record in data:
        all_keys.update(record.keys())

    # Calculate averages for each key
    result = {}
    for key in all_keys:
        values = [record.get(key, 0) for record in data if key in record]
        if values:
            result[key] = sum(values) / len(values)

    return result

def main():
    """Demonstrate collections type hints usage."""
    print("=== Collections Type Hints Demo ===\n")

    # List operations
    print("--- Lists ---")
    processed_names = process_names(names)
    print(f"Original names: {names}")
    print(f"Processed names: {processed_names}\n")

    # Dict operations
    print("--- Dictionaries ---")
    avg_score = calculate_average(scores)
    print(f"Scores: {scores}")
    print(f"Average score: {avg_score:.2f}")

    person_record = create_person_record("David", 28, "Boston")
    print(f"Person record: {person_record}\n")

    # Tuple operations
    print("--- Tuples ---")
    coords = get_coordinates()
    print(f"3D coordinates: {coords}")
    x, y, z = coords
    print(f"Unpacked: x={x}, y={y}, z={z}\n")

    # Set operations
    print("--- Sets ---")
    common = find_common_elements({1, 2, 3, 4}, {3, 4, 5, 6})
    print(f"Common elements: {common}\n")

    # Complex data analysis
    print("--- Complex Data Analysis ---")
    sample_data = [
        {"math": 85, "science": 92},
        {"math": 78, "science": 88, "english": 95},
        {"math": 92, "english": 87}
    ]
    analysis = analyze_data(sample_data)
    print(f"Sample data: {sample_data}")
    print(f"Analysis results: {analysis}")

if __name__ == "__main__":
    main()
