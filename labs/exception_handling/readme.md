# Python Exception Handling Lab

This lab will guide you through implementing key exception handling concepts in Python. You'll build upon the concepts demonstrated in the `demos/exception_handling/` folder.

## Prerequisites

Before starting, review the demo files in `demos/exception_handling/` to understand the concepts:

- `basic_try_except.py` - Basic try-except blocks
- `multiple_exceptions.py` - Handling multiple exception types
- `finally_block.py` - Finally blocks for cleanup
- `raise_exceptions.py` - Raising exceptions
- `custom_exceptions.py` - Custom exception classes
- `exception_chaining.py` - Exception chaining
- `context_managers.py` - Context managers with exceptions
- `best_practices.py` - Exception handling best practices

## Lab Structure

- **Starter files**: Located in `labs/exception_handling/`
- **Solutions**: Located in `solutions/exception_handling/` (check after completing exercises)
- **Your work**: Modify the starter files in `labs/exception_handling/`

## Exercise 1: Basic Try-Except

**File**: `labs/exception_handling/basic_exception_handling.py`

Implement basic exception handling for common operations:

1. Create a function `safe_divide(a, b)` that handles division by zero
2. Create a function `safe_list_access(lst, index)` that handles index errors
3. Create a function `safe_int_conversion(value)` that handles conversion errors
4. Test all functions with various inputs

**Test your implementation**:
```python
# Test safe_divide
result = safe_divide(10, 2)  # Should return 5.0
result = safe_divide(10, 0)  # Should handle ZeroDivisionError

# Test safe_list_access
my_list = [1, 2, 3]
result = safe_list_access(my_list, 1)  # Should return 2
result = safe_list_access(my_list, 10)  # Should handle IndexError

# Test safe_int_conversion
result = safe_int_conversion("42")  # Should return 42
result = safe_int_conversion("hello")  # Should handle ValueError
```

## Exercise 2: Multiple Exception Types

**File**: `labs/exception_handling/multiple_exception_types.py`

Implement functions that handle multiple exception types:

1. Create a function `process_user_input(data)` that handles ValueError and TypeError
2. Create a function `read_file_safely(filename)` that handles FileNotFoundError and PermissionError
3. Create a function `network_request(url)` that handles different network errors
4. Test with various error conditions

**Test your implementation**:
```python
# Test process_user_input
result = process_user_input("10")  # Should process successfully
result = process_user_input("abc")  # Should handle ValueError
result = process_user_input([1, 2, 3])  # Should handle TypeError

# Test read_file_safely
content = read_file_safely("existing_file.txt")  # Should read successfully
content = read_file_safely("nonexistent.txt")  # Should handle FileNotFoundError
```

## Exercise 3: Finally Blocks

**File**: `labs/exception_handling/finally_blocks.py`

Implement functions using finally blocks for cleanup:

1. Create a function `file_operation(filename)` that uses finally for file cleanup
2. Create a function `database_transaction()` that uses finally for connection cleanup
3. Create a function `resource_management()` that ensures cleanup happens
4. Test that cleanup occurs even when exceptions are raised

**Test your implementation**:
```python
# Test file_operation
result = file_operation("test.txt")  # Should handle file operations with cleanup
result = file_operation("nonexistent.txt")  # Should cleanup even on error

# Test database_transaction
result = database_transaction()  # Should perform transaction with cleanup
```

## Exercise 4: Raising Exceptions

**File**: `labs/exception_handling/raising_exceptions.py`

Implement functions that raise exceptions for validation:

1. Create a function `validate_age(age)` that raises ValueError for invalid ages
2. Create a function `validate_password(password)` that raises exceptions for weak passwords
3. Create a function `withdraw_money(balance, amount)` that raises exceptions for invalid withdrawals
4. Test exception raising and catching

**Test your implementation**:
```python
# Test validate_age
try:
    validate_age(25)  # Should pass
    validate_age(-5)  # Should raise ValueError
except ValueError as e:
    print(f"Age validation error: {e}")

# Test validate_password
try:
    validate_password("Strong123")  # Should pass
    validate_password("weak")  # Should raise ValueError
except ValueError as e:
    print(f"Password validation error: {e}")
```

## Exercise 5: Custom Exceptions

**File**: `labs/exception_handling/custom_exceptions.py`

Create and use custom exception classes:

1. Create custom exception classes: `InsufficientFundsError`, `InvalidAmountError`, `AccountNotFoundError`
2. Create a `BankAccount` class that uses these exceptions
3. Implement `deposit()`, `withdraw()`, and `transfer()` methods
4. Create a function to find accounts with exception handling

