# decorators.py
# Demonstrating decorators in Python

# Decorators are functions that modify the behavior of other functions
# They allow you to wrap another function to extend its behavior without modifying it

# Basic decorator
def simple_decorator(func):
    """A simple decorator that prints before and after function execution."""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@simple_decorator
def greet(name):
    """Function decorated with simple_decorator."""
    print(f"Hello, {name}!")
    return f"Greeted {name}"

print("=== BASIC DECORATOR ===")
result = greet("Alice")
print(f"Result: {result}")

# Decorator with parameters
def repeat(times):
    """Decorator factory that creates a repeater decorator."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

print("\n=== DECORATOR WITH PARAMETERS ===")
say_hello("Bob")

# Timing decorator
import time

def timing_decorator(func):
    """Decorator that measures function execution time."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """A function that takes some time."""
    time.sleep(0.5)
    return "Done"

print("\n=== TIMING DECORATOR ===")
result = slow_function()
print(f"Result: {result}")

# Logging decorator
def logging_decorator(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logging_decorator
def add_numbers(a, b):
    return a + b

@logging_decorator
def multiply_numbers(a, b, c=1):
    return a * b * c

print("\n=== LOGGING DECORATOR ===")
print(add_numbers(3, 4))
print(multiply_numbers(2, 3, c=5))

# Class-based decorator
class CountCalls:
    """Class-based decorator that counts function calls."""

    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Call {self.call_count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n=== CLASS-BASED DECORATOR ===")
print(f"Fibonacci(5): {fibonacci(10)}")  # Note: recursive calls also counted

# Decorator that modifies return value
def uppercase_decorator(func):
    """Decorator that converts string return value to uppercase."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_decorator
def get_message(name):
    return f"Hello, {name}! How are you?"

print("\n=== DECORATOR MODIFYING RETURN VALUE ===")
message = get_message("Charlie")
print(f"Message: {message}")

# Stacking decorators
def bold_decorator(func):
    """Add bold tags."""
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic_decorator(func):
    """Add italic tags."""
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold_decorator
@italic_decorator
def format_text(text):
    return text

print("\n=== STACKING DECORATORS ===")
formatted = format_text("Hello World")
print(f"Formatted: {formatted}")

# Decorator with functools.wraps (preserves function metadata)
import functools

def proper_decorator(func):
    """Proper decorator that preserves function metadata."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function."""
        print(f"Calling {func.__name__} with docstring: {func.__doc__}")
        return func(*args, **kwargs)
    return wrapper

@proper_decorator
def documented_function():
    """This is a well-documented function."""
    return "Documented result"

print("\n=== DECORATOR WITH functools.wraps ===")
result = documented_function()
print(f"Function name: {documented_function.__name__}")
print(f"Function doc: {documented_function.__doc__}")
print(f"Result: {result}")

# Method decorator
def method_decorator(func):
    """Decorator for class methods."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Calling method {func.__name__} on {self.__class__.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    """A simple calculator class."""

    def __init__(self):
        self.value = 0

    @method_decorator
    def add(self, x):
        self.value += x
        return self.value

    @method_decorator
    def multiply(self, x):
        self.value *= x
        return self.value

print("\n=== METHOD DECORATOR ===")
calc = Calculator()
print(calc.add(10))
print(calc.multiply(3))
