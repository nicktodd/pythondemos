# Exercise 2: Multiple Exception Types

def process_user_input(data):
    """Process user input, handling multiple exception types"""
    try:
        # Try to convert to int and perform operation
        num = int(data)
        result = 100 / num
        print(f"Successfully processed {data}: result = {result}")
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

def read_file_safely(filename):
    """Read a file safely, handling multiple file-related exceptions"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Successfully read {len(content)} characters from {filename}")
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

def network_request(url):
    """Simulate a network request, handling different network errors"""
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

# Test code
if __name__ == "__main__":
    print("=== Multiple Exception Types Tests ===\n")

    # Test process_user_input
    test_inputs = ["10", "0", "abc", [1, 2, 3]]
    for data in test_inputs:
        print(f"Processing: {data}")
        result = process_user_input(data)
        print(f"Result: {result}\n")

    # Test read_file_safely
    files_to_test = ["basic_exception_handling.py", "nonexistent.txt"]
    for filename in files_to_test:
        print(f"Reading: {filename}")
        content = read_file_safely(filename)
        if content:
            print(f"Content length: {len(content)}")
        print()

    # Test network_request
    urls = ["http://example.com", "invalid", "timeout", "forbidden"]
    for url in urls:
        print(f"Requesting: {url}")
        result = network_request(url)
        print(f"Result: {result}\n")
