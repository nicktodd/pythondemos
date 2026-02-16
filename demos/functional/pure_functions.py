# pure_functions.py
# Demonstrating pure vs impure functions in Python

# Pure functions:
# - Always return the same result for the same inputs
# - Have no side effects (don't modify external state)
# - Don't depend on external state

# Impure functions:
# - May return different results for same inputs
# - Have side effects
# - Depend on external state

# Global variable (external state)
balance = 1000

# IMPURE FUNCTIONS
print("=== IMPURE FUNCTIONS ===")

def impure_add(x, y):
    """Impure: depends on and modifies external state."""
    global balance
    balance += x + y
    return balance

print("Impure function - depends on global state:")
result1 = impure_add(10, 20)
print(f"Result 1: {result1}, Balance: {balance}")

result2 = impure_add(10, 20)  # Same inputs, different result
print(f"Result 2: {result2}, Balance: {balance}")

def impure_print_and_return(x):
    """Impure: has side effect of printing."""
    print(f"Processing: {x}")
    return x * 2

print("\nImpure function - has side effects:")
result = impure_print_and_return(5)  # Prints and returns

# PURE FUNCTIONS
print("\n=== PURE FUNCTIONS ===")

def pure_add(x, y):
    """Pure: only depends on inputs, no side effects."""
    return x + y

def pure_multiply(x, y):
    """Pure: deterministic and no side effects."""
    return x * y

def pure_square(x):
    """Pure: always same result for same input."""
    return x ** 2

print("Pure functions - same inputs always give same results:")
print(f"pure_add(3, 4): {pure_add(3, 4)}")
print(f"pure_add(3, 4): {pure_add(3, 4)}")  # Same result
print(f"pure_multiply(5, 6): {pure_multiply(5, 6)}")
print(f"pure_square(7): {pure_square(7)}")

# Pure function with collections
def pure_filter_even(numbers):
    """Pure: returns new list, doesn't modify input."""
    return [n for n in numbers if n % 2 == 0]

def pure_double_list(numbers):
    """Pure: returns new list, doesn't modify input."""
    return [n * 2 for n in numbers]

original_list = [1, 2, 3, 4, 5]
print(f"\nOriginal list: {original_list}")

even_numbers = pure_filter_even(original_list)
doubled_numbers = pure_double_list(original_list)

print(f"Even numbers: {even_numbers}")
print(f"Doubled numbers: {doubled_numbers}")
print(f"Original list unchanged: {original_list}")

# IMPURE vs PURE: List operations
print("\n=== LIST OPERATIONS: IMPURE vs PURE ===")

def impure_append(lst, item):
    """Impure: modifies the input list."""
    lst.append(item)
    return lst

def pure_append(lst, item):
    """Pure: returns new list, doesn't modify input."""
    return lst + [item]

my_list = [1, 2, 3]
print(f"Original list: {my_list}")

# Impure operation
impure_result = impure_append(my_list, 4)
print(f"After impure append: {my_list}")  # Original modified!
print(f"Impure result: {impure_result}")

# Reset list
my_list = [1, 2, 3]

# Pure operation
pure_result = pure_append(my_list, 4)
print(f"After pure append: {my_list}")    # Original unchanged
print(f"Pure result: {pure_result}")

# Higher-order pure functions
def pure_map(func, lst):
    """Pure map function."""
    return [func(x) for x in lst]

def pure_filter(func, lst):
    """Pure filter function."""
    return [x for x in lst if func(x)]

def pure_reduce(func, lst, initial=0):
    """Pure reduce function."""
    result = initial
    for item in lst:
        result = func(result, item)
    return result

print("\n=== HIGHER-ORDER PURE FUNCTIONS ===")
numbers = [1, 2, 3, 4, 5]

# Pure map
squared = pure_map(lambda x: x**2, numbers)
print(f"Squared: {squared}")

# Pure filter
evens = pure_filter(lambda x: x % 2 == 0, numbers)
print(f"Evens: {evens}")

# Pure reduce
total = pure_reduce(lambda x, y: x + y, numbers)
print(f"Sum: {total}")

# Benefits of pure functions
print("\n=== BENEFITS OF PURE FUNCTIONS ===")

# 1. Testability
def test_pure_functions():
    """Easy to test pure functions."""
    assert pure_add(2, 3) == 5
    assert pure_square(4) == 16
    assert pure_filter_even([1, 2, 3, 4]) == [2, 4]
    print("All pure function tests passed!")

test_pure_functions()

# 2. Parallelization (conceptual)
def process_data_pure(data):
    """Pure function that can be easily parallelized."""
    return [pure_square(x) for x in data]

# 3. Memoization example
def memoize(func):
    """Decorator to memoize pure functions."""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def expensive_pure_calculation(n):
    """Simulate expensive calculation."""
    print(f"Calculating for {n}...")
    return n ** n

print("\nMemoization with pure functions:")
print(expensive_pure_calculation(3))  # Calculates
print(expensive_pure_calculation(3))  # Uses cache
print(expensive_pure_calculation(4))  # Calculates
