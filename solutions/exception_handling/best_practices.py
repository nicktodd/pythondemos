# Exercise 8: Best Practices

import logging

def safe_operation():
    """Demonstrate proper exception handling - avoid bare except"""
    try:
        result = 10 / 2  # This will succeed
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid types for operation")
        return None

def another_safe_operation():
    """Demonstrate logging errors instead of silent failure"""
    try:
        result = int("not_a_number")
        return result
    except ValueError as e:
        logging.error(f"Failed to convert to int: {e}")
        print("Could not convert to integer")
        return None

def proper_cleanup():
    """Use finally for cleanup instead of bare except"""
    file = None
    try:
        file = open("example.txt", 'w')
        file.write("Hello World")
        print("File written successfully")
    except IOError as e:
        print(f"File error: {e}")
    finally:
        if file:
            file.close()
            print("File closed properly")

def meaningful_error_messages():
    """Provide meaningful error messages"""
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
        return age
    except ValueError as e:
        print(f"Invalid age provided: {e}")
        return None
    except KeyboardInterrupt:
        print("Operation cancelled by user")
        return None

def avoid_bare_except():
    """Avoid bare except clauses"""
    try:
        # Some operation
        result = 10 / 2
        return result
    except ZeroDivisionError:
        print("Division by zero")
        return None
    # Don't use bare except - it catches everything including KeyboardInterrupt

def log_and_handle():
    """Log errors and handle appropriately"""
    try:
        risky_operation()
    except ValueError as e:
        logging.warning(f"Value error occurred: {e}")
        print("Handled value error")
        return False
    except ConnectionError as e:
        logging.error(f"Connection failed: {e}")
        print("Connection error - retrying...")
        return False
    return True

def risky_operation():
    """Simulate an operation that might fail"""
    import random
    if random.choice([True, False]):
        raise ValueError("Random value error")
    elif random.choice([True, False]):
        raise ConnectionError("Random connection error")
    else:
        print("Operation succeeded")
        return True

# Test code
if __name__ == "__main__":
    print("=== Best Practices Tests ===\n")

    # Test safe_operation
    result = safe_operation()
    print(f"Safe operation result: {result}\n")

    # Test another_safe_operation
    result = another_safe_operation()
    print(f"Another safe operation result: {result}\n")

    # Test proper_cleanup
    proper_cleanup()
    print()

    # Test meaningful_error_messages (commented to avoid input)
    # result = meaningful_error_messages()
    # print(f"Age result: {result}\n")

    # Test avoid_bare_except
    result = avoid_bare_except()
    print(f"Avoid bare except result: {result}\n")

    # Test log_and_handle
    result = log_and_handle()
    print(f"Log and handle result: {result}")
