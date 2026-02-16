# filepath: d:\GitRepos\Courses\pythondemos\demos\testing_and_mock\pyhamcrest_demo.py
"""
PyHamcrest Demo

This module demonstrates pyhamcrest matchers for more expressive assertions:
- Basic matchers (equal_to, is_, contains_string)
- Collection matchers (has_item, has_items, contains)
- Number matchers (greater_than, less_than, close_to)
- String matchers (starts_with, ends_with, matches_regexp)
- Logical matchers (all_of, any_of, not_)
- Custom matchers
"""

import pytest
from hamcrest import (
    assert_that, equal_to, is_, contains_string, has_item, has_items,
    contains, has_length, greater_than, less_than, close_to,
    starts_with, ends_with, matches_regexp, all_of, any_of, not_,
    has_key, has_value, has_entry, instance_of, has_property,
    calling, raises, contains_inanyorder
)
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers import wrap_matcher
import math


# Sample classes for testing
class Person:
    """Person class for testing."""

    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


class ShoppingCart:
    """Shopping cart for testing collections."""

    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        """Add item to cart."""
        self.items.append({"item": item, "price": price})

    def get_total(self):
        """Calculate total price."""
        return sum(item["price"] for item in self.items)

    def get_items(self):
        """Get all items."""
        return self.items


class Calculator:
    """Calculator for testing numeric operations."""

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square_root(self, n):
        if n < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(n)


# Basic matchers
def test_basic_matchers():
    """Test basic hamcrest matchers."""
    # equal_to matcher
    assert_that(5, equal_to(5))
    assert_that("hello", equal_to("hello"))

    # is_ matcher (alias for equal_to)
    assert_that(42, is_(42))
    assert_that(True, is_(True))

    # contains_string matcher
    assert_that("hello world", contains_string("world"))
    assert_that("python programming", contains_string("python"))


def test_calculator_with_hamcrest():
    """Test Calculator class with hamcrest matchers."""
    calc = Calculator()

    # Test addition
    assert_that(calc.add(2, 3), equal_to(5))
    assert_that(calc.add(-1, 1), is_(0))

    # Test division
    assert_that(calc.divide(10, 2), equal_to(5.0))
    assert_that(calc.divide(5, 2), close_to(2.5, 0.01))  # Close to with delta


# Collection matchers
def test_collection_matchers():
    """Test collection-related matchers."""
    numbers = [1, 2, 3, 4, 5]

    # has_item - check if collection contains specific item
    assert_that(numbers, has_item(3))
    assert_that(numbers, has_item(greater_than(4)))

    # has_items - check for multiple items
    assert_that(numbers, has_items(1, 3, 5))

    # contains - check exact order
    assert_that([1, 2, 3], contains(1, 2, 3))
    assert_that(["a", "b", "c"], contains("a", "b", "c"))

    # has_length - check collection length
    assert_that(numbers, has_length(5))
    assert_that([], has_length(0))


def test_shopping_cart():
    """Test ShoppingCart with collection matchers."""
    cart = ShoppingCart()
    cart.add_item("apple", 1.50)
    cart.add_item("banana", 0.75)
    cart.add_item("orange", 2.00)

    items = cart.get_items()

    # Check that items contain specific entries
    assert_that(items, has_item(has_entry("item", "apple")))
    assert_that(items, has_item(has_entry("price", 1.50)))

    # Check total price
    assert_that(cart.get_total(), close_to(4.25, 0.01))


# Number matchers
def test_number_matchers():
    """Test numeric matchers."""
    # greater_than, less_than
    assert_that(10, greater_than(5))
    assert_that(3, less_than(8))

    # close_to for floating point comparisons
    assert_that(3.14159, close_to(3.14, 0.01))
    assert_that(2.718, close_to(math.e, 0.001))

    # Test calculator results
    calc = Calculator()
    assert_that(calc.square_root(16), close_to(4.0, 0.001))
    assert_that(calc.divide(22, 7), close_to(3.14, 0.01))


# String matchers
def test_string_matchers():
    """Test string-related matchers."""
    text = "Hello, World!"

    # starts_with, ends_with
    assert_that(text, starts_with("Hello"))
    assert_that(text, ends_with("World!"))

    # contains_string
    assert_that(text, contains_string("World"))

    # matches_regexp
    assert_that("abc123", matches_regexp(r"\w+\d+"))
    assert_that("test@example.com", matches_regexp(r".+@.+\..+"))


