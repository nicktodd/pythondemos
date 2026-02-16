# Context Managers and Exceptions

class DatabaseConnection:
    """Custom context manager for database connections"""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def __enter__(self):
        # Setup: establish connection
        print(f"Connecting to database: {self.connection_string}")
        self.connection = f"Connection to {self.connection_string}"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup: close connection
        print("Closing database connection")
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
            # Could log, rollback transaction, etc.
        self.connection = None
        return False  # Don't suppress the exception

class FileHandler:
    """Context manager for file operations with exception handling"""

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            print(f"Opened file: {self.filename}")
            return self.file
        except IOError as e:
            print(f"Failed to open file {self.filename}: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            try:
                self.file.close()
                print(f"Closed file: {self.filename}")
            except Exception as e:
                print(f"Error closing file: {e}")
                return False
        return False

def process_with_database():
    """Demonstrate context manager with database operations"""
    try:
        with DatabaseConnection("postgresql://localhost/mydb") as conn:
            print(f"Performing database operations with: {conn}")
            # Simulate work
            if False:  # Change to True to test exception
                raise ValueError("Database operation failed")
            print("Database operations completed successfully")
    except ValueError as e:
        print(f"Database operation error: {e}")

def process_file_safely(filename):
    """Demonstrate file handling with context manager"""
    try:
        with FileHandler(filename, 'r') as file:
            content = file.read()
            print(f"Read {len(content)} characters from {filename}")
            # Simulate processing that might fail
            if "error" in content.lower():
                raise RuntimeError("Processing failed due to content")
            return content
    except (IOError, RuntimeError) as e:
        print(f"File processing error: {e}")
        return None

def nested_context_managers():
    """Demonstrate nested context managers"""
    try:
        with DatabaseConnection("db1") as db1:
            print("Working with db1")
            with FileHandler("basic_try_except.py", 'r') as file:
                print("Working with file")
                # Simulate nested operations
                if True:  # Change to test exception
                    raise Exception("Nested operation failed")
                print("All nested operations completed")
    except Exception as e:
        print(f"Nested operation error: {e}")

# Using built-in context managers
def builtin_context_managers():
    """Demonstrate built-in context managers like open()"""
    try:
        with open("basic_try_except.py", 'r') as file:
            content = file.read()
            print(f"Read file with built-in context manager: {len(content)} chars")
            # Simulate error
            if False:
                raise ValueError("Processing error")
    except (IOError, ValueError) as e:
        print(f"Built-in context manager error: {e}")

# Test the context managers
if __name__ == "__main__":
    print("=== Context Managers Demo ===\n")

    # Database operations
    process_with_database()
    print()

    # File operations
    process_file_safely("basic_try_except.py")
    process_file_safely("nonexistent.txt")
    print()

    # Nested context managers
    nested_context_managers()
    print()

    # Built-in context managers
    builtin_context_managers()
