# generators.py
# Demonstrating generators and generator functions in Python

# Generators are functions that return an iterator
# They use 'yield' instead of 'return'
# They are memory efficient for large datasets

def countdown(n):
    """Generator function that counts down from n."""
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Countdown finished!")

print("=== BASIC GENERATOR FUNCTION ===")
# Create generator object
counter = countdown(5)
print(f"Generator object: {counter}")

# Get values one by one
print("Countdown:")
for num in counter:
    print(num)

# Generator expressions (similar to list comprehensions but lazy)
print("\n=== GENERATOR EXPRESSIONS ===")
squares_gen = (x**2 for x in range(10))
print(f"Generator expression: {squares_gen}")

print("Squares from generator:")
for square in squares_gen:
    print(square, end=" ")
print()

# Memory comparison
print("\n=== MEMORY EFFICIENCY ===")
import sys

# List comprehension (creates entire list in memory)
large_list = [x**2 for x in range(10000)]
print(f"List memory usage: {sys.getsizeof(large_list)} bytes")

# Generator expression (creates values on demand)
large_gen = (x**2 for x in range(10000))
print(f"Generator memory usage: {sys.getsizeof(large_gen)} bytes")

# Fibonacci generator
def fibonacci(limit):
    """Generate Fibonacci sequence up to limit."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print("\n=== FIBONACCI GENERATOR ===")
fib_gen = fibonacci(10)
print("First 10 Fibonacci numbers:")
for num in fib_gen:
    print(num, end=" ")
print()

# Prime number generator
def primes():
    """Infinite generator of prime numbers."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print("\n=== PRIME NUMBER GENERATOR ===")
prime_gen = primes()
print("First 10 prime numbers:")
for _ in range(10):
    print(next(prime_gen), end=" ")
print()

# Generator with send() method (coroutine)
def accumulator():
    """Generator that accumulates values sent to it."""
    total = 0
    while True:
        value = (yield total)
        if value is not None:
            total += value

print("\n=== GENERATOR AS COROUTINE ===")
acc = accumulator()
next(acc)  # Prime the generator
print(f"Initial total: {acc.send(None)}")

print("Adding values:")
print(f"After adding 10: {acc.send(10)}")
print(f"After adding 5: {acc.send(5)}")
print(f"After adding 20: {acc.send(20)}")

# File reading generator (memory efficient)
def read_large_file(file_path, chunk_size=1024):
    """Generator to read large file in chunks."""
    try:
        with open(file_path, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    except FileNotFoundError:
        yield "File not found"

print("\n=== FILE READING GENERATOR ===")
# Create a sample file for demonstration
with open('sample.txt', 'w') as f:
    f.write("This is a sample file.\n" * 100)

file_gen = read_large_file('sample.txt')
print("Reading file in chunks:")
chunk_count = 0
for chunk in file_gen:
    chunk_count += 1
    print(f"Chunk {chunk_count}: {len(chunk)} characters")
    if chunk_count >= 3:  # Show only first 3 chunks
        break

# Pipeline of generators
def integers():
    """Generate integers starting from 1."""
    n = 1
    while True:
        yield n
        n += 1

def squares(gen):
    """Square the numbers from a generator."""
    for n in gen:
        yield n ** 2

def evens(gen):
    """Filter for even numbers."""
    for n in gen:
        if n % 2 == 0:
            yield n

print("\n=== GENERATOR PIPELINE ===")
# Create pipeline: integers -> squares -> evens
pipeline = evens(squares(integers()))

print("First 5 even squares:")
for _ in range(5):
    print(next(pipeline), end=" ")
print()

# Clean up
import os
os.remove('sample.txt')
