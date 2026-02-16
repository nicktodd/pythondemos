"""
Async Python Lab - Exercise 6: Error Handling

Implement comprehensive error handling in async code.
Complete the TODO sections with your implementations.
"""

import asyncio
import time
import random
import logging
from typing import List, Any, Callable, TypeVar, Awaitable
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

T = TypeVar('T')


# TODO: Implement retry_async decorator
def retry_async(max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    Decorator that retries an async function on failure.

    Args:
        max_retries: Maximum number of retry attempts
        delay: Initial delay between retries
        backoff: Backoff multiplier for delay
    """
    def decorator(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            current_delay = delay
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e

                    if attempt < max_retries:
                        logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {e}. "
                                     f"Retrying in {current_delay:.2f}s...")
                        await asyncio.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(f"All {max_retries + 1} attempts failed for {func.__name__}: {e}")

            raise last_exception

        return wrapper
    return decorator


# TODO: Implement safe_gather function
async def safe_gather(*coroutines: Awaitable[Any]) -> List[Any]:
    """
    Gather multiple coroutines but handle exceptions individually.

    Args:
        *coroutines: Variable number of awaitable coroutines

    Returns:
        List of results, with exceptions where coroutines failed
    """
    results = []

    for coro in asyncio.as_completed(coroutines):
        try:
            result = await coro
            results.append(result)
        except Exception as e:
            logger.error(f"Coroutine failed: {e}")
            results.append(e)  # Store the exception

    return results


# TODO: Implement timeout_demo function
async def timeout_demo():
    """
    Demonstrate timeout handling with asyncio.wait_for and asyncio.shield.
    """
    print("=== Timeout Demo ===")

    # Function that may take too long
    async def slow_operation(name: str, duration: float) -> str:
        print(f"Starting {name}...")
        await asyncio.sleep(duration)
        return f"{name} completed successfully"

    # Test with wait_for
    print("\n1. Using asyncio.wait_for:")
    try:
        result = await asyncio.wait_for(slow_operation("Quick Task", 1.0), timeout=2.0)
        print(f"Success: {result}")
    except asyncio.TimeoutError:
        print("Task timed out!")

    try:
        result = await asyncio.wait_for(slow_operation("Slow Task", 3.0), timeout=1.0)
        print(f"Success: {result}")
    except asyncio.TimeoutError:
        print("Task timed out as expected!")

    # Test with shield
    print("\n2. Using asyncio.shield:")
    async def cancellable_task():
        try:
            await asyncio.sleep(2.0)
            return "Task completed"
        except asyncio.CancelledError:
            print("Task was cancelled but shielded!")
            # Do some cleanup
            await asyncio.sleep(0.5)
            print("Cleanup completed")
            raise

    try:
        # Start a task and shield it
        task = asyncio.create_task(cancellable_task())
        shielded_task = asyncio.shield(task)

        # Try to cancel after 1 second
        await asyncio.sleep(1.0)
        task.cancel()

        result = await shielded_task
        print(f"Shielded task result: {result}")

    except asyncio.CancelledError:
        print("Shielded task was cancelled")


# TODO: Implement cancellation_demo function
async def cancellation_demo():
    """
    Demonstrate proper cancellation handling for long-running tasks.
    """
    print("=== Cancellation Demo ===")

    async def long_running_task(task_id: int, duration: float) -> str:
        try:
            print(f"Task {task_id} starting ({duration}s)...")
            await asyncio.sleep(duration)
            print(f"Task {task_id} completed normally")
            return f"Task {task_id} result"
        except asyncio.CancelledError:
            print(f"Task {task_id} was cancelled - cleaning up...")
            # Simulate cleanup work
            await asyncio.sleep(0.2)
            print(f"Task {task_id} cleanup complete")
            raise  # Re-raise to propagate cancellation

    # Test cancellation
    print("\n1. Testing task cancellation:")
    task = asyncio.create_task(long_running_task(1, 3.0))

    # Cancel after 1 second
    await asyncio.sleep(1.0)
    print("Cancelling task...")
    task.cancel()

    try:
        result = await task
        print(f"Task result: {result}")
    except asyncio.CancelledError:
        print("Task was properly cancelled")

    # Test multiple tasks with cancellation
    print("\n2. Testing multiple tasks with cancellation:")
    tasks = [asyncio.create_task(long_running_task(i, random.uniform(1.0, 3.0)))
             for i in range(1, 4)]

    # Cancel all after 1.5 seconds
    await asyncio.sleep(1.5)
    print("Cancelling all tasks...")
    for task in tasks:
        if not task.done():
            task.cancel()

    # Wait for all to complete/cancel
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"All tasks finished: {len(results)} total")


# TODO: Implement structured_error_logging function
async def structured_error_logging():
    """
    Demonstrate structured error logging in async operations.
    """
    print("=== Structured Error Logging Demo ===")

    # Create a custom logger with more detailed formatting
    error_logger = logging.getLogger('async_errors')
    error_logger.setLevel(logging.ERROR)

    # Add a file handler for error logging
    handler = logging.FileHandler('async_errors.log')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    ))
    error_logger.addHandler(handler)

    async def operation_with_logging(name: str, should_fail: bool = False) -> str:
        try:
            logger.info(f"Starting operation: {name}")
            await asyncio.sleep(0.5)

            if should_fail:
                raise ValueError(f"Simulated error in {name}")

            logger.info(f"Operation {name} completed successfully")
            return f"Success: {name}"

        except Exception as e:
            # Log structured error information
            error_info = {
                "operation": name,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "timestamp": time.time()
            }

            error_logger.error(f"Operation failed: {error_info}")
            logger.error(f"Operation {name} failed: {e}")
            raise

    # Test successful operations
    print("\n1. Testing successful operations:")
    results = await safe_gather(
        operation_with_logging("op1"),
        operation_with_logging("op2"),
        operation_with_logging("op3")
    )
    print(f"Results: {results}")

    # Test operations with errors
    print("\n2. Testing operations with errors:")
    results = await safe_gather(
        operation_with_logging("good_op"),
        operation_with_logging("bad_op", should_fail=True),
        operation_with_logging("another_good_op")
    )
    print(f"Results (with errors): {results}")

    print("Check 'async_errors.log' for detailed error logs")


# TODO: Implement comprehensive_error_handling_demo function
async def comprehensive_error_handling_demo():
    """
    Run all error handling demonstrations.
    """
    print("=== Comprehensive Error Handling Demo ===")

    # Demo 1: Retry decorator
    print("\n1. Retry Decorator Demo:")
    @retry_async(max_retries=2, delay=0.5)
    async def unreliable_operation():
        if random.random() < 0.7:  # 70% failure rate
            raise ConnectionError("Network temporarily unavailable")
        return "Operation succeeded!"

    try:
        result = await unreliable_operation()
        print(f"Retry demo result: {result}")
    except Exception as e:
        print(f"Retry demo failed after all attempts: {e}")

    # Demo 2: Safe gather
    print("\n2. Safe Gather Demo:")
    async def sometimes_fails(name: str):
        await asyncio.sleep(0.3)
        if random.random() < 0.5:
            raise RuntimeError(f"Random failure in {name}")
        return f"Success from {name}"

    results = await safe_gather(
        sometimes_fails("task1"),
        sometimes_fails("task2"),
        sometimes_fails("task3"),
        sometimes_fails("task4")
    )
    print(f"Safe gather results: {results}")

    # Demo 3: Timeout handling
    await timeout_demo()

    # Demo 4: Cancellation handling
    await cancellation_demo()

    # Demo 5: Structured logging
    await structured_error_logging()

    print("\n=== Comprehensive Error Handling Demo Complete ===")


if __name__ == "__main__":
    asyncio.run(comprehensive_error_handling_demo())
