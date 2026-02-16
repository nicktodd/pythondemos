"""
Collections Type Hints Lab
==========================

Implement functions using collection type hints.
Complete the TODO sections below.
"""

from typing import List, Dict, Set

def analyze_numbers(numbers: List[int]) -> Dict[str, float]:
    """Analyze a list of numbers and return statistics."""
    # TODO: Calculate min, max, and average
    # Return a dict with keys: "min", "max", "average"
    pass

def count_word_frequency(text: str) -> Dict[str, int]:
    """Count frequency of each word in text."""
    # TODO: Split text into words and count occurrences
    # Return a dict with word -> count mapping
    pass

def merge_dictionaries(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    """Merge two dictionaries, summing values for duplicate keys."""
    # TODO: Merge the dictionaries
    pass

def get_unique_items(items: List[str]) -> Set[str]:
    """Return unique items from a list."""
    # TODO: Convert list to set to get unique items
    pass

def main():
    """Test your implementations."""
    # TODO: Test analyze_numbers
    # stats = analyze_numbers([1, 2, 3, 4, 5])
    # print(stats)

    # TODO: Test count_word_frequency
    # freq = count_word_frequency("hello world hello python")
    # print(freq)

    # TODO: Test merge_dictionaries
    # merged = merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
    # print(merged)

    # TODO: Test get_unique_items
    # unique = get_unique_items(["a", "b", "a", "c", "b"])
    # print(unique)

if __name__ == "__main__":
    main()
