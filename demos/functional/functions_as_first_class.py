# functions_as_first_class.py
# Demonstrating functions as first-class citizens in Python

def greet(name):
    """A simple greeting function."""
    return f"Hello, {name}!"

def farewell(name):
    """A farewell function."""
    return f"Goodbye, {name}!"

def apply_greeting(greeting_func, name):
    """
    Higher-order function that takes a greeting function and applies it.
    This demonstrates functions as parameters.
    """
    return greeting_func(name)

def create_multiplier(factor):
    """
    Function that returns another function.
    This demonstrates functions as return values.
    """
    def multiplier(x):
        return x * factor
    return multiplier

# Functions can be assigned to variables
hello_func = greet
goodbye_func = farewell

print("Functions as variables:")
print(hello_func("Alice"))  # Hello, Alice!
print(goodbye_func("Bob"))  # Goodbye, Bob!

print("\nFunctions as parameters:")
print(apply_greeting(greet, "Charlie"))  # Hello, Charlie!
print(apply_greeting(farewell, "Diana"))  # Goodbye, Diana!

print("\nFunctions as return values:")
double = create_multiplier(2)
triple = create_multiplier(3)
print(f"Double 5: {double(5)}")  # 10
print(f"Triple 5: {triple(5)}")  # 15

# Functions can be stored in data structures
greeting_functions = [greet, farewell]
for func in greeting_functions:
    print(func("Eve"))

# Functions have attributes
print(f"\nFunction name: {greet.__name__}")
print(f"Function docstring: {greet.__doc__}")
