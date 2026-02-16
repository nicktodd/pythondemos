"""
Advanced Type Hints Demo
========================

This demo covers advanced typing features like generics, protocols, and type variables.
These features provide more sophisticated type checking and better code documentation.
"""

from typing import TypeVar, Generic, Protocol, List, Dict, Optional, Union, Callable, Any
from abc import ABC, abstractmethod
import math

# TypeVar for generics
T = TypeVar('T')  # Generic type
K = TypeVar('K')  # Key type
V = TypeVar('V')  # Value type

# Constrained TypeVar
NumberType = TypeVar('NumberType', int, float, complex)

# Protocol for structural typing (duck typing)
class SupportsComparison(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

class SupportsLength(Protocol):
    def __len__(self) -> int: ...

# Generic classes
class Stack(Generic[T]):
    """A generic stack implementation."""

    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self) -> Optional[T]:
        """Pop an item from the stack."""
        return self.items.pop() if self.items else None

    def peek(self) -> Optional[T]:
        """Peek at the top item without removing it."""
        return self.items[-1] if self.items else None

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Get stack size."""
        return len(self.items)

class Pair(Generic[K, V]):
    """A generic pair class."""

    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

    def get_key(self) -> K:
        return self.key

    def get_value(self) -> V:
        return self.value

    def swap(self) -> 'Pair[V, K]':
        """Return a new pair with key and value swapped."""
        return Pair(self.value, self.key)

# Generic functions
def reverse_list(items: List[T]) -> List[T]:
    """Reverse a list of any type."""
    return items[::-1]

def find_max(items: List[SupportsComparison]) -> Optional[Any]:
    """Find maximum item in a list of comparable items."""
    if not items:
        return None
    return max(items)

def get_length(obj: SupportsLength) -> int:
    """Get length of any object that supports len()."""
    return len(obj)

def map_function(items: List[T], func: Callable[[T], V]) -> List[V]:
    """Apply a function to each item in a list."""
    return [func(item) for item in items]

def filter_items(items: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """Filter items based on a predicate function."""
    return [item for item in items if predicate(item)]

# Advanced generic function
def group_by_key(items: List[T], key_func: Callable[[T], K]) -> Dict[K, List[T]]:
    """Group items by a key function."""
    groups: Dict[K, List[T]] = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

# Protocol-based classes
class Shape(Protocol):
    """Protocol for shapes that can calculate area."""

    def area(self) -> float: ...

class Drawable(Protocol):
    """Protocol for objects that can be drawn."""

    def draw(self) -> str: ...

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def draw(self) -> str:
        return f"Drawing circle with radius {self.radius}"

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def draw(self) -> str:
        return f"Drawing rectangle {self.width}x{self.height}"

# Functions using protocols
def calculate_total_area(shapes: List[Shape]) -> float:
    """Calculate total area of shapes."""
    return sum(shape.area() for shape in shapes)

def render_shapes(drawables: List[Drawable]) -> str:
    """Render multiple drawable objects."""
    return "\n".join(drawable.draw() for drawable in drawables)

# Mathematical operations with constrained TypeVar
def add_numbers(a: NumberType, b: NumberType) -> NumberType:
    """Add two numbers of the same numeric type."""
    return a + b

def multiply_by_two(value: NumberType) -> NumberType:
    """Multiply a number by two."""
    return value * 2

def main():
    """Demonstrate advanced type hints."""
    print("=== Advanced Type Hints Demo ===\n")

    # Generic Stack
    print("--- Generic Stack ---")
    int_stack = Stack[int]()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"Stack size: {int_stack.size()}")
    print(f"Top item: {int_stack.peek()}")
    print(f"Popped: {int_stack.pop()}")
    print(f"Stack size after pop: {int_stack.size()}\n")

    str_stack = Stack[str]()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"String stack: {str_stack.items}")
    print(f"Reversed: {reverse_list(str_stack.items)}\n")

    # Generic Pair
    print("--- Generic Pair ---")
    pair = Pair("name", "Alice")
    print(f"Original pair: {pair.get_key()} -> {pair.get_value()}")
    swapped = pair.swap()
    print(f"Swapped pair: {swapped.get_key()} -> {swapped.get_value()}\n")

    # Protocol examples
    print("--- Protocols ---")
    shapes: List[Shape] = [
        Circle(5.0),
        Rectangle(4.0, 6.0),
        Circle(3.0)
    ]
    total_area = calculate_total_area(shapes)
    print(f"Total area of shapes: {total_area:.2f}\n")

    drawables: List[Drawable] = [
        Circle(2.0),
        Rectangle(3.0, 4.0)
    ]
    print("Rendering shapes:")
    print(render_shapes(drawables))
    print()

    # Function with protocols
    print("--- Protocol-based Functions ---")
    print(f"Length of list: {get_length([1, 2, 3, 4, 5])}")
    print(f"Length of string: {get_length('hello world')}")
    print(f"Length of dict: {get_length({'a': 1, 'b': 2})}\n")

    # Generic functions
    print("--- Generic Functions ---")
    numbers = [1, 2, 3, 4, 5]
    doubled = map_function(numbers, lambda x: x * 2)
    print(f"Original: {numbers}")
    print(f"Doubled: {doubled}")

    even_numbers = filter_items(numbers, lambda x: x % 2 == 0)
    print(f"Even numbers: {even_numbers}\n")

    # Grouping example
    print("--- Grouping ---")
    people = [
        {"name": "Alice", "age": 30, "city": "NYC"},
        {"name": "Bob", "age": 25, "city": "LA"},
        {"name": "Charlie", "age": 35, "city": "NYC"},
        {"name": "David", "age": 28, "city": "LA"}
    ]

    grouped_by_city = group_by_key(people, lambda p: p["city"])
    print("People grouped by city:")
    for city, city_people in grouped_by_city.items():
        names = [p["name"] for p in city_people]
        print(f"  {city}: {names}")
    print()

    # Constrained TypeVar
    print("--- Constrained TypeVar ---")
    print(f"Add integers: {add_numbers(5, 3)}")
    print(f"Add floats: {add_numbers(5.5, 3.2)}")
    print(f"Multiply by two: {multiply_by_two(21)}")
    print(f"Multiply float by two: {multiply_by_two(3.14)}\n")

    # Comparison protocol
    print("--- Comparison Protocol ---")
    values = [3, 1, 4, 1, 5, 9, 2, 6]
    max_value = find_max(values)
    print(f"Maximum value in {values}: {max_value}")

    strings = ["apple", "banana", "cherry"]
    max_string = find_max(strings)
    print(f"Maximum string in {strings}: {max_string}")

if __name__ == "__main__":
    main()
