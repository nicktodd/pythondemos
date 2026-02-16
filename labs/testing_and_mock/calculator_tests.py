# filepath: d:\GitRepos\Courses\pythondemos\labs\testing_and_mock\calculator_tests.py
"""
Calculator Tests Lab

Implement a Calculator class and comprehensive tests.
Complete the TODO items to create working tests.
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


# TODO: Implement comprehensive tests for the Calculator class
# Test all methods with various inputs
# Test error conditions
# Use appropriate assertions

def test_add():
    """Test the add method."""
    calc = Calculator()
    # TODO: Implement test cases for addition
    pass


def test_subtract():
    """Test the subtract method."""
    calc = Calculator()
    # TODO: Implement test cases for subtraction
    pass


def test_multiply():
    """Test the multiply method."""
    calc = Calculator()
    # TODO: Implement test cases for multiplication
    pass


def test_divide():
    """Test the divide method."""
    calc = Calculator()
    # TODO: Implement test cases for division
    pass


def test_divide_by_zero():
    """Test division by zero raises error."""
    calc = Calculator()
    # TODO: Test that division by zero raises ValueError
    pass


def test_power():
    """Test the power method."""
    calc = Calculator()
    # TODO: Implement test cases for power function
    pass


def test_square_root():
    """Test the square_root method."""
    calc = Calculator()
    # TODO: Implement test cases for square root
    pass


def test_square_root_negative():
    """Test square root of negative number raises error."""
    calc = Calculator()
    # TODO: Test that square root of negative raises ValueError
    pass


# TODO: Add more test cases for edge cases and boundary conditions
# Consider testing with floating point numbers, large numbers, etc.
