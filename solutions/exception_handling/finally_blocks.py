# Exercise 3: Finally Blocks

def file_operation(filename):
    """Perform file operations with finally block for cleanup"""
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"Successfully read {len(content)} characters from {filename}")
        return content
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return None
    except IOError as e:
        print(f"IOError: {e}")
        return None
    finally:
        # This always executes
        if file:
            file.close()
            print(f"File {filename} closed in finally block")
        else:
            print("No file to close")

def database_transaction():
    """Simulate database transaction with finally for cleanup"""
    connection = None
    transaction_started = False
    try:
        # Simulate connection
        connection = "DatabaseConnection"
        print("Database connected successfully")

        # Simulate transaction start
        transaction_started = True
        print("Transaction started")

        # Simulate some work that might fail
        if True:  # Change to False to test success
            print("Database operation completed successfully")
        else:
            raise Exception("Database operation failed")

    except Exception as e:
        print(f"Database error: {e}")
        # Could rollback transaction here
        if transaction_started:
            print("Transaction rolled back")
    finally:
        # Always cleanup resources
        if connection:
            # Simulate closing connection
            print("Database connection closed")
            connection = None

def resource_management():
    """Demonstrate resource management with finally"""
    resource = None
    try:
        resource = "SomeResource"
        print(f"Acquired resource: {resource}")

        # Simulate work that might fail
        if False:  # Change to True to test exception
            raise ValueError("Something went wrong during work")
        else:
            print("Work completed successfully")

    except ValueError as e:
        print(f"Error during work: {e}")
    finally:
        # Cleanup always happens
        if resource:
            print(f"Released resource: {resource}")
            resource = None
        print("Cleanup completed")

# Test code
if __name__ == "__main__":
    print("=== Finally Blocks Tests ===\n")

    # Test file_operation
    print("Testing file operation with existing file:")
    result = file_operation("basic_exception_handling.py")
    print()

    print("Testing file operation with nonexistent file:")
    result = file_operation("nonexistent.txt")
    print()

    # Test database_transaction
    print("Testing database transaction:")
    result = database_transaction()
    print()

    # Test resource_management
    print("Testing resource management:")
    resource_management()