**Test your implementation**:
```python
# Test custom exceptions
try:
    account = BankAccount("ACC001", 1000)
    account.deposit(500)
    account.withdraw(2000)  # Should raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Funds error: {e}")

try:
    account.deposit(-100)  # Should raise InvalidAmountError
except InvalidAmountError as e:
    print(f"Amount error: {e}")
```

## Exercise 6: Exception Chaining

**File**: `labs/exception_handling/exception_chaining.py`

Implement exception chaining with `raise from`:

1. Create a multi-level function call chain that chains exceptions
2. Create a data processing function that chains parsing errors
3. Implement file operations with chained exceptions
4. Test that `__cause__` attributes are preserved

**Test your implementation**:
```python
# Test exception chaining
try:
    high_level_operation()
except Exception as e:
    print(f"Error: {e}")
    if e.__cause__:
        print(f"Caused by: {e.__cause__}")
```

## Exercise 7: Context Managers

**File**: `labs/exception_handling/context_managers.py`

Implement context managers for resource management:

1. Create a custom context manager class for file handling
2. Create a context manager for database connections
3. Use context managers in functions with proper exception handling
4. Test cleanup behavior with exceptions

**Test your implementation**:
```python
# Test context managers
try:
    with FileHandler("test.txt", 'w') as f:
        f.write("Hello World")
        # Simulate error
        raise ValueError("Test error")
except ValueError:
    print("Error occurred, but file should be closed")
```

## Exercise 8: Best Practices

**File**: `labs/exception_handling/best_practices.py`

Apply exception handling best practices:

1. Avoid bare `except:` clauses
2. Catch specific exceptions, not `Exception`
3. Use finally for cleanup instead of bare except
4. Provide meaningful error messages
5. Don't suppress important exceptions
6. Log errors appropriately

**Test your implementation**:
```python
# Test best practices
result = safe_operation()  # Should handle errors properly
result = another_safe_operation()  # Should log errors
```

## Exercise 9: Exception Handling with Files

**File**: `labs/exception_handling/files_and_exceptions.py`

Practice exception handling when reading and writing text files and CSV files.

Two sample files are provided in `labs/exception_handling/` to use during the exercises:
- `sample_text.txt` – a plain text file with 10 lines
- `sample_data.csv` – a CSV file with columns `id`, `name`, and `value`; some rows contain intentionally bad data so you can practice skipping invalid entries

### Part 1 – Text files

1. `read_text_file(filepath)` – read a file and handle `FileNotFoundError`, `PermissionError`, and `OSError`
2. `write_text_file(filepath, content)` – write content to a file and return `True`/`False`
3. `append_to_text_file(filepath, line)` – append a line and handle errors gracefully
4. `count_lines(filepath)` – count lines in a file, returning `-1` on error

### Part 2 – CSV files

5. `read_csv_file(filepath)` – read a CSV with a header row into a list of dicts using `csv.DictReader`
6. `write_csv_file(filepath, fieldnames, rows)` – write a list of dicts to a CSV using `csv.DictWriter`; raise `ValueError` for empty `fieldnames`
7. `get_csv_column(filepath, column_name)` – return all values in a named column; handle a missing column with `KeyError`

### Part 3 – Putting it together

8. `process_csv_safely(filepath, output_filepath)` – read a CSV with `id` and `value` columns, skip rows where `value` is not a valid float, and write a new CSV that adds a `squared` column

**Test your implementation**:
```python
# Part 1 – use the provided sample_text.txt
print(read_text_file("sample_text.txt"))     # prints file contents
print(count_lines("sample_text.txt"))        # 10
append_to_text_file("sample_text.txt", "Line 11: appended!")
print(read_text_file("missing.txt"))         # "File not found: missing.txt"

# Part 2 – use the provided sample_data.csv
print(read_csv_file("sample_data.csv"))      # list of dicts, one per row
print(get_csv_column("sample_data.csv", "name"))   # ['Alice', 'Bob', ...]
print(get_csv_column("sample_data.csv", "score"))  # [] with a 'column not found' message

# Part 3 – process sample_data.csv; rows with bad 'value' entries should be skipped
process_csv_safely("sample_data.csv", "processed_output.csv")
print(read_csv_file("processed_output.csv"))  # rows with 'squared' column added
```

## Submission

1. Complete all exercises in the `labs/exception_handling/` files
2. Test your implementations with the provided test cases
3. Compare your solutions with the completed versions in `solutions/exception_handling/`
4. Run the demo files to see advanced examples

## Tips

- Start with Exercise 1 and build upon previous exercises
- Use the demo files as references, but implement your own versions
- Test frequently as you implement each function
- Remember that good exception handling is about failing gracefully
- Use specific exception types rather than catching everything
