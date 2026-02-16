# Exercise 7: Context Managers

class FileHandler:
    """Custom context manager for file operations"""

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

class DatabaseConnection:
    """Context manager for database connections"""

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
        self.connection = None
        return False  # Don't suppress the exception

def process_with_file_handler(filename):
    """Use FileHandler context manager"""
    try:
        with FileHandler(filename, 'r') as file:
            content = file.read()
            print(f"Read {len(content)} characters")
            # Simulate processing that might fail
            if "error" in content.lower():
                raise RuntimeError("Processing failed due to content")
            return content
    except (IOError, RuntimeError) as e:
        print(f"File processing error: {e}")
        return None

def process_with_database():
    """Use DatabaseConnection context manager"""
    try:
        with DatabaseConnection("postgresql://localhost/mydb") as conn:
            print(f"Performing operations with: {conn}")
            # Simulate work
            if False:  # Change to True to test exception
                raise ValueError("Database operation failed")
            print("Operations completed successfully")
    except ValueError as e:
        print(f"Database operation error: {e}")

# Test code
if __name__ == "__main__":
    print("=== Context Managers Tests ===\n")

    # Test FileHandler
    print("Testing FileHandler with existing file:")
    result = process_with_file_handler("basic_exception_handling.py")
    print()

    print("Testing FileHandler with nonexistent file:")
    result = process_with_file_handler("nonexistent.txt")
    print()

    # Test DatabaseConnection
    print("Testing DatabaseConnection:")
    process_with_database()
    print()

    # Test built-in context manager
    print("Testing built-in file context manager:")
    try:
        with open("basic_exception_handling.py", 'r') as file:
            content = file.read()
            print(f"Read {len(content)} characters with built-in context manager")
    except IOError as e:
        print(f"Built-in context manager error: {e}")
