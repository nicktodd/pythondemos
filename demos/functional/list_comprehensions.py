# list_comprehensions.py
# Demonstrating list comprehensions in Python

# List comprehensions provide a concise way to create lists
# Syntax: [expression for item in iterable if condition]

# Sample data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["hello", "world", "python", "programming", "code"]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original data:")
print(f"Numbers: {numbers}")
print(f"Words: {words}")
print(f"Matrix: {matrix}")

# Basic list comprehension
print("\n=== BASIC LIST COMPREHENSIONS ===")
squares = [x ** 2 for x in numbers]
print(f"Squares: {squares}")

# With condition (filtering)
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# String operations
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")

# Length of words
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")

# Nested list comprehension (flatten matrix)
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# DICTIONARY COMPREHENSIONS
print("\n=== DICTIONARY COMPREHENSIONS ===")
# Create dict of word: length
word_dict = {word: len(word) for word in words}
print(f"Word lengths dict: {word_dict}")

# Create dict of number: square for even numbers
even_squares_dict = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares dict: {even_squares_dict}")

# SET COMPREHENSIONS
print("\n=== SET COMPREHENSIONS ===")
# Create set of unique word lengths
lengths_set = {len(word) for word in words}
print(f"Unique word lengths: {lengths_set}")

# Create set of squares
squares_set = {x**2 for x in numbers}
print(f"Squares set: {squares_set}")

# GENERATOR EXPRESSIONS (similar to list comprehensions but lazy)
print("\n=== GENERATOR EXPRESSIONS ===")
# Use () instead of []
squares_gen = (x**2 for x in numbers)
print(f"Generator object: {squares_gen}")
print(f"First 3 squares: {list(squares_gen)[:3]}")

# Memory efficient for large data
large_squares = (x**2 for x in range(1000000))
print(f"Large generator created (memory efficient)")

# NESTED COMPREHENSIONS
print("\n=== NESTED COMPREHENSIONS ===")
# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Transposed matrix: {transposed}")

# Cartesian product
colors = ['red', 'blue', 'green']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
print(f"Color-size combinations: {combinations[:6]}...")  # Show first 6

# CONDITIONAL EXPRESSIONS IN COMPREHENSIONS
print("\n=== CONDITIONAL EXPRESSIONS ===")
# Categorize numbers
categories = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(f"Number categories: {categories}")

# FizzBuzz with comprehension
fizzbuzz = ['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else str(x) for x in range(1, 16)]
print(f"FizzBuzz: {fizzbuzz}")

# PRACTICAL EXAMPLES
print("\n=== PRACTICAL EXAMPLES ===")
# Read and process file (simulated)
data_lines = ["Name: Alice, Age: 25", "Name: Bob, Age: 30", "Name: Charlie, Age: 35"]

# Extract names
names = [line.split(',')[0].split(':')[1].strip() for line in data_lines]
print(f"Extracted names: {names}")

# Extract ages as integers
ages = [int(line.split(',')[1].split(':')[1].strip()) for line in data_lines]
print(f"Extracted ages: {ages}")

# Create person dicts
persons = [{'name': line.split(',')[0].split(':')[1].strip(),
            'age': int(line.split(',')[1].split(':')[1].strip())} for line in data_lines]
print(f"Person dicts: {persons}")

# Filter adults
adults = [person for person in persons if person['age'] >= 18]
print(f"Adults: {adults}")
