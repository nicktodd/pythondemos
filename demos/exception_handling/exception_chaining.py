# Exception Chaining

def low_level_operation():
    """Simulate a low-level operation that raises an exception"""
    raise ValueError("Low-level operation failed")

def middle_level_operation():
    """Middle-level operation that catches and re-raises with chaining"""
    try:
        low_level_operation()
    except ValueError as e:
        # Re-raise with chaining to preserve original exception
        raise RuntimeError("Middle-level operation encountered an error") from e

def high_level_operation():
    """High-level operation that handles chained exceptions"""
    try:
        middle_level_operation()
    except RuntimeError as e:
        print(f"High-level caught RuntimeError: {e}")
        print(f"Original cause: {e.__cause__}")
        # Could choose to re-raise or handle
        raise

def process_data(data):
    """Demonstrate exception chaining in data processing"""
    try:
        # Step 1: Validate data
        if not isinstance(data, str):
            raise TypeError("Data must be a string")

        # Step 2: Parse data
        try:
            value = int(data)
        except ValueError as parse_error:
            raise ValueError(f"Failed to parse '{data}' as integer") from parse_error

        # Step 3: Validate range
        if value < 0 or value > 100:
            raise ValueError(f"Value {value} is out of valid range (0-100)")

        return value

    except Exception as e:
        # Log the full chain
        print(f"Data processing failed: {e}")
        if e.__cause__:
            print(f"Caused by: {e.__cause__}")
        return None

def suppress_chaining():
    """Demonstrate suppressing the exception chain"""
    try:
        low_level_operation()
    except ValueError:
        # Suppress chaining by not using 'from'
        raise RuntimeError("Operation failed (chain suppressed)")

def chained_file_operations():
    """Demonstrate chaining in file operations"""
    try:
        # Try to open a file
        try:
            with open("nonexistent.txt", 'r') as f:
                content = f.read()
        except FileNotFoundError as file_error:
            raise IOError("Failed to access required file") from file_error

    except IOError as io_error:
        print(f"File operation failed: {io_error}")
        print(f"Root cause: {io_error.__cause__}")

# Test exception chaining
if __name__ == "__main__":
    print("=== Exception Chaining Demo ===\n")

    # Basic chaining
    try:
        high_level_operation()
    except Exception as e:
        print(f"Final exception: {e}")
        if hasattr(e, '__cause__') and e.__cause__:
            print(f"Caused by: {e.__cause__}")

    print()

    # Data processing with chaining
    test_data = ["42", "abc", "150", [1, 2, 3]]
    for data in test_data:
        print(f"Processing: {data}")
        result = process_data(data)
        if result is not None:
            print(f"Result: {result}")
        print()

    # Suppressed chaining
    try:
        suppress_chaining()
    except RuntimeError as e:
        print(f"Suppressed chain: {e}")
        print(f"Has cause: {hasattr(e, '__cause__')}")

    print()

    # File operations chaining
    chained_file_operations()
