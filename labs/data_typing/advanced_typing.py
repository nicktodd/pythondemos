"""
Advanced Type Hints Lab
=======================

Implement advanced typing features.
Complete the TODO sections below.
"""

from typing import TypeVar, Generic, Protocol, List, Callable

# TODO: Define TypeVar
# T = TypeVar('T')
# K = TypeVar('K')
# V = TypeVar('V')

# TODO: Create a generic Stack[T] class
class Stack:
    """A generic stack implementation."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        # TODO: Implement push
        pass

    def pop(self):
        """Pop an item from the stack."""
        # TODO: Implement pop
        pass

    def peek(self):
        """Peek at the top item without removing it."""
        # TODO: Implement peek
        pass

    def is_empty(self):
        """Check if stack is empty."""
        # TODO: Implement is_empty
        pass

# TODO: Create a generic Cache[K, V] class
class Cache:
    """A generic cache for key-value storage."""

    def __init__(self):
        self.data = {}

    def get(self, key):
        """Get a value by key."""
        # TODO: Implement get
        pass

    def put(self, key, value):
        """Put a key-value pair in cache."""
        # TODO: Implement put
        pass

    def clear(self):
        """Clear all items from cache."""
        # TODO: Implement clear
        pass

def filter_items(items, predicate):
    """Filter items based on a predicate function."""
    # TODO: Implement filtering
    pass

# TODO: Create a Shape protocol
# class Shape(Protocol):
#     ...

# TODO: Implement Circle class
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    # TODO: Implement area method

# TODO: Implement Rectangle class
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    # TODO: Implement area method

def calculate_total_area(shapes):
    """Calculate total area of shapes."""
    # TODO: Sum areas of all shapes
    pass

def main():
    """Test your implementations."""
    # TODO: Test Stack
    # stack = Stack[int]()
    # stack.push(1)
    # stack.push(2)
    # print(stack.pop())  # Should be 2

    # TODO: Test Cache
    # cache = Cache[str, int]()
    # cache.put("key1", 42)
    # print(cache.get("key1"))  # Should be 42

    # TODO: Test filter_items
    # numbers = [1, 2, 3, 4, 5]
    # even_numbers = filter_items(numbers, lambda x: x % 2 == 0)
    # print(even_numbers)  # Should be [2, 4]

    # TODO: Test Shape protocol
    # shapes = [Circle(5), Rectangle(4, 6)]
    # total_area = calculate_total_area(shapes)
    # print(f"Total area: {total_area}")

if __name__ == "__main__":
    main()
