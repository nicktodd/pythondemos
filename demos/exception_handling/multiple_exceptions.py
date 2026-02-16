# Multiple Exception Types Handling

def process_data(data):
    """Demonstrate handling multiple exception types"""
    try:
        # Try to convert to int and divide
        num = int(data)
        result = 100 / num
        print(f"Processed {data}: result = {result}")
        return result
    except ValueError as e:
        print(f"ValueError: {data} is not a valid integer - {e}")
        return None
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: Cannot divide by {data} - {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def read_file_content(filename):
    """Demonstrate file handling with multiple exceptions"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File '{filename}' read successfully")
            return content
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {filename} does not exist - {e}")
        return None
    except PermissionError as e:
        print(f"PermissionError: Cannot access {filename} - {e}")
        return None
    except IOError as e:
        print(f"IOError: Problem reading {filename} - {e}")
        return None

def network_operation(url):
    """Simulate network operation with multiple exceptions"""
    try:
        # Simulate network call
        if url == "invalid":
            raise ValueError("Invalid URL format")
        elif url == "timeout":
            raise TimeoutError("Connection timed out")
        elif url == "forbidden":
            raise PermissionError("Access forbidden")
        else:
            print(f"Successfully connected to {url}")
            return f"Data from {url}"
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TimeoutError as e:
        print(f"TimeoutError: {e}")
        return None
    except PermissionError as e:
        print(f"PermissionError: {e}")
        return None

# Test the functions
if __name__ == "__main__":
    print("=== Multiple Exceptions Demo ===\n")

    # Data processing examples
    process_data("10")
    process_data("0")
    process_data("abc")
    process_data([1, 2, 3])

    print()

    # File reading examples
    read_file_content("nonexistent.txt")
    read_file_content("basic_try_except.py")  # Assuming this file exists

    print()

    # Network operation examples
    network_operation("http://example.com")
    network_operation("invalid")
    network_operation("timeout")
    network_operation("forbidden")
