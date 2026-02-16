# Python Data Typing Lab

This lab will guide you through implementing comprehensive type hints in Python. You'll build upon the concepts demonstrated in the `demos/data_typing/` folder and learn how to "strongly" type your Python code.

## Prerequisites

Before starting, review the demo files in `demos/data_typing/` to understand the concepts:

- `basic_type_hints.py` - Basic type hints for variables and functions
- `collections_typing.py` - Type hints with collections (List, Dict, Tuple, Set)
- `optional_union.py` - Optional and Union types
- `custom_types.py` - Custom types, type aliases, and advanced structures
- `advanced_typing.py` - Generics, protocols, and type variables
- `type_checking.py` - Runtime type checking and validation
- `best_practices.py` - Best practices for effective type hinting

## Lab Structure

- **Starter files**: Located in `labs/data_typing/`
- **Solutions**: Located in `solutions/data_typing/` (check after completing exercises)
- **Your work**: Modify the starter files in `labs/data_typing/`

## Exercise 1: Basic Type Hints

**File**: `labs/data_typing/basic_type_hints.py`

Implement basic type hints for variables and functions:

1. Create variables with proper type hints for different data types
2. Create a function `calculate_bmi(weight_kg: float, height_m: float) -> float` that calculates BMI
3. Create a function `format_person_info(name: str, age: int, city: str) -> str` that formats person information
4. Create a function `is_adult(age: int) -> bool` that checks if someone is an adult
5. Test all functions with various inputs

**Test your implementation**:
```python
# Test calculate_bmi
bmi = calculate_bmi(70.0, 1.75)  # Should return ~22.86
print(f"BMI: {bmi:.2f}")

# Test format_person_info
info = format_person_info("Alice", 30, "New York")
print(info)  # Should format nicely

# Test is_adult
print(is_adult(25))  # Should return True
print(is_adult(15))  # Should return False
```

## Exercise 2: Collections Type Hints

**File**: `labs/data_typing/collections_typing.py`

Implement functions using collection type hints:

1. Create a function `analyze_numbers(numbers: List[int]) -> Dict[str, float]` that returns min, max, and average
2. Create a function `count_word_frequency(text: str) -> Dict[str, int]` that counts word occurrences
3. Create a function `merge_dictionaries(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]` that merges two dictionaries
4. Create a function `get_unique_items(items: List[str]) -> Set[str]` that returns unique items
5. Test all functions with various inputs

**Test your implementation**:
```python
# Test analyze_numbers
stats = analyze_numbers([1, 2, 3, 4, 5])
print(stats)  # Should contain min, max, average

# Test count_word_frequency
freq = count_word_frequency("hello world hello")
print(freq)  # Should show word counts

# Test merge_dictionaries
merged = merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
print(merged)  # Should merge with sum for duplicate keys
```

## Exercise 3: Optional and Union Types

**File**: `labs/data_typing/optional_union.py`

Implement functions using Optional and Union types:

1. Create a function `safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]` for safe division
2. Create a function `parse_number(value: str) -> Optional[Union[int, float]]` that parses strings to numbers
3. Create a function `find_in_list(items: List[str], target: str) -> Optional[int]` that finds index of target
4. Create a function `validate_email(email: Union[str, None]) -> bool` that validates email format
5. Test all functions with various inputs including None and invalid values

**Test your implementation**:
```python
# Test safe_divide
result = safe_divide(10, 2)  # Should return 5.0
result = safe_divide(10, 0)  # Should return None

# Test parse_number
result = parse_number("42")  # Should return 42
result = parse_number("3.14")  # Should return 3.14
result = parse_number("hello")  # Should return None

# Test find_in_list
index = find_in_list(["a", "b", "c"], "b")  # Should return 1
index = find_in_list(["a", "b", "c"], "z")  # Should return None
```

## Exercise 4: Custom Types and Type Aliases

**File**: `labs/data_typing/custom_types.py`

Create and use custom types and type aliases:

1. Define type aliases: `UserId = str`, `ProductId = int`, `Email = str`, `Price = float`
2. Create a `Person` NamedTuple with name, age, and email fields
3. Create a `Product` TypedDict with id, name, price, and in_stock fields
4. Create a `ShoppingCart` class that uses these types
5. Implement methods: `add_product()`, `remove_product()`, `get_total_price()`
6. Create functions to work with these custom types

