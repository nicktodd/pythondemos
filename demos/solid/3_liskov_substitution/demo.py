# Liskov Substitution Principle (LSP)
# Subtypes must be substitutable for their base types

from abc import ABC, abstractmethod

# BAD: Square breaks the behavior expected from Rectangle
class BadRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height


class BadSquare(BadRectangle):
    """This violates LSP - it changes the behavior of set_width/set_height"""
    def set_width(self, width):
        self.width = width
        self.height = width  # Forces height to match width
    
    def set_height(self, height):
        self.width = height  # Forces width to match height
        self.height = height


def bad_process_rectangle(rectangle: BadRectangle):
    """This function expects normal rectangle behavior"""
    rectangle.set_width(5)
    rectangle.set_height(4)
    expected_area = 5 * 4  # 20
    actual_area = rectangle.get_area()
    
    print(f"Expected area: {expected_area}, Actual area: {actual_area}")
    assert actual_area == expected_area, "Area calculation is wrong!"


# GOOD: Use composition and abstraction instead of inheritance
class Shape(ABC):
    """Abstract base class for all shapes"""
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    """Rectangle with independent width and height"""
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def get_area(self):
        return self._width * self._height
    
    def __repr__(self):
        return f"Rectangle({self._width}x{self._height})"


class Square(Shape):
    """Square with a single side length - NOT a subtype of Rectangle"""
    def __init__(self, side):
        self._side = side
    
    def get_area(self):
        return self._side * self._side
    
    def __repr__(self):
        return f"Square({self._side}x{self._side})"


def process_shape(shape: Shape):
    """Works with any Shape - no unexpected behavior"""
    print(f"{shape} has area: {shape.get_area()}")


# Usage
if __name__ == "__main__":
    print("=== Bad Example - Violates LSP ===")
    bad_rect = BadRectangle(0, 0)
    print("Processing Rectangle:")
    bad_process_rectangle(bad_rect)
    
    print("\nProcessing Square (breaks expectations!):")
    bad_square = BadSquare(0)
    try:
        bad_process_rectangle(bad_square)  # This will fail!
    except AssertionError as e:
        print(f"ERROR: {e}")
        print("Square changed width AND height when we only set one!")
    
    print("\n=== Good Example - Follows LSP ===")
    shapes = [
        Rectangle(5, 4),
        Square(5),
        Rectangle(3, 7),
        Square(3)
    ]
    
    for shape in shapes:
        process_shape(shape)  # All shapes work correctly
    
    print("\nNo surprises! Each shape behaves as expected.")
