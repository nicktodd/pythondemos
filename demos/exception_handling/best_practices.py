# Exception Handling Best Practices

def bad_practice_bare_except():
    """Demonstrate what NOT to do - bare except"""
    try:
        result = 10 / 0
    except:  # This catches everything, including KeyboardInterrupt!
        print("Something went wrong")
        return None

def good_practice_specific_exceptions():
    """Demonstrate catching specific exceptions"""
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Type error in division")
        return None

def bad_practice_catch_all():
    """Another bad practice - catching Exception"""
    try:
        risky_operation()
    except Exception:  # Too broad, catches programming errors
        print("Something went wrong")
        return None

def good_practice_catch_what_you_handle():
    """Catch only what you can handle"""
    try:
        risky_operation()
    except ValueError:
        print("Invalid value provided")
        return None
    except ConnectionError:
        print("Network connection failed")
        return None
    # Let other exceptions propagate

def risky_operation():
    """Simulate an operation that might fail"""
    import random
    if random.choice([True, False]):
        raise ValueError("Invalid input")
    elif random.choice([True, False]):
        raise ConnectionError("Network timeout")
    else:
        return "Success"

def bad_practice_silent_failure():
    """Don't hide errors"""
    try:
        result = int("not_a_number")
    except ValueError:
        pass  # Silent failure - bad!
    return None

def good_practice_log_and_handle():
    """Log errors and handle appropriately"""
    import logging
    try:
        result = int("not_a_number")
        return result
    except ValueError as e:
        logging.error(f"Failed to convert to int: {e}")
        print("Could not convert to integer")
        return None

def bad_practice_large_try_blocks():
    """Don't put too much code in try blocks"""
    try:
        # Too much code here
        x = 1
        y = 2
        z = x + y
        result = z / 0  # Error here
        more_code = result * 2
    except ZeroDivisionError:
        print("Division by zero")
        # Now we don't know which operation failed

def good_practice_minimal_try_blocks():
    """Keep try blocks focused"""
    x = 1
    y = 2
    z = x + y

    try:
        result = z / 0
    except ZeroDivisionError:
        print("Division by zero in calculation")
        result = 0

    more_code = result * 2

def proper_cleanup_with_finally():
    """Use finally for cleanup"""
    file = None
    try:
        file = open("example.txt", 'w')
        file.write("Hello World")
    except IOError as e:
        print(f"File error: {e}")
    finally:
        if file:
            file.close()
            print("File closed")

def use_context_managers():
    """Prefer context managers for resource management"""
    try:
        with open("example.txt", 'w') as file:
            file.write("Hello World")
        print("File automatically closed")
    except IOError as e:
        print(f"File error: {e}")

def avoid_empty_except():
    """Don't use empty except blocks"""
    try:
        risky_operation()
    except ValueError:
        # At minimum, log the error
        print("ValueError occurred")
        raise  # Re-raise if you can't handle it

def provide_meaningful_messages():
    """Give meaningful error messages"""
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
    except ValueError as e:
        print(f"Invalid age: {e}")
        return None
    return age

# Test the best practices
if __name__ == "__main__":
    print("=== Exception Handling Best Practices ===\n")

    print("1. Bad practice - bare except:")
    bad_practice_bare_except()

    print("\n2. Good practice - specific exceptions:")
    good_practice_specific_exceptions()

    print("\n3. Bad practice - catch all Exception:")
    bad_practice_catch_all()

    print("\n4. Good practice - catch what you handle:")
    good_practice_catch_what_you_handle()

    print("\n5. Bad practice - silent failure:")
    bad_practice_silent_failure()

    print("\n6. Good practice - log and handle:")
    good_practice_log_and_handle()

    print("\n7. Bad practice - large try blocks:")
    bad_practice_large_try_blocks()

    print("\n8. Good practice - minimal try blocks:")
    good_practice_minimal_try_blocks()

    print("\n9. Proper cleanup with finally:")
    proper_cleanup_with_finally()

    print("\n10. Use context managers:")
    use_context_managers()

    print("\n11. Avoid empty except:")
    try:
        avoid_empty_except()
    except ValueError:
        print("ValueError was re-raised as expected")

    print("\n12. Provide meaningful messages:")
    provide_meaningful_messages()
