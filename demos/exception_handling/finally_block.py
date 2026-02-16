# Finally Block in Exception Handling

def file_operations(filename):
    """Demonstrate finally block for cleanup"""
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
        # This always executes, regardless of exceptions
        if file:
            file.close()
            print(f"File {filename} closed in finally block")
        else:
            print("No file to close")

def database_connection():
    """Simulate database operations with finally"""
    connection = None
    try:
        # Simulate connection
        connection = "DatabaseConnection"
        print("Database connected successfully")

        # Simulate some operation that might fail
        if True:  # Simulate success
            print("Database operation completed")
        else:
            raise Exception("Database operation failed")

    except Exception as e:
        print(f"Database error: {e}")
        # Could rollback transaction here
        print("Transaction rolled back")
    finally:
        # Always cleanup resources
        if connection:
            # Simulate closing connection
            print("Database connection closed")
            connection = None

def resource_management():
    """Demonstrate finally for general resource cleanup"""
    resource = None
    try:
        resource = "SomeResource"
        print(f"Acquired resource: {resource}")

        # Simulate work that might fail
        if False:  # Change to True to test exception
            raise ValueError("Something went wrong")
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

# Test the functions
if __name__ == "__main__":
    print("=== Finally Block Demo ===\n")

    # File operations
    file_operations("nonexistent.txt")
    print()
    file_operations("basic_try_except.py")  # Assuming this exists
    print()

    # Database simulation
    database_connection()
    print()

    # Resource management
    resource_management()