**Test your implementation**:
```python
# Test custom types
person = create_person("Alice", 30, "alice@example.com")
print(f"Person: {person}")

product = create_product(101, "Laptop", 999.99, True)
print(f"Product: {product}")

cart = ShoppingCart()
cart.add_product(product)
print(f"Cart total: ${cart.get_total_price()}")
```

## Exercise 5: Advanced Type Hints

**File**: `labs/data_typing/advanced_typing.py`

Implement advanced typing features:

1. Create a generic `Stack[T]` class with push, pop, peek, and is_empty methods
2. Create a generic `Cache[K, V]` class for key-value storage with get, put, and clear methods
3. Implement a function `filter_items(items: List[T], predicate: Callable[[T], bool]) -> List[T]`
4. Create a `Shape` protocol with an `area()` method
5. Implement `Circle` and `Rectangle` classes that implement the Shape protocol
6. Create a function `calculate_total_area(shapes: List[Shape]) -> float`

**Test your implementation**:
```python
# Test generic Stack
stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())  # Should return 2

# Test Shape protocol
shapes = [Circle(5), Rectangle(4, 6)]
total_area = calculate_total_area(shapes)
print(f"Total area: {total_area}")
```

## Exercise 6: Type Checking and Validation

**File**: `labs/data_typing/type_checking.py`

Implement runtime type checking and validation:

1. Create a `TypeValidator` class that validates data against type hints
2. Implement `validate_function_call(func, *args, **kwargs)` that checks argument types
3. Create a data validation system for user registration
4. Implement a function that safely processes mixed-type data
5. Add proper error handling and informative error messages

**Test your implementation**:
```python
# Test type validation
def add(a: int, b: int) -> int:
    return a + b

try:
    result = validate_function_call(add, 5, 3)
    print(f"Result: {result}")
except TypeError as e:
    print(f"Validation error: {e}")

try:
    result = validate_function_call(add, "5", 3)
    print(f"Result: {result}")
except TypeError as e:
    print(f"Validation error: {e}")
```

## Exercise 7: Best Practices

**File**: `labs/data_typing/best_practices.py`

Apply type hinting best practices:

1. Create a well-structured e-commerce system with proper type hints
2. Implement user management with type-safe operations
3. Create product catalog with generic repository pattern
4. Implement order processing with comprehensive type checking
5. Add proper documentation for complex type decisions
6. Use appropriate levels of typing (not over-typed, not under-typed)
7. Handle edge cases gracefully with Optional and Union types

**Test your implementation**:
```python
# Test the complete system
user_manager = UserManager()
product_repo = ProductRepository()

# Create users and products
user = user_manager.create_user("alice", "alice@example.com")
product = product_repo.save(Product(1, "Laptop", 999.99))

# Process orders
order = create_order(user, [product])
total = calculate_order_total(order)
print(f"Order total: ${total}")
```

## Exercise 8: Integration Project

**File**: `labs/data_typing/integration_project.py`

Create a comprehensive integration project that combines all concepts:

1. Build a library management system
2. Implement book catalog with search functionality
3. Create user borrowing system with due dates
4. Add fine calculation for overdue books
5. Implement library statistics and reporting
6. Use all type hinting concepts learned throughout the lab

**Test your implementation**:
```python
# Test the complete library system
library = Library()

# Add books
book1 = library.add_book("Python Basics", "John Doe", "Tech")
book2 = library.add_book("Advanced Python", "Jane Smith", "Tech")

# Register users
user = library.register_user("Alice", "alice@example.com")

# Borrow books
success = library.borrow_book(user.id, book1.id)
print(f"Borrow successful: {success}")

# Return books and calculate fines
fine = library.return_book(user.id, book1.id)
print(f"Fine: ${fine}")

# Generate reports
stats = library.get_statistics()
print(f"Library stats: {stats}")
```

## Submission

1. Complete all exercises in the `labs/data_typing/` files
2. Test your implementations with the provided test cases
3. Compare your solutions with the completed versions in `solutions/data_typing/`
4. Run the demo files to see advanced examples
5. Try running `mypy` on your completed files for static type checking

## Tips

- Start with Exercise 1 and build upon previous exercises
- Use the demo files as references, but implement your own versions
- Test frequently as you implement each function
- Remember that type hints improve code quality and catch errors early
- Use descriptive type aliases for complex types
- Don't over-type simple functions, but do type complex ones
- Use mypy for static type checking: `pip install mypy && mypy your_file.py`

## Additional Resources

- [Python Typing Documentation](https://docs.python.org/3/library/typing.html)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [Real Python Type Hints Guide](https://realpython.com/python-type-checking/)
