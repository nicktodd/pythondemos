# filepath: d:\GitRepos\Courses\pythondemos\labs\testing_and_mock\hamcrest_assertions.py
"""
PyHamcrest Assertions Lab

Rewrite tests using pyhamcrest matchers for more expressive assertions.
Complete the TODO items to use hamcrest matchers.
"""

import pytest
from hamcrest import (
    assert_that, equal_to, is_, contains_string, has_item, has_items,
    contains, has_length, greater_than, less_than, close_to,
    starts_with, ends_with, matches_regexp, all_of, any_of, not_,
    has_key, has_value, has_entry, instance_of
)


class Calculator:
    """Simple calculator for testing."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, n):
        if n < 0:
            raise ValueError("Cannot take square root of negative number")
        import math
        return math.sqrt(n)


@pytest.fixture
def calculator():
    """Calculator fixture."""
    return Calculator()


# TODO: Rewrite calculator tests using hamcrest matchers
def test_add_with_hamcrest(calculator):
    """Test addition with hamcrest matchers."""
    # TODO: Replace assert statements with hamcrest assertions
    # Example: assert_that(calculator.add(2, 3), equal_to(5))
    result = calculator.add(2, 3)
    assert result == 5  # Replace with hamcrest
    pass


def test_subtract_with_hamcrest(calculator):
    """Test subtraction with hamcrest matchers."""
    # TODO: Use hamcrest matchers
    result = calculator.subtract(5, 3)
    assert result == 2
    pass


def test_multiply_with_hamcrest(calculator):
    """Test multiplication with hamcrest matchers."""
    # TODO: Use hamcrest matchers
    result = calculator.multiply(4, 7)
    assert result == 28
    pass


def test_divide_with_hamcrest(calculator):
    """Test division with hamcrest matchers."""
    # TODO: Use close_to for floating point comparisons
    result = calculator.divide(10, 3)
    assert abs(result - 3.333333) < 0.01
    pass


def test_power_with_hamcrest(calculator):
    """Test power function with hamcrest matchers."""
    # TODO: Use hamcrest matchers
    result = calculator.power(2, 3)
    assert result == 8
    pass


def test_square_root_with_hamcrest(calculator):
    """Test square root with hamcrest matchers."""
    # TODO: Use close_to for floating point
    result = calculator.square_root(16)
    assert abs(result - 4.0) < 0.001
    pass


# TODO: Test collections with hamcrest matchers
def test_list_assertions():
    """Test list assertions with hamcrest."""
    numbers = [1, 2, 3, 4, 5]

    # TODO: Use has_item, has_items, contains, has_length
    assert 3 in numbers
    assert len(numbers) == 5
    pass


def test_dictionary_assertions():
    """Test dictionary assertions with hamcrest."""
    person = {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }

    # TODO: Use has_key, has_value, has_entry
    assert "name" in person
    assert person["age"] == 30
    pass


def test_string_assertions():
    """Test string assertions with hamcrest."""
    text = "Hello, World!"

    # TODO: Use contains_string, starts_with, ends_with
    assert "World" in text
    assert text.startswith("Hello")
    pass


# TODO: Test error conditions with hamcrest
def test_divide_by_zero_hamcrest(calculator):
    """Test division by zero with hamcrest."""
    from hamcrest import calling, raises

    # TODO: Use calling and raises matchers
    try:
        calculator.divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Cannot divide by zero" in str(e)
    pass


# TODO: Create custom matcher example
def test_custom_assertions():
    """Test custom assertions."""
    # TODO: Create a custom matcher or use complex hamcrest expressions
    # Example: assert_that(value, all_of(greater_than(0), less_than(100)))
    pass
