# Exercise 4: List Comprehensions

# Create a list of squares for even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Create a dictionary of word lengths
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}

# Create a set of unique characters from a string
text = "hello world"
unique_chars = {char for char in text if char != ' '}

# Flatten a nested list using comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]

# Create conditional comprehensions
positive_squares = [x**2 for x in range(-5, 6) if x > 0]
even_or_odd = ["even" if x % 2 == 0 else "odd" for x in range(5)]

# Test code
print("Even squares:", even_squares)  # [4, 16, 36]
print("Word lengths:", word_lengths)  # {'hello': 5, 'world': 5, 'python': 6}
print("Unique chars:", unique_chars)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
print("Flattened:", flattened)  # [1, 2, 3, 4, 5, 6]
print("Positive squares:", positive_squares)  # [1, 4, 9, 16, 25]
print("Even or odd:", even_or_odd)  # ['even', 'odd', 'even', 'odd', 'even']
