"""
PyHamcrest Assertions Solution

Complete implementation of tests using pyhamcrest matchers for more expressive assertions.
"""

import pytest
from hamcrest import (
    assert_that, equal_to, is_, contains_string, has_item, has_items,
    contains, has_length, greater_than, less_than, close_to,
    starts_with, ends_with, matches_regexp, all_of, any_of, not_,
    has_key, has_value, has_entry, instance_of, calling, raises
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


def test_add_with_hamcrest(calculator):
    """Test addition with hamcrest matchers."""
    assert_that(calculator.add(2, 3), equal_to(5))
    assert_that(calculator.add(-1, 1), equal_to(0))
    assert_that(calculator.add(0, 0), equal_to(0))


def test_subtract_with_hamcrest(calculator):
    """Test subtraction with hamcrest matchers."""
    assert_that(calculator.subtract(5, 3), equal_to(2))
    assert_that(calculator.subtract(3, 5), equal_to(-2))
    assert_that(calculator.subtract(10, 10), equal_to(0))


def test_multiply_with_hamcrest(calculator):
    """Test multiplication with hamcrest matchers."""
    assert_that(calculator.multiply(4, 7), equal_to(28))
    assert_that(calculator.multiply(-3, 5), equal_to(-15))
    assert_that(calculator.multiply(0, 100), equal_to(0))


def test_divide_with_hamcrest(calculator):
    """Test division with hamcrest matchers."""
    assert_that(calculator.divide(10, 3), close_to(3.333333, 0.01))
    assert_that(calculator.divide(15, 5), equal_to(3.0))
    assert_that(calculator.divide(-10, 2), equal_to(-5.0))


def test_power_with_hamcrest(calculator):
    """Test power function with hamcrest matchers."""
    assert_that(calculator.power(2, 3), equal_to(8))
    assert_that(calculator.power(5, 0), equal_to(1))
    assert_that(calculator.power(-2, 2), equal_to(4))


def test_square_root_with_hamcrest(calculator):
    """Test square root with hamcrest matchers."""
    assert_that(calculator.square_root(16), close_to(4.0, 0.001))
    assert_that(calculator.square_root(9), equal_to(3.0))
    assert_that(calculator.square_root(2), close_to(1.414213, 0.001))


def test_list_assertions():
    """Test list assertions with hamcrest."""
    numbers = [1, 2, 3, 4, 5]

    assert_that(numbers, has_item(3))
    assert_that(numbers, has_items(1, 5))
    assert_that(numbers, contains(1, 2, 3, 4, 5))
    assert_that(numbers, has_length(5))
    assert_that(numbers, has_length(greater_than(3)))


def test_dictionary_assertions():
    """Test dictionary assertions with hamcrest."""
    person = {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }

    assert_that(person, has_key("name"))
    assert_that(person, has_value("Alice"))
    assert_that(person, has_entry("age", 30))
    assert_that(person, has_key(all_of(starts_with("n"), ends_with("e"))))


def test_string_assertions():
    """Test string assertions with hamcrest."""
    text = "Hello, World!"

    assert_that(text, contains_string("World"))
    assert_that(text, starts_with("Hello"))
    assert_that(text, ends_with("!"))
    assert_that(text, matches_regexp(r"Hello.*World.*!"))


def test_divide_by_zero_hamcrest(calculator):
    """Test division by zero with hamcrest."""
    assert_that(calling(calculator.divide).with_args(10, 0),
                raises(ValueError, "Cannot divide by zero"))


def test_custom_assertions():
    """Test custom assertions."""
    # Test with complex hamcrest expressions
    value = 50
    assert_that(value, all_of(greater_than(0), less_than(100)))

    # Test with any_of
    assert_that(value, any_of(equal_to(50), equal_to(25)))

    # Test with not_
    assert_that(value, is_(not_(equal_to(25))))

    # Test instance type
    assert_that(value, instance_of(int))

    # Complex list assertions
    numbers = [10, 20, 30, 40, 50]
    assert_that(numbers, all_of(
        has_length(5),
        contains(greater_than(5), greater_than(15), greater_than(25), greater_than(35), greater_than(45))
    ))


def test_complex_hamcrest_expressions():
    """Test more complex hamcrest expressions."""
    data = {
        "users": [
            {"name": "Alice", "age": 25, "active": True},
            {"name": "Bob", "age": 30, "active": False},
            {"name": "Charlie", "age": 35, "active": True}
        ],
        "total": 3
    }

    # Test nested structures
    assert_that(data, has_entry("total", equal_to(3)))
    assert_that(data["users"], has_length(3))
    assert_that(data["users"], has_item(has_entry("name", "Alice")))
    assert_that(data["users"], has_item(has_entry("active", True)))

    # Test with logical operators
    assert_that(25, all_of(greater_than(20), less_than(30), instance_of(int)))


def test_error_assertions_with_hamcrest():
    """Test error assertions using hamcrest."""
    calculator = Calculator()

    # Test that calling square_root with negative number raises ValueError
    assert_that(calling(calculator.square_root).with_args(-1),
                raises(ValueError))

    # Test specific error message
    assert_that(calling(calculator.divide).with_args(10, 0),
                raises(ValueError, contains_string("divide by zero")))
