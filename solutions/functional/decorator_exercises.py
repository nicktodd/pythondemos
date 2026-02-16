# Exercise 8: Decorators

import time
from functools import wraps

# Create a timing decorator
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

# Create a logging decorator
def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Create a decorator that caches function results
def cache_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# Create a decorator that validates function arguments
def validate_positive(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg < 0:
                raise ValueError("All arguments must be positive numbers")
        return func(*args)
    return wrapper

# Stack multiple decorators
@timing_decorator
@logging_decorator
@cache_decorator
@validate_positive
def complex_function(x, y):
    time.sleep(0.1)  # Simulate work
    return x + y

# Test code
@timing_decorator
def example_function(x, y):
    return x + y

print("Timing decorator:")
result = example_function(2, 3)
print("Result:", result)

@logging_decorator
def another_function(x):
    return x * 2

print("\nLogging decorator:")
result2 = another_function(5)
print("Result:", result2)

print("\nStacked decorators:")
result3 = complex_function(2, 3)
print("Result:", result3)

# Second call should use cache
print("\nCached call:")
result4 = complex_function(2, 3)
print("Result:", result4)
