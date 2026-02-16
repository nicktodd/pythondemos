"""
Advanced Type Hints Solution
===========================

Complete implementation of advanced typing features.
"""

from typing import TypeVar, Generic, Protocol, List, Callable
import math

# Type variables
T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

# Generic Stack class
class Stack(Generic[T]):
    """A generic stack implementation."""

    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self) -> T:
        """Pop an item from the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self) -> T:
        """Peek at the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Get the size of the stack."""
        return len(self.items)

# Generic Cache class
class Cache(Generic[K, V]):
    """A generic cache for key-value storage."""

    def __init__(self):
        self.data: dict[K, V] = {}

    def get(self, key: K) -> V:
        """Get a value by key."""
        if key not in self.data:
            raise KeyError(f"Key {key} not found in cache")
        return self.data[key]

    def put(self, key: K, value: V) -> None:
        """Put a key-value pair in cache."""
        self.data[key] = value

    def clear(self) -> None:
        """Clear all items from cache."""
        self.data.clear()

    def contains(self, key: K) -> bool:
        """Check if key exists in cache."""
        return key in self.data

# Generic filter function
def filter_items(items: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """Filter items based on a predicate function."""
    return [item for item in items if predicate(item)]

# Shape protocol
class Shape(Protocol):
    """Protocol for shapes that can calculate area."""

    def area(self) -> float:
        """Calculate the area of the shape."""
        ...

# Circle class implementing Shape
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"

# Rectangle class implementing Shape
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

def calculate_total_area(shapes: List[Shape]) -> float:
    """Calculate total area of shapes."""
    return sum(shape.area() for shape in shapes)

def find_largest_shape(shapes: List[Shape]) -> Shape:
    """Find the shape with the largest area."""
    if not shapes:
        raise ValueError("No shapes provided")
    return max(shapes, key=lambda s: s.area())

def main():
    """Test the implementations."""
    # Test Stack
    print("Testing Stack:")
    int_stack = Stack[int]()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"Stack size: {int_stack.size()}")
    print(f"Top item: {int_stack.peek()}")
    print(f"Popped: {int_stack.pop()}")
    print(f"Stack size after pop: {int_stack.size()}")

    str_stack = Stack[str]()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"String stack popped: {str_stack.pop()}")

    # Test Cache
    print("\nTesting Cache:")
    str_int_cache = Cache[str, int]()
    str_int_cache.put("key1", 42)
    str_int_cache.put("key2", 100)
    print(f"key1 = {str_int_cache.get('key1')}")
    print(f"key2 = {str_int_cache.get('key2')}")
    print(f"Contains 'key1': {str_int_cache.contains('key1')}")
    str_int_cache.clear()
    print(f"Cache size after clear: {len(str_int_cache.data)}")

    # Test filter_items
    print("\nTesting filter_items:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_items(numbers, lambda x: x % 2 == 0)
    odd_numbers = filter_items(numbers, lambda x: x % 2 != 0)
    large_numbers = filter_items(numbers, lambda x: x > 5)

    print(f"Original: {numbers}")
    print(f"Even: {even_numbers}")
    print(f"Odd: {odd_numbers}")
    print(f"Large (>5): {large_numbers}")

    # Test Shape protocol
    print("\nTesting Shape Protocol:")
    shapes: List[Shape] = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Circle(3.0),
        Rectangle(2.0, 8.0)
    ]

    print("Shapes:")
    for shape in shapes:
        print(f"  {shape} -> Area: {shape.area():.2f}")

    total_area = calculate_total_area(shapes)
    print(f"Total area: {total_area:.2f}")

    largest = find_largest_shape(shapes)
    print(f"Largest shape: {largest} (area: {largest.area():.2f})")

if __name__ == "__main__":
    main()
