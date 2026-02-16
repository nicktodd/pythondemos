"""
Collections Type Hints Solution
===============================

Complete implementation of functions using collection type hints.
"""

from typing import List, Dict, Set

def analyze_numbers(numbers: List[int]) -> Dict[str, float]:
    """Analyze a list of numbers and return statistics."""
    if not numbers:
        return {"min": 0.0, "max": 0.0, "average": 0.0}

    return {
        "min": float(min(numbers)),
        "max": float(max(numbers)),
        "average": sum(numbers) / len(numbers)
    }

def count_word_frequency(text: str) -> Dict[str, int]:
    """Count frequency of each word in text."""
    words = text.lower().split()
    frequency: Dict[str, int] = {}

    for word in words:
        # Remove punctuation for cleaner counting
        clean_word = word.strip('.,!?;:')
        if clean_word:
            frequency[clean_word] = frequency.get(clean_word, 0) + 1

    return frequency

def merge_dictionaries(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    """Merge two dictionaries, summing values for duplicate keys."""
    result = dict1.copy()

    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value

    return result

def get_unique_items(items: List[str]) -> Set[str]:
    """Return unique items from a list."""
    return set(items)

def main():
    """Test the implementations."""
    # Test analyze_numbers
    numbers = [1, 2, 3, 4, 5]
    stats = analyze_numbers(numbers)
    print(f"Numbers: {numbers}")
    print(f"Statistics: {stats}")

    # Test count_word_frequency
    text = "hello world hello python world"
    freq = count_word_frequency(text)
    print(f"\nText: '{text}'")
    print(f"Word frequency: {freq}")

    # Test merge_dictionaries
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged = merge_dictionaries(dict1, dict2)
    print(f"\nDict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Merged: {merged}")

    # Test get_unique_items
    items = ["a", "b", "a", "c", "b", "d", "a"]
    unique = get_unique_items(items)
    print(f"\nOriginal items: {items}")
    print(f"Unique items: {sorted(unique)}")

if __name__ == "__main__":
    main()
