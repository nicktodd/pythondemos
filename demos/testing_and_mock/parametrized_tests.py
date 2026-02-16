# filepath: d:\GitRepos\Courses\pythondemos\demos\testing_and_mock\parametrized_tests.py
"""
Parametrized Tests Demo

This module demonstrates parametrized tests in pytest:
- @pytest.mark.parametrize decorator
- Multiple parameters
- Parameterized fixtures
- Id functions for test names
- Skipping and conditional tests
"""

import pytest
import math


# Sample code to test
class MathUtils:
    """Utility class for mathematical operations."""

    @staticmethod
    def factorial(n):
        """Calculate factorial of n."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * MathUtils.factorial(n - 1)

    @staticmethod
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def fibonacci(n):
        """Calculate nth Fibonacci number."""
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def gcd(a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        """Calculate least common multiple."""
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // MathUtils.gcd(a, b)


class StringUtils:
    """Utility class for string operations."""

    @staticmethod
    def reverse_string(s):
        """Reverse a string."""
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        """Check if string is a palindrome."""
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def count_vowels(s):
        """Count vowels in a string."""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)

    @staticmethod
    def capitalize_words(s):
        """Capitalize first letter of each word."""
        return ' '.join(word.capitalize() for word in s.split())


# Parametrized tests for MathUtils
@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_factorial(n, expected):
    """Test factorial function with multiple inputs."""
    assert MathUtils.factorial(n) == expected


@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
    (11, True),
    (13, True),
    (17, True),
])
def test_is_prime(n, expected):
    """Test prime checking with various numbers."""
    assert MathUtils.is_prime(n) == expected


@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (10, 55),
])
def test_fibonacci(n, expected):
    """Test Fibonacci sequence calculation."""
    assert MathUtils.fibonacci(n) == expected


@pytest.mark.parametrize("a,b,expected", [
    (12, 18, 6),
    (100, 75, 25),
    (7, 3, 1),
    (1, 1, 1),
    (0, 5, 5),
    (5, 0, 5),
])
def test_gcd(a, b, expected):
    """Test GCD calculation with multiple pairs."""
    assert MathUtils.gcd(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (4, 5, 20),
    (3, 7, 21),
    (6, 8, 24),
    (1, 1, 1),
    (0, 5, 0),
    (5, 0, 0),
])
def test_lcm(a, b, expected):
    """Test LCM calculation."""
    assert MathUtils.lcm(a, b) == expected


# Parametrized tests for StringUtils
@pytest.mark.parametrize("input_str,expected", [
    ("hello", "olleh"),
    ("", ""),
    ("a", "a"),
    ("12345", "54321"),
    ("Python", "nohtyP"),
])
def test_reverse_string(input_str, expected):
    """Test string reversal."""
    assert StringUtils.reverse_string(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [
    ("radar", True),
    ("A man a plan a canal Panama", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("Racecar", True),
    ("Python", False),
])
def test_is_palindrome(input_str, expected):
    """Test palindrome checking."""
    assert StringUtils.is_palindrome(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [
    ("hello", 2),
    ("aeiou", 5),
    ("bcdfg", 0),
    ("", 0),
    ("AEIOU", 5),
    ("Hello World", 3),
])
def test_count_vowels(input_str, expected):
    """Test vowel counting."""
    assert StringUtils.count_vowels(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [
    ("hello world", "Hello World"),
    ("python programming", "Python Programming"),
    ("", ""),
    ("a", "A"),
    ("multiple   spaces", "Multiple Spaces"),
])
def test_capitalize_words(input_str, expected):
    """Test word capitalization."""
    assert StringUtils.capitalize_words(input_str) == expected


# Parametrized tests with custom IDs
@pytest.mark.parametrize("n,expected", [
    pytest.param(0, 1, id="zero"),
    pytest.param(1, 1, id="one"),
    pytest.param(5, 120, id="five"),
    pytest.param(10, 3628800, id="ten"),
], ids=lambda param: f"factorial_of_{param}")
def test_factorial_with_ids(n, expected):
    """Test factorial with custom test IDs."""
    assert MathUtils.factorial(n) == expected


# Parametrized tests with error cases
@pytest.mark.parametrize("n", [-1, -5, -10])
def test_factorial_negative_raises_error(n):
    """Test that factorial raises error for negative numbers."""
    with pytest.raises(ValueError, match="not defined for negative numbers"):
        MathUtils.factorial(n)


@pytest.mark.parametrize("n", [-1, -5, -10])
def test_fibonacci_negative_raises_error(n):
    """Test that fibonacci raises error for negative numbers."""
    with pytest.raises(ValueError, match="not defined for negative numbers"):
        MathUtils.fibonacci(n)


# Conditional parametrized tests
@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
])
def test_is_prime_small_primes(n, expected):
    """Test small prime numbers."""
    assert MathUtils.is_prime(n) == expected


@pytest.mark.parametrize("n,expected", [
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
])
def test_is_prime_small_composites(n, expected):
    """Test small composite numbers."""
    assert MathUtils.is_prime(n) == expected


# Parametrized fixture example
@pytest.fixture(params=["hello", "world", "python"])
def sample_string(request):
    """Fixture that provides different strings."""
    return request.param


def test_string_length(sample_string):
    """Test string length using parametrized fixture."""
    assert len(sample_string) > 0


def test_string_has_vowels(sample_string):
    """Test that strings contain vowels."""
    vowels = 'aeiouAEIOU'
    assert any(char in vowels for char in sample_string)


# Multiple parametrized fixtures
@pytest.fixture(params=[1, 2, 3])
def num1(request):
    return request.param


@pytest.fixture(params=[4, 5, 6])
def num2(request):
    return request.param


def test_add_parametrized_fixtures(num1, num2):
    """Test addition with multiple parametrized fixtures."""
    assert num1 + num2 > 4


# Skipping parametrized tests conditionally
@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 2),
    pytest.param(100, "skipped", marks=pytest.mark.skip(reason="Too large for demo")),
    (3, 6),
])
def test_factorial_with_skip(n, expected):
    """Test factorial with some tests skipped."""
    if expected == "skipped":
        pytest.skip("Skipping large factorial")
    assert MathUtils.factorial(n) == expected


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
