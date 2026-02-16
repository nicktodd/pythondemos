# map_filter_reduce.py
# Demonstrating map, filter, and reduce functions in Python

# Sample data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["hello", "world", "python", "programming"]
prices = [10.99, 25.50, 8.75, 15.00, 42.30]

print("Original data:")
print(f"Numbers: {numbers}")
print(f"Words: {words}")
print(f"Prices: {prices}")

# MAP: Apply a function to each element
print("\n=== MAP ===")
# Using map with a named function
def square(x):
    return x ** 2

squared_numbers = list(map(square, numbers))
print(f"Squared numbers: {squared_numbers}")

# Using map with lambda
uppercase_words = list(map(lambda w: w.upper(), words))
print(f"Uppercase words: {uppercase_words}")

# Map with multiple iterables
combined = list(map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30]))
print(f"Combined lists: {combined}")

# FILTER: Select elements based on a condition
print("\n=== FILTER ===")
# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Filter long words
long_words = list(filter(lambda w: len(w) > 5, words))
print(f"Long words (>5 chars): {long_words}")

# Filter expensive items
expensive_items = list(filter(lambda p: p > 20, prices))
print(f"Expensive items (>$20): {expensive_items}")

# REDUCE: Combine elements into a single value
print("\n=== REDUCE ===")
from functools import reduce

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers: {total}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum number: {maximum}")

# Concatenate strings
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"Concatenated words: {sentence}")

# Calculate total price
total_price = reduce(lambda x, y: x + y, prices)
print(f"Total price: ${total_price:.2f}")

# More complex reduce example: factorial
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(f"Factorial of 5: {factorial(5)}")

# Combining map, filter, reduce
print("\n=== COMBINING MAP, FILTER, REDUCE ===")
# Calculate sum of squares of even numbers
result = reduce(lambda x, y: x + y,
                map(lambda x: x ** 2,
                    filter(lambda x: x % 2 == 0, numbers)))
print(f"Sum of squares of even numbers: {result}")

# Alternative using list comprehensions (covered in next demo)
result2 = sum([x**2 for x in numbers if x % 2 == 0])
print(f"Same result with comprehension: {result2}")
