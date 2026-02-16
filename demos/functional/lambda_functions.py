# lambda_functions.py
# Demonstrating lambda functions (anonymous functions) in Python

# Lambda functions are small, anonymous functions defined with the lambda keyword
# Syntax: lambda arguments: expression

# Basic lambda examples
square = lambda x: x ** 2
cube = lambda x: x ** 3

print("Basic lambda functions:")
print(f"Square of 5: {square(5)}")  # 25
print(f"Cube of 3: {cube(3)}")     # 27

# Lambda with multiple arguments
add = lambda x, y: x + y
multiply = lambda x, y, z: x * y * z

print(f"\nAdd 3 + 4: {add(3, 4)}")           # 7
print(f"Multiply 2 * 3 * 4: {multiply(2, 3, 4)}")  # 24

# Lambda with conditional expressions
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
maximum = lambda x, y: x if x > y else y

print(f"\n5 is: {is_even(5)}")    # Odd
print(f"8 is: {is_even(8)}")    # Even
print(f"Max of 10, 20: {maximum(10, 20)}")  # 20

# Lambda in sorting
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade using lambda as key
sorted_students = sorted(students, key=lambda student: student["grade"])
print(f"\nStudents sorted by grade:")
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")

# Lambda in filtering (though filter() is better, this shows the concept)
high_achievers = list(filter(lambda s: s["grade"] >= 80, students))
print(f"\nHigh achievers (>=80): {[s['name'] for s in high_achievers]}")

# Lambda with default arguments
power = lambda x, n=2: x ** n
print(f"\nPower functions:")
print(f"5^2: {power(5)}")      # 25
print(f"5^3: {power(5, 3)}")   # 125

# Lambda returning lambda (currying)
def make_power_function(n):
    return lambda x: x ** n

square_func = make_power_function(2)
cube_func = make_power_function(3)

print(f"\nUsing curried functions:")
print(f"5 squared: {square_func(5)}")  # 25
print(f"5 cubed: {cube_func(5)}")     # 125
