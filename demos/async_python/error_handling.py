"""
Error Handling in Async Python Demo
===================================

Demonstrates various error handling patterns in asynchronous Python code.
"""

import asyncio
import random
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class NetworkError(Exception):
    """Custom exception for network-related errors."""
    pass

class TimeoutError(Exception):
    """Custom exception for timeout errors."""
    pass

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

async def unreliable_network_call(url: str, success_rate: float = 0.8) -> str:
    """Simulate a network call that can fail."""
    await asyncio.sleep(random.uniform(0.1, 0.5))

    if random.random() > success_rate:
        if random.choice([True, False]):
            raise NetworkError(f"Connection failed to {url}")
        else:
            raise TimeoutError(f"Timeout connecting to {url}")

    return f"Response from {url}"

async def validate_data(data: str) -> str:
    """Validate data and raise exception if invalid."""
    await asyncio.sleep(0.1)

    if not data or len(data.strip()) == 0:
        raise ValidationError("Data cannot be empty")

    if len(data) > 100:
        raise ValidationError("Data too long (max 100 characters)")

    return f"Validated: {data}"

async def process_with_retry(func, *args, max_retries: int = 3, delay: float = 0.5, **kwargs):
    """Execute a function with retry logic."""
    last_exception = None

    for attempt in range(max_retries):
        try:
            return await func(*args, **kwargs)
        except (NetworkError, TimeoutError) as e:
            last_exception = e
            wait_time = delay * (2 ** attempt)  # Exponential backoff
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.1f}s...")
            await asyncio.sleep(wait_time)
        except Exception as e:
            # Don't retry for other types of exceptions
            logger.error(f"Non-retryable error: {e}")
            raise

    logger.error(f"All {max_retries} attempts failed")
    raise last_exception

async def fetch_multiple_urls(urls: List[str]) -> List[str]:
    """Fetch multiple URLs, handling errors gracefully."""
    tasks = []

    for url in urls:
        # Create task for each URL with retry logic
        task = asyncio.create_task(
            process_with_retry(unreliable_network_call, url, success_rate=0.7)
        )
        tasks.append(task)

    # Wait for all tasks to complete, gathering results and exceptions
    results = []
    exceptions = []

    for coro in asyncio.as_completed(tasks):
        try:
            result = await coro
            results.append(result)
        except Exception as e:
            exceptions.append(e)
            logger.error(f"Failed to fetch URL: {e}")

    logger.info(f"Successfully fetched {len(results)} URLs, {len(exceptions)} failed")
    return results

async def process_user_data(user_data: dict) -> dict:
    """Process user data with comprehensive error handling."""
    try:
        # Validate required fields
        required_fields = ['name', 'email', 'age']
        for field in required_fields:
            if field not in user_data:
                raise ValidationError(f"Missing required field: {field}")

        # Validate and process each field
        name = await validate_data(user_data['name'])
        email = await validate_data(user_data['email'])

        # Validate age
        try:
            age = int(user_data['age'])
            if age < 0 or age > 150:
                raise ValidationError("Age must be between 0 and 150")
        except (ValueError, TypeError):
            raise ValidationError("Age must be a valid integer")

        # Simulate additional processing that might fail
        await asyncio.sleep(0.2)
        if random.random() < 0.1:  # 10% chance of processing error
            raise Exception("Processing failed due to internal error")

        return {
            'processed_name': name,
            'processed_email': email,
            'processed_age': age,
            'status': 'success'
        }

    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        return {'status': 'validation_error', 'error': str(e)}
    except Exception as e:
        logger.error(f"Processing error: {e}")
        return {'status': 'processing_error', 'error': str(e)}

async def demo_exception_chaining():
    """Demonstrate exception chaining in async code."""
    async def inner_operation():
        await asyncio.sleep(0.1)
        raise ValueError("Inner operation failed")

    async def middle_operation():
        try:
            return await inner_operation()
        except ValueError as e:
            raise RuntimeError("Middle operation failed") from e

    async def outer_operation():
        try:
            return await middle_operation()
        except RuntimeError as e:
            raise Exception("Outer operation failed") from e

    try:
        await outer_operation()
    except Exception as e:
        logger.error(f"Final exception: {e}")
        logger.error(f"Chain: {e.__cause__}")
        if e.__cause__ and e.__cause__.__cause__:
            logger.error(f"Root cause: {e.__cause__.__cause__}")

