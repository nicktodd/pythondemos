# Exercise 5: Generators

# Create a generator that yields Fibonacci numbers
def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Loop n times to generate the sequence
    for _ in range(n):
        # Yield the current value of a (the next Fibonacci number)
        yield a
        # Update a and b to the next pair in the sequence
        a, b = b, a + b

# Benefit: This generator produces Fibonacci numbers one at a time without storing the entire sequence in memory

# Create a generator that reads a file line by line
def read_file_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Create a generator expression for squares
squares = (x**2 for x in range(10))

# Implement a generator pipeline
def even_squares(numbers):
    return (x**2 for x in numbers if x % 2 == 0)

# Test code
fib_gen = fibonacci(10)
print("Fibonacci:", list(fib_gen))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print("Squares:", list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sq = even_squares(numbers)
print("Even squares:", list(even_sq))  # [4, 16, 36, 64, 100]

# For file reading, assuming a test file exists
# lines = list(read_file_lines('test.txt'))
# print("File lines:", lines)
