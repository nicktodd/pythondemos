"""
Async Python Lab - Exercise 4: Async Context Managers

Implement async context managers for proper resource management.
Complete the TODO sections with your implementations.
"""

import asyncio
import time
from typing import Any, Optional
from contextlib import asynccontextmanager


# TODO: Implement AsyncFileHandler class
class AsyncFileHandler:
    """
    Async context manager for file operations.
    """

    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    async def __aenter__(self):
        """Enter the async context manager"""
        # Simulate opening file asynchronously
        await asyncio.sleep(0.1)
        print(f"Opening file: {self.filename}")
        # In real implementation, you'd use aiofiles or similar
        # For this demo, we'll simulate with regular open
        self.file = open(self.filename, self.mode)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the async context manager"""
        # Simulate closing file asynchronously
        await asyncio.sleep(0.05)
        if self.file:
            self.file.close()
            print(f"Closed file: {self.filename}")
        return False  # Don't suppress exceptions

    async def read(self) -> str:
        """Read file content"""
        if not self.file:
            raise RuntimeError("File not opened")
        # Simulate async read
        await asyncio.sleep(0.1)
        return self.file.read()

    async def write(self, content: str):
        """Write content to file"""
        if not self.file:
            raise RuntimeError("File not opened")
        # Simulate async write
        await asyncio.sleep(0.1)
        self.file.write(content)
        self.file.flush()


# TODO: Implement AsyncDatabaseConnection class
class AsyncDatabaseConnection:
    """
    Async context manager for database connections.
    """

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None
        self.connected = False

    async def __aenter__(self):
        """Establish database connection"""
        print(f"Connecting to database: {self.connection_string}")
        # Simulate connection time
        await asyncio.sleep(0.2)

        # Simulate successful connection
        self.connection = f"Connection to {self.connection_string}"
        self.connected = True
        print("Database connected")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Close database connection"""
        print("Closing database connection...")
        # Simulate cleanup time
        await asyncio.sleep(0.1)

        if self.connection:
            self.connection = None
            self.connected = False
            print("Database connection closed")
        return False

    async def execute_query(self, query: str) -> str:
        """Execute a database query"""
        if not self.connected:
            raise RuntimeError("Not connected to database")

        print(f"Executing query: {query}")
        # Simulate query execution time
        await asyncio.sleep(0.3)

        # Simulate query result
        return f"Result for query: {query}"


# TODO: Implement AsyncTimer context manager
@asynccontextmanager
async def AsyncTimer():
    """
    Async context manager that measures execution time.
    """
    start_time = time.time()
    print("Timer started...")

    # Create a simple object to hold elapsed time
    class TimerResult:
        def __init__(self):
            self.elapsed = 0.0

    timer = TimerResult()

    try:
        yield timer
    finally:
        end_time = time.time()
        timer.elapsed = end_time - start_time
        print(".2f")


# TODO: Implement nested_context_managers function
async def nested_context_managers():
    """
    Demonstrate nested async context managers.
    """
    print("=== Nested Context Managers Demo ===")

    # Create a temporary file for testing
    test_file = "temp_nested_test.txt"

    try:
        async with AsyncTimer() as outer_timer:
            print("Outer timer started")

            async with AsyncFileHandler(test_file, 'w') as file_handler:
                print("File handler opened")

                # Simulate some work
                await asyncio.sleep(0.5)
                await file_handler.write("Hello from nested context managers!")

                async with AsyncDatabaseConnection("postgresql://localhost/test") as db:
                    print("Database connection established")

                    # Simulate database work
                    await asyncio.sleep(0.3)
                    result = await db.execute_query("SELECT * FROM users")
                    print(f"Query result: {result}")

                    # More file operations
                    await file_handler.write(f"\nDatabase result: {result}")

                print("Database connection closed (inner context)")

            print("File handler closed (middle context)")

        print(".2f")

    except Exception as e:
        print(f"Error in nested contexts: {e}")
    finally:
        # Cleanup
        import os
        if os.path.exists(test_file):
            os.remove(test_file)
            print(f"Cleaned up temporary file: {test_file}")


# TODO: Implement ResourcePool class
class ResourcePool:
    """
    A pool of resources managed with async context managers.
    """

    def __init__(self, max_resources: int = 5):
        self.max_resources = max_resources
        self.available_resources = max_resources
        self.resources_in_use = 0
        self._lock = asyncio.Lock()

    @asynccontextmanager
    async def acquire_resource(self):
        """
        Acquire a resource from the pool.
        """
        async with self._lock:
            if self.available_resources == 0:
                raise RuntimeError("No resources available")

            self.available_resources -= 1
            self.resources_in_use += 1
            resource_id = self.resources_in_use

        print(f"Acquired resource {resource_id}")

        try:
            yield f"Resource-{resource_id}"
        finally:
            async with self._lock:
                self.available_resources += 1
                self.resources_in_use -= 1
                print(f"Released resource {resource_id}")

    async def get_stats(self) -> dict:
        """Get pool statistics"""
        async with self._lock:
            return {
                "max_resources": self.max_resources,
                "available": self.available_resources,
                "in_use": self.resources_in_use
            }


# TODO: Implement resource_pool_demo function
async def resource_pool_demo():
    """
    Demonstrate resource pool usage.
    """
    print("=== Resource Pool Demo ===")

    pool = ResourcePool(max_resources=3)

    async def use_resource(task_id: int):
        """Simulate using a resource"""
        try:
            async with pool.acquire_resource() as resource:
                print(f"Task {task_id} using {resource}")
                await asyncio.sleep(random.uniform(0.5, 1.5))
                print(f"Task {task_id} finished using {resource}")
        except RuntimeError as e:
            print(f"Task {task_id} failed to acquire resource: {e}")

    # Test resource pool with multiple concurrent tasks
    tasks = [use_resource(i) for i in range(6)]  # More tasks than resources

    print("Starting resource pool test...")
    await asyncio.gather(*tasks)

    # Check final stats
    stats = await pool.get_stats()
    print(f"Final pool stats: {stats}")


# TODO: Implement comprehensive_demo function
async def comprehensive_demo():
    """
    Comprehensive demonstration of all async context managers.
    """
    print("=== Comprehensive Async Context Managers Demo ===")

    # Demo 1: Basic file operations
    print("\n1. Basic File Operations:")
    test_file = "comprehensive_test.txt"

    try:
        async with AsyncFileHandler(test_file, 'w') as handler:
            await handler.write("Hello, async context managers!")
            print("File written successfully")
    except Exception as e:
        print(f"File operation failed: {e}")

    # Demo 2: Database operations
    print("\n2. Database Operations:")
    async with AsyncDatabaseConnection("sqlite:///test.db") as db:
        result = await db.execute_query("SELECT COUNT(*) FROM users")
        print(f"Database query result: {result}")

    # Demo 3: Timing operations
    print("\n3. Timing Operations:")
    async with AsyncTimer() as timer:
        await asyncio.sleep(1.0)
        print("Slept for 1 second")
    print(".2f")

    # Demo 4: Resource pool
    print("\n4. Resource Pool:")
    await resource_pool_demo()

    # Demo 5: Nested operations
    print("\n5. Nested Operations:")
    await nested_context_managers()

    print("\n=== Comprehensive Demo Complete ===")


if __name__ == "__main__":
    import random
    asyncio.run(comprehensive_demo())
