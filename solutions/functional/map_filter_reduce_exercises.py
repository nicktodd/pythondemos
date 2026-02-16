# Exercise 3: Map, Filter, Reduce

from functools import reduce

# Use map to convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

# Use filter to get all words longer than 4 characters
words = ["hello", "world", "python", "is", "awesome"]
long_words = list(filter(lambda w: len(w) > 4, words))

# Use reduce to calculate the product of a list of numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

# Combine all three to process a list of numbers
combined = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# Test code
print("Fahrenheit:", fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
print("Long words:", long_words)  # ['hello', 'world', 'python', 'awesome']
print("Product:", product)  # 120
print("Combined (sum of squares of evens):", combined)  # 20 (4 + 16)
