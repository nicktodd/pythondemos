# Basic Try-Except Exception Handling

def divide_numbers(a, b):
    """Demonstrate basic try-except block"""
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

def access_list_element(lst, index):
    """Demonstrate exception handling for list access"""
    try:
        value = lst[index]
        print(f"Element at index {index}: {value}")
        return value
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None

def convert_to_int(value):
    """Demonstrate exception handling for type conversion"""
    try:
        num = int(value)
        print(f"Successfully converted '{value}' to {num}")
        return num
    except ValueError:
        print(f"Error: Cannot convert '{value}' to integer!")
        return None

# Test the functions
if __name__ == "__main__":
    print("=== Basic Try-Except Demo ===\n")

    # Division examples
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    divide_numbers("10", 2)

    print()

    # List access examples
    my_list = [1, 2, 3, 4, 5]
    access_list_element(my_list, 2)
    access_list_element(my_list, 10)

    print()

    # Type conversion examples
    convert_to_int("42")
    convert_to_int("hello")
    convert_to_int(3.14)
