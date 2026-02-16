# Exercise 1: Basic Try-Except

def safe_divide(a, b):
    """Safely divide two numbers, handling division by zero"""
    try:
        result = a / b
        print(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid types for division!")
        return None

def safe_list_access(lst, index):
    """Safely access a list element, handling index errors"""
    try:
        value = lst[index]
        print(f"Element at index {index}: {value}")
        return value
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None

def safe_int_conversion(value):
    """Safely convert a value to integer, handling conversion errors"""
    try:
        num = int(value)
        print(f"Successfully converted '{value}' to {num}")
        return num
    except ValueError:
        print(f"Error: Cannot convert '{value}' to integer!")
        return None

# Test code
if __name__ == "__main__":
    print("=== Basic Exception Handling Tests ===\n")

    # Test safe_divide
    result = safe_divide(10, 2)
    print(f"Result: {result}\n")

    result = safe_divide(10, 0)
    print(f"Result: {result}\n")

    result = safe_divide("10", 2)
    print(f"Result: {result}\n")

    # Test safe_list_access
    my_list = [1, 2, 3]
    result = safe_list_access(my_list, 1)
    print(f"Result: {result}\n")

    result = safe_list_access(my_list, 10)
    print(f"Result: {result}\n")

    # Test safe_int_conversion
    result = safe_int_conversion("42")
    print(f"Result: {result}\n")

    result = safe_int_conversion("hello")
    print(f"Result: {result}\n")

    result = safe_int_conversion(3.14)
    print(f"Result: {result}\n")