# Logical matchers
def test_logical_matchers():
    """Test logical matchers: all_of, any_of, not_."""
    number = 15

    # all_of - all conditions must be true
    assert_that(number, all_of(
        greater_than(10),
        less_than(20),
        is_(15)
    ))

    # any_of - at least one condition must be true
    assert_that(number, any_of(
        equal_to(10),
        equal_to(15),
        equal_to(20)
    ))

    # not_ - negate a matcher
    assert_that(number, not_(equal_to(10)))
    assert_that("hello", not_(starts_with("world")))


# Dictionary/Object matchers
def test_dictionary_matchers():
    """Test dictionary and object matchers."""
    person_dict = {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }

    # has_key, has_value
    assert_that(person_dict, has_key("name"))
    assert_that(person_dict, has_value("Alice"))

    # has_entry - check both key and value
    assert_that(person_dict, has_entry("age", 30))

    # Check multiple entries
    assert_that(person_dict, all_of(
        has_entry("name", "Alice"),
        has_entry("email", contains_string("@"))
    ))


def test_object_matchers():
    """Test object property matchers."""
    person = Person("Bob", 25, "bob@test.com")

    # has_property
    assert_that(person, has_property("name", "Bob"))
    assert_that(person, has_property("age", greater_than(20)))

    # instance_of
    assert_that(person, instance_of(Person))
    assert_that(person.name, instance_of(str))


# Exception testing
def test_exception_matchers():
    """Test exception-related matchers."""
    calc = Calculator()

    # Test that function raises specific exception
    assert_that(
        calling(calc.divide).with_args(10, 0),
        raises(ValueError)
    )

    assert_that(
        calling(calc.square_root).with_args(-1),
        raises(ValueError, "negative")
    )


# Custom matchers
class DivisibleBy(BaseMatcher):
    """Custom matcher to check if number is divisible by another."""

    def __init__(self, divisor):
        self.divisor = divisor

    def _matches(self, item):
        return item % self.divisor == 0

    def describe_to(self, description):
        description.append_text(f"number divisible by {self.divisor}")

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text(f"{item} is not divisible by {self.divisor}")


def divisible_by(divisor):
    """Factory function for DivisibleBy matcher."""
    return DivisibleBy(divisor)


def test_custom_matcher():
    """Test custom matcher."""
    assert_that(10, divisible_by(2))
    assert_that(15, divisible_by(5))
    assert_that(7, not_(divisible_by(3)))


# Complex assertions
def test_complex_assertions():
    """Test complex assertions combining multiple matchers."""
    people = [
        Person("Alice", 30, "alice@test.com"),
        Person("Bob", 25, "bob@test.com"),
        Person("Charlie", 35, "charlie@test.com")
    ]

    # Check that list contains people with specific properties
    assert_that(people, has_item(
        all_of(
            has_property("age", greater_than(25)),
            has_property("email", contains_string("alice"))
        )
    ))

    # Check ages are all reasonable
    ages = [p.age for p in people]
    assert_that(ages, contains_inanyorder(
        all_of(greater_than(20), less_than(40)),
        all_of(greater_than(20), less_than(40)),
        all_of(greater_than(20), less_than(40))
    ))


def test_shopping_cart_complex():
    """Complex test of shopping cart."""
    cart = ShoppingCart()
    cart.add_item("laptop", 999.99)
    cart.add_item("mouse", 25.50)
    cart.add_item("keyboard", 75.00)

    # Check cart has expected items with prices in range
    assert_that(cart.get_items(), has_items(
        has_entry("price", greater_than(20)),
        has_entry("price", less_than(100)),
        has_entry("price", greater_than(900))
    ))

    # Check total is reasonable
    assert_that(cart.get_total(), all_of(
        greater_than(1000),
        less_than(1200)
    ))


# More examples with different data types
def test_mixed_types():
    """Test matchers with different data types."""
    # Lists
    fruits = ["apple", "banana", "cherry"]
    assert_that(fruits, contains("apple", "banana", "cherry"))
    assert_that(fruits, has_length(3))

    # Sets (order doesn't matter)
    colors = {"red", "green", "blue"}
    assert_that(colors, has_item("red"))
    assert_that(colors, has_length(3))

    # Tuples
    point = (3, 4)
    assert_that(point, contains(greater_than(2), less_than(5)))

    # None values
    assert_that(None, equal_to(None))
    assert_that("", not_(equal_to(None)))


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
