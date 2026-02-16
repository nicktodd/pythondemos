# Exercise 7: Pure Functions

# Create pure functions for mathematical operations
def pure_add(x, y):
    return x + y

def pure_multiply(x, y):
    return x * y

# Create impure functions that modify external state
total = 0

def impure_add(x):
    global total
    total += x
    return total

state = []

def impure_append(item):
    state.append(item)
    return state

# Implement pure versions of list operations
def pure_filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def pure_map_square(numbers):
    return [n**2 for n in numbers]

# Create a memoization decorator for pure functions
# Role: Caches function results to avoid recomputing expensive operations for the same inputs
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Test code
print("Pure add:", pure_add(3, 4))  # 7
print("Pure filter even:", pure_filter_even([1, 2, 3, 4, 5]))  # [2, 4]

impure_add(5)
print("Impure total:", total)  # 5

print("Fib 10:", fib(10))  # 55
