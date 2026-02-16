# Python Functional Programming Lab

This lab will guide you through implementing key functional programming concepts in Python. You'll build upon the concepts demonstrated in the `demos/functional/` folder.

## Prerequisites

Before starting, review the demo files in `demos/functional/` to understand the concepts:

- `functions_as_first_class.py` - Functions as first-class citizens
- `lambda_functions.py` - Lambda expressions
- `map_filter_reduce.py` - Higher-order functions
- `list_comprehensions.py` - Comprehension syntax
- `generators.py` - Generator functions and expressions
- `recursion.py` - Recursive functions
- `pure_functions.py` - Pure vs impure functions
- `decorators.py` - Function decorators

## Lab Structure

- **Starter files**: Located in `labs/functional/`
- **Solutions**: Located in `solutions/functional/` (check after completing exercises)
- **Your work**: Modify the starter files in `labs/functional/`

## Exercise 1: Functions as First-Class Citizens

**File**: `labs/functional/first_class_functions.py`

Implement functions that demonstrate functions as first-class citizens:

1. Create a function `apply_operation(func, x, y)` that takes a function and two numbers, applies the function to them
2. Create a function `create_multiplier(factor)` that returns a function that multiplies by the factor
3. Create a list of functions and apply them to a value
4. Store functions in a dictionary and call them by key

**Test your implementation**:
```python
# Test apply_operation
result = apply_operation(lambda x, y: x + y, 3, 4)  # Should return 7

# Test create_multiplier
double = create_multiplier(2)
print(double(5))  # Should print 10

# Test function collections
funcs = [lambda x: x**2, lambda x: x*2, lambda x: x+10]
results = [f(3) for f in funcs]  # Should be [9, 6, 13]
```

## Exercise 2: Lambda Functions

**File**: `labs/functional/lambda_exercises.py`

Implement various lambda functions for different scenarios:

1. Create lambda functions for basic arithmetic operations
2. Use lambda in sorting (sort a list of tuples by second element)
3. Create lambda functions with conditional expressions
4. Use lambda with map, filter, and reduce

**Test your implementation**:
```python
# Arithmetic lambdas
add = lambda x, y: x + y
multiply = lambda x, y: x * y

# Sorting with lambda
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

# Conditional lambda
check_number = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
```

## Exercise 3: Map, Filter, Reduce

**File**: `labs/functional/map_filter_reduce_exercises.py`

Implement solutions using map, filter, and reduce:

1. Use map to convert temperatures from Celsius to Fahrenheit
2. Use filter to get all words longer than 4 characters
3. Use reduce to calculate the product of a list of numbers
4. Combine all three to process a list of numbers

**Test your implementation**:
```python
from functools import reduce

# Temperature conversion
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

# Filter long words
words = ["hello", "world", "python", "is", "awesome"]
long_words = list(filter(lambda w: len(w) > 4, words))

# Product with reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
```

## Exercise 4: List Comprehensions

**File**: `labs/functional/comprehensions_exercises.py`

Implement various list, dict, and set comprehensions:

1. Create a list of squares for even numbers
2. Create a dictionary of word lengths
3. Create a set of unique characters from a string
4. Flatten a nested list using comprehension
5. Create conditional comprehensions

**Test your implementation**:
```python
# List comprehension
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Dict comprehension
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}

# Set comprehension
text = "hello world"
unique_chars = {char for char in text if char != ' '}

# Nested comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
```

## Exercise 5: Generators

**File**: `labs/functional/generator_exercises.py`

Implement generator functions and expressions:

1. Create a generator that yields Fibonacci numbers
2. Create a generator that reads a file line by line
3. Create a generator expression for squares
4. Implement a generator pipeline

**Test your implementation**:
```python
# Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generator expression
squares = (x**2 for x in range(10))

# Pipeline
def even_squares(numbers):
    return (x**2 for x in numbers if x % 2 == 0)
```

## Exercise 6: Recursion

**File**: `labs/functional/recursion_exercises.py`

Implement recursive solutions for common problems:

1. Calculate factorial recursively
2. Reverse a string recursively
3. Sum a list recursively
4. Implement binary search recursively
5. Flatten a nested list recursively

**Test your implementation**:
```python
# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Reverse string
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# Sum list
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
```

## Exercise 7: Pure Functions

**File**: `labs/functional/pure_functions_exercises.py`

Implement pure and impure functions, demonstrating the difference:

1. Create pure functions for mathematical operations
2. Create impure functions that modify external state
3. Implement pure versions of list operations
4. Create a memoization decorator for pure functions

**Test your implementation**:
```python
# Pure functions
def pure_add(x, y):
    return x + y

def pure_filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

# Impure function
total = 0
def impure_add(x):
    global total
    total += x
    return total

# Memoization
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

## Exercise 8: Decorators

**File**: `labs/functional/decorator_exercises.py`

Implement various decorators:

1. Create a timing decorator
2. Create a logging decorator
3. Create a decorator that caches function results
4. Create a decorator that validates function arguments
5. Stack multiple decorators

**Test your implementation**:
```python
# Timing decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

# Logging decorator
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@timing_decorator
@logging_decorator
def example_function(x, y):
    return x + y
```

## Submission

1. Complete all exercises in the `labs/functional/` files
2. Test your implementations with the provided test cases
3. Compare your solutions with the completed versions in `solutions/functional/`
4. Run the demo files to see advanced examples

## Tips

- Start with Exercise 1 and build upon previous exercises
- Use the demo files as references, but implement your own versions
- Test frequently as you implement each function
- Remember that functional programming emphasizes immutability and pure functions
- Use `functools` module for advanced functional operations
