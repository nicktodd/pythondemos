"""
Async Context Managers Demo
===========================

Demonstrates async context managers and their usage patterns.
"""

import asyncio
import time
import random
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Any

class AsyncDatabaseConnection:
    """Simulate an async database connection."""

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connected = False
        self.connection_id = None

    async def __aenter__(self):
        """Async context manager entry."""
        print(f"Connecting to database: {self.connection_string}")
        await asyncio.sleep(0.5)  # Connection time
        self.connected = True
        self.connection_id = f"conn_{hash(self.connection_string) % 1000}"
        print(f"Connected successfully (ID: {self.connection_id})")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        print(f"Closing connection {self.connection_id}")
        await asyncio.sleep(0.2)  # Cleanup time
        self.connected = False
        print(f"Connection {self.connection_id} closed")
        return False  # Don't suppress exceptions

    async def execute_query(self, query: str):
        """Execute a database query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")

        print(f"Executing query: {query}")
        await asyncio.sleep(0.3)  # Query execution time
        # Simulate query result
        result = f"Result for: {query}"
        print(f"Query completed: {result}")
        return result

class AsyncFileHandler:
    """Async file handler with proper resource management."""

    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    async def __aenter__(self):
        """Open file asynchronously."""
        print(f"Opening file: {self.filename}")
        await asyncio.sleep(0.1)  # Simulate file open time
        # In real code, this would be: self.file = await aiofiles.open(self.filename, self.mode)
        self.file = f"mock_file_handle_{self.filename}"
        print(f"File opened: {self.file}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close file asynchronously."""
        print(f"Closing file: {self.filename}")
        await asyncio.sleep(0.05)  # Simulate file close time
        self.file = None
        print(f"File closed: {self.filename}")
        return False

    async def read(self) -> str:
        """Read from file."""
        if not self.file:
            raise RuntimeError("File not open")
        print(f"Reading from {self.filename}")
        await asyncio.sleep(0.2)  # Simulate read time
        content = f"Content of {self.filename}"
        print(f"Read complete: {content}")
        return content

    async def write(self, data: str):
        """Write to file."""
        if not self.file:
            raise RuntimeError("File not open")
        print(f"Writing to {self.filename}: {data}")
        await asyncio.sleep(0.15)  # Simulate write time
        print(f"Write complete: {self.filename}")

@asynccontextmanager
async def async_timer(description: str) -> AsyncGenerator[None, None]:
    """Async context manager for timing operations."""
    print(f"Starting: {description}")
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print(f"Finished: {description} (took {duration:.2f} seconds)")

@asynccontextmanager
async def async_transaction(connection):
    """Async context manager for database transactions."""
    print("Starting transaction...")
    await connection.execute_query("BEGIN TRANSACTION")

    try:
        yield connection
        await connection.execute_query("COMMIT")
        print("Transaction committed")
    except Exception as e:
        await connection.execute_query("ROLLBACK")
        print(f"Transaction rolled back due to: {e}")
        raise

class AsyncResourcePool:
    """Pool of async resources with context manager support."""

    def __init__(self, max_resources: int = 3):
        self.max_resources = max_resources
        self.available_resources = max_resources
        self.semaphore = asyncio.Semaphore(max_resources)

    @asynccontextmanager
    async def acquire(self) -> AsyncGenerator[str, None]:
        """Acquire a resource from the pool."""
        async with self.semaphore:
            resource_id = f"resource_{self.max_resources - self.available_resources + 1}"
            print(f"Acquired {resource_id}")
            try:
                yield resource_id
            finally:
                print(f"Released {resource_id}")

async def main():
    """Demonstrate async context managers."""
    print("=== Async Context Managers Demo ===\n")

    # 1. Basic async context manager usage
    print("1. Database connection context manager:")
    async with AsyncDatabaseConnection("postgresql://localhost/mydb") as db:
        result1 = await db.execute_query("SELECT * FROM users")
        result2 = await db.execute_query("SELECT * FROM products")
    print("Database operations completed\n")

    # 2. File handling with async context manager
    print("2. Async file handling:")
    async with AsyncFileHandler("data.txt", "r") as file:
        content = await file.read()
        print(f"File content: {content}")

    async with AsyncFileHandler("output.txt", "w") as file:
        await file.write("Hello, async world!")
    print()

    # 3. Nested context managers
    print("3. Nested context managers:")
    async with async_timer("Database operations with timing"):
        async with AsyncDatabaseConnection("sqlite:///test.db") as db:
            async with async_timer("Query execution"):
                result = await db.execute_query("SELECT COUNT(*) FROM table")
    print()

    # 4. Transaction management
    print("4. Transaction context manager:")
    async with AsyncDatabaseConnection("postgresql://localhost/transactions") as db:
        try:
            async with async_transaction(db):
                await db.execute_query("INSERT INTO users (name) VALUES ('Alice')")
                await db.execute_query("INSERT INTO users (name) VALUES ('Bob')")
                # Simulate an error
                if random.choice([True, False]):
                    raise Exception("Simulated transaction error")
        except Exception as e:
            print(f"Transaction failed: {e}")

        # This should still work since we're outside the transaction
        result = await db.execute_query("SELECT COUNT(*) FROM users")
    print()

    # 5. Resource pool
    print("5. Resource pool with context manager:")
    pool = AsyncResourcePool(max_resources=2)

    async def use_resource(task_id: int):
        async with pool.acquire() as resource:
            print(f"Task {task_id} using {resource}")
            await asyncio.sleep(random.uniform(0.1, 0.5))
            print(f"Task {task_id} finished with {resource}")

    # Run multiple tasks competing for resources
    await asyncio.gather(
        use_resource(1),
        use_resource(2),
        use_resource(3),
        use_resource(4)
    )
    print()

    # 6. Exception handling in context managers
    print("6. Exception handling in context managers:")
    try:
        async with AsyncFileHandler("nonexistent.txt", "r") as file:
            # This will work fine
            content = await file.read()
            # Simulate an error
            raise ValueError("Simulated error during file processing")
    except ValueError as e:
        print(f"Caught exception: {e}")
    # File should still be properly closed due to context manager
    print("File context manager ensured proper cleanup despite exception\n")

    # 7. Multiple context managers in one async with
    print("7. Multiple context managers:")
    async with AsyncDatabaseConnection("db1") as db1, \
               AsyncDatabaseConnection("db2") as db2, \
               async_timer("Multiple DB operations"):
        result1 = await db1.execute_query("SELECT * FROM table1")
        result2 = await db2.execute_query("SELECT * FROM table2")
    print("All context managers properly closed")

if __name__ == "__main__":
    asyncio.run(main())
