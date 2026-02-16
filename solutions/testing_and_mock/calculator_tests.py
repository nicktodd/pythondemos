"""
Calculator Tests Solution

Complete implementation of comprehensive tests for the Calculator class.
"""

import pytest
import math


class Calculator:
    """Simple calculator class for testing."""

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

    def square_root(self, n):
        """Calculate square root."""
        if n < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(n)


def test_add():
    """Test the add method."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    assert calc.add(1.5, 2.5) == 4.0
    assert calc.add(-5, -3) == -8


def test_subtract():
    """Test the subtract method."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(1.5, 0.5) == 1.0
    assert calc.subtract(-5, -3) == -2


def test_multiply():
    """Test the multiply method."""
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0
    assert calc.multiply(1.5, 2) == 3.0
    assert calc.multiply(-2, -3) == 6


def test_divide():
    """Test the divide method."""
    calc = Calculator()
    assert calc.divide(6, 3) == 2
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 3) == -2
    assert calc.divide(1.5, 0.5) == 3.0
    assert calc.divide(-6, -3) == 2


def test_divide_by_zero():
    """Test division by zero raises error."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


def test_power():
    """Test the power method."""
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2, -1) == 0.5
    assert calc.power(-2, 2) == 4
    assert calc.power(-2, 3) == -8


def test_square_root():
    """Test the square_root method."""
    calc = Calculator()
    assert calc.square_root(4) == 2
    assert calc.square_root(9) == 3
    assert calc.square_root(0) == 0
    assert calc.square_root(2) == pytest.approx(1.414, rel=1e-3)
    assert calc.square_root(1.21) == 1.1


def test_square_root_negative():
    """Test square root of negative number raises error."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot take square root of negative number"):
        calc.square_root(-1)


def test_add_large_numbers():
    """Test addition with large numbers."""
    calc = Calculator()
    assert calc.add(1000000, 2000000) == 3000000


def test_multiply_floats():
    """Test multiplication with floating point precision."""
    calc = Calculator()
    result = calc.multiply(0.1, 0.2)
    assert result == pytest.approx(0.02, rel=1e-10)


def test_power_edge_cases():
    """Test power function edge cases."""
    calc = Calculator()
    assert calc.power(0, 5) == 0
    assert calc.power(1, 100) == 1
    assert calc.power(-1, 0) == 1
