# recursion.py
# Demonstrating recursive functions in Python

# Recursion is when a function calls itself
# Every recursive function needs a base case and a recursive case

def factorial(n):
    """
    Calculate factorial using recursion.
    Base case: n == 0 or n == 1
    Recursive case: n * factorial(n-1)
    """
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)

print("=== FACTORIAL ===")
print(f"Factorial of 5: {factorial(5)}")  # 120
print(f"Factorial of 0: {factorial(0)}")  # 1

# Fibonacci sequence
def fibonacci(n):
    """
    Calculate nth Fibonacci number recursively.
    Base cases: n == 0 or n == 1
    Recursive case: fibonacci(n-1) + fibonacci(n-2)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("\n=== FIBONACCI SEQUENCE ===")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}", end=" ")
print()

# Sum of list elements
def sum_list(lst):
    """Sum all elements in a list recursively."""
    if not lst:  # Base case: empty list
        return 0
    else:  # Recursive case
        return lst[0] + sum_list(lst[1:])

print("\n=== SUM LIST ===")
numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers}: {sum_list(numbers)}")

# Reverse a string
def reverse_string(s):
    """Reverse a string recursively."""
    if len(s) <= 1:  # Base case
        return s
    else:  # Recursive case
        return reverse_string(s[1:]) + s[0]

print("\n=== REVERSE STRING ===")
text = "Hello, World!"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")

# Binary search (recursive)
def binary_search(arr, target, low=0, high=None):
    """
    Binary search using recursion.
    Returns index of target if found, -1 otherwise.
    """
    if high is None:
        high = len(arr) - 1

    if low > high:  # Base case: not found
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:  # Base case: found
        return mid
    elif arr[mid] > target:  # Search left half
        return binary_search(arr, target, low, mid - 1)
    else:  # Search right half
        return binary_search(arr, target, mid + 1, high)

print("\n=== BINARY SEARCH ===")
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
index = binary_search(sorted_list, target)
print(f"Target {target} found at index {index} in {sorted_list}")

target = 4
index = binary_search(sorted_list, target)
print(f"Target {target} found at index {index} in {sorted_list}")

# Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve Tower of Hanoi puzzle recursively.
    n: number of disks
    source, target, auxiliary: rod names
    """
    if n == 1:  # Base case
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, auxiliary, target)

    # Move nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n-1, auxiliary, target, source)

print("\n=== TOWER OF HANOI ===")
print("Solution for 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')

# Flatten nested list
def flatten_list(nested_list):
    """Flatten a nested list recursively."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # Recursive call
        else:
            result.append(item)
    return result

print("\n=== FLATTEN NESTED LIST ===")
nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(f"Nested: {nested}")
print(f"Flattened: {flatten_list(nested)}")

# Tail recursion optimization (Python doesn't optimize tail recursion)
def factorial_tail(n, accumulator=1):
    """Tail recursive factorial."""
    if n == 0 or n == 1:
        return accumulator
    else:
        return factorial_tail(n - 1, n * accumulator)

print("\n=== TAIL RECURSION ===")
print(f"Tail recursive factorial of 5: {factorial_tail(5)}")

# Warning about recursion depth
import sys
print(f"\nRecursion limit: {sys.getrecursionlimit()}")
# factorial(1000)  # This would cause RecursionError