async def demo_async_context_manager_with_errors():
    """Demonstrate error handling in async context managers."""

    class AsyncResource:
        def __init__(self, name: str):
            self.name = name
            self.acquired = False

        async def __aenter__(self):
            print(f"Acquiring resource: {self.name}")
            await asyncio.sleep(0.1)
            self.acquired = True
            print(f"Resource {self.name} acquired")
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print(f"Releasing resource: {self.name}")
            await asyncio.sleep(0.05)
            self.acquired = False
            print(f"Resource {self.name} released")
            # Return False to propagate exceptions
            return False

        async def use_resource(self):
            if not self.acquired:
                raise RuntimeError("Resource not acquired")
            await asyncio.sleep(0.2)
            if random.random() < 0.3:  # 30% chance of failure
                raise Exception(f"Resource {self.name} operation failed")
            return f"Resource {self.name} operation successful"

    # Test successful operation
    print("Testing successful resource usage:")
    async with AsyncResource("Resource1") as res:
        result = await res.use_resource()
        print(f"Result: {result}")

    # Test failed operation
    print("\nTesting failed resource usage:")
    try:
        async with AsyncResource("Resource2") as res:
            result = await res.use_resource()
            print(f"Result: {result}")
    except Exception as e:
        print(f"Operation failed: {e}")
        print("Resource was still properly released due to context manager")

async def demo_cancellation():
    """Demonstrate task cancellation and cleanup."""
    async def cancellable_task(task_id: int, duration: float):
        try:
            print(f"Task {task_id} starting ({duration}s)")
            await asyncio.sleep(duration)
            print(f"Task {task_id} completed successfully")
            return f"Task {task_id} result"
        except asyncio.CancelledError:
            print(f"Task {task_id} was cancelled, performing cleanup...")
            # Simulate cleanup
            await asyncio.sleep(0.1)
            print(f"Task {task_id} cleanup completed")
            raise  # Re-raise the cancellation

    async def supervisor():
        # Start multiple tasks
        tasks = [
            asyncio.create_task(cancellable_task(i, random.uniform(1, 3)))
            for i in range(1, 4)
        ]

        # Wait a bit then cancel some tasks
        await asyncio.sleep(0.5)

        # Cancel the first task
        tasks[0].cancel()

        # Wait a bit more then cancel another
        await asyncio.sleep(0.3)
        tasks[1].cancel()

        # Wait for all tasks
        results = []
        for i, task in enumerate(tasks):
            try:
                result = await task
                results.append(result)
            except asyncio.CancelledError:
                results.append(f"Task {i+1} was cancelled")

        return results

    results = await supervisor()
    print("Supervisor results:", results)

async def main():
    """Main demo function."""
    print("=== Error Handling in Async Python Demo ===\n")

    # 1. Basic exception handling
    print("1. Basic exception handling:")
    try:
        result = await unreliable_network_call("https://api.example.com", success_rate=0.5)
        print(f"Success: {result}")
    except (NetworkError, TimeoutError) as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    print()

    # 2. Retry logic
    print("2. Retry logic with exponential backoff:")
    try:
        result = await process_with_retry(
            unreliable_network_call,
            "https://unreliable-api.com",
            success_rate=0.3  # Low success rate to trigger retries
        )
        print(f"Final success: {result}")
    except Exception as e:
        print(f"All retries failed: {e}")
    print()

    # 3. Handling multiple concurrent errors
    print("3. Handling multiple concurrent operations:")
    urls = [f"https://api{i}.example.com" for i in range(1, 6)]
    results = await fetch_multiple_urls(urls)
    print(f"Successful fetches: {results}")
    print()

    # 4. Comprehensive error handling in data processing
    print("4. Comprehensive error handling in data processing:")
    test_data = [
        {"name": "Alice", "email": "alice@example.com", "age": "25"},
        {"name": "", "email": "bob@example.com", "age": "30"},  # Invalid name
        {"name": "Charlie", "email": "charlie@example.com", "age": "invalid"},  # Invalid age
        {"name": "David", "email": "david@example.com"}  # Missing age
    ]

    for i, data in enumerate(test_data, 1):
        print(f"Processing user {i}:")
        result = await process_user_data(data)
        print(f"Result: {result}")
        print()

    # 5. Exception chaining
    print("5. Exception chaining:")
    await demo_exception_chaining()
    print()

    # 6. Async context managers with errors
    print("6. Async context managers with error handling:")
    try:
        await demo_async_context_manager_with_errors()
    except Exception as e:
        print(f"Demo error (expected): {e}")
    print()

    # 7. Task cancellation
    print("7. Task cancellation and cleanup:")
    await demo_cancellation()

if __name__ == "__main__":
    asyncio.run(main())
