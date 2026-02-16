# Exercise 2: Lambda Functions

# Create lambda functions for basic arithmetic operations
add = lambda x, y: x + y
multiply = lambda x, y: x * y
subtract = lambda x, y: x - y
divide = lambda x, y: x / y if y != 0 else None

# Use lambda in sorting (sort a list of tuples by second element)
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

# Create lambda functions with conditional expressions
check_number = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

# Use lambda with map, filter, and reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
sum_all = reduce(lambda x, y: x + y, numbers)

# Test code
print("Add:", add(2, 3))  # 5
print("Multiply:", multiply(4, 5))  # 20
print("Sorted pairs:", sorted_pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]
print("Check number 5:", check_number(5))  # positive
print("Check number -3:", check_number(-3))  # negative
print("Check number 0:", check_number(0))  # zero
print("Squares:", squares)  # [1, 4, 9, 16, 25]
print("Evens:", evens)  # [2, 4]
print("Sum:", sum_all)  # 15
