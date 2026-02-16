"""
Basic Pytest Demo

This module demonstrates basic pytest usage including:
- Simple test functions
- Assertions
- Test discovery
- Running tests
"""

import pytest


# Sample code to test
class Calculator:
    """Simple calculator class for demonstration."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        """Calculate power."""
        return base ** exponent


# Test functions
def test_add():
    """Test the add method."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_subtract():
    """Test the subtract method."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(0, 5) == -5


def test_multiply():
    """Test the multiply method."""
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0


def test_divide():
    """Test the divide method."""
    calc = Calculator()
    assert calc.divide(6, 2) == 3.0
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(0, 5) == 0.0


def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


def test_power():
    """Test the power method."""
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(10, 1) == 10


def test_assertion_examples():
    """Demonstrate different types of assertions."""
    # Basic assertions
    assert True
    assert not False

    # Comparison assertions
    assert 5 > 3
    assert 3 <= 5
    assert "hello" == "hello"
    assert "hello" != "world"

    # Membership assertions
    assert 1 in [1, 2, 3]
    assert "a" in "abc"
    assert 5 not in [1, 2, 3]

    # Type assertions
    assert isinstance(42, int)
    assert isinstance("hello", str)

    # Length assertions
    assert len([1, 2, 3]) == 3
    assert len("hello") == 5


def test_failing_test_example():
    """This test will fail to demonstrate pytest output."""
    # Uncomment the line below to see a failing test
    # assert 2 + 2 == 5, "This should fail"


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
