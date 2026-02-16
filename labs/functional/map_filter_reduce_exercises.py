# Exercise 3: Map, Filter, Reduce

from functools import reduce

# TODO: Use map to convert temperatures from Celsius to Fahrenheit

# TODO: Use filter to get all words longer than 4 characters

# TODO: Use reduce to calculate the product of a list of numbers

# TODO: Combine all three to process a list of numbers

# Test code (uncomment to test)
# celsius = [0, 10, 20, 30, 40]
# fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
# print(fahrenheit)  # Should print [32.0, 50.0, 68.0, 86.0, 104.0]

# words = ["hello", "world", "python", "is", "awesome"]
# long_words = list(filter(lambda w: len(w) > 4, words))
# print(long_words)  # Should print ['hello', 'world', 'python', 'awesome']

# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Should print 120
