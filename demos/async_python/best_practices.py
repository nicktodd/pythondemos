"""
Async Python Best Practices Demo

This module demonstrates best practices for writing efficient, maintainable,
and robust asynchronous Python code. It covers performance optimization,
error handling patterns, resource management, and common pitfalls to avoid.
"""

import asyncio
import time
import logging
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager
import aiohttp
import random

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Best Practice 1: Use async context managers for resource management
@asynccontextmanager
async def managed_session():
    """Properly manage HTTP session resources"""
    session = aiohttp.ClientSession()
    try:
        yield session
    finally:
        await session.close()


# Best Practice 2: Implement proper error handling with retries
async def fetch_with_retry(session: aiohttp.ClientSession, url: str,
                          max_retries: int = 3, delay: float = 1.0) -> Optional[str]:
    """Fetch URL with exponential backoff retry logic"""
    for attempt in range(max_retries):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                response.raise_for_status()
                return await response.text()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            if attempt == max_retries - 1:
                logger.error(f"Failed to fetch {url} after {max_retries} attempts: {e}")
                return None

            wait_time = delay * (2 ** attempt) + random.uniform(0, 0.1)
            logger.warning(f"Attempt {attempt + 1} failed for {url}, retrying in {wait_time:.2f}s: {e}")
            await asyncio.sleep(wait_time)

    return None


# Best Practice 3: Use asyncio.gather with exception handling
async def gather_with_exception_handling(*coroutines):
    """Gather results while handling exceptions individually"""
    results = []
    for coro in asyncio.as_completed(coroutines):
        try:
            result = await coro
            results.append(result)
        except Exception as e:
            logger.error(f"Coroutine failed: {e}")
            results.append(None)  # Or handle differently based on requirements
    return results


# Best Practice 4: Implement proper cancellation handling
async def cancellable_task(name: str, duration: float):
    """Task that can be properly cancelled"""
    try:
        logger.info(f"Starting task {name}")
        await asyncio.sleep(duration)
        logger.info(f"Completed task {name}")
        return f"Task {name} completed"
    except asyncio.CancelledError:
        logger.info(f"Task {name} was cancelled")
        raise  # Re-raise to propagate cancellation


# Best Practice 5: Use asyncio.Semaphore for rate limiting
async def rate_limited_request(semaphore: asyncio.Semaphore, session: aiohttp.ClientSession,
                              url: str, delay: float = 0.1) -> Optional[str]:
    """Make rate-limited HTTP requests"""
    async with semaphore:
        result = await fetch_with_retry(session, url)
        await asyncio.sleep(delay)  # Additional rate limiting
        return result


# Best Practice 6: Avoid blocking operations in async code
async def non_blocking_file_operation():
    """Demonstrate how to handle potentially blocking operations"""
    # Use ThreadPoolExecutor for CPU-bound or blocking operations
    loop = asyncio.get_event_loop()

    # Simulate a blocking operation (e.g., file I/O, CPU-intensive task)
    def blocking_operation():
        time.sleep(0.1)  # This would block the event loop
        return "Blocking operation result"

    # Run in thread pool to avoid blocking
    result = await loop.run_in_executor(None, blocking_operation)
    return result


# Best Practice 7: Use asyncio.Queue for producer-consumer patterns
async def producer(queue: asyncio.Queue, items: List[str], num_consumers: int = 1):
    """Producer that adds items to queue"""
    for item in items:
        await queue.put(item)
        logger.info(f"Produced: {item}")
        await asyncio.sleep(0.1)  # Simulate production time

    # Put sentinel values for each consumer
    for _ in range(num_consumers):
        await queue.put(None)  # Sentinel value to signal end


async def consumer(queue: asyncio.Queue, consumer_id: int):
    """Consumer that processes items from queue"""
    while True:
        item = await queue.get()
        if item is None:  # Sentinel value
            queue.task_done()
            break

        logger.info(f"Consumer {consumer_id} processing: {item}")
        await asyncio.sleep(0.2)  # Simulate processing time
        queue.task_done()


# Best Practice 8: Proper task lifecycle management
async def task_lifecycle_demo():
    """Demonstrate proper task creation, monitoring, and cleanup"""
    async def worker(task_id: int):
        try:
            await asyncio.sleep(random.uniform(0.5, 2.0))
            return f"Task {task_id} completed"
        except asyncio.CancelledError:
            logger.info(f"Task {task_id} cancelled")
            raise

    # Create tasks
    tasks = [asyncio.create_task(worker(i)) for i in range(5)]

    try:
        # Wait for all tasks with timeout
        results = await asyncio.wait_for(asyncio.gather(*tasks, return_exceptions=True), timeout=3.0)
        return results
    except asyncio.TimeoutError:
        logger.warning("Timeout reached, cancelling remaining tasks")
        # Cancel remaining tasks
        for task in tasks:
            if not task.done():
                task.cancel()

        # Wait for cancellation to complete
        await asyncio.gather(*tasks, return_exceptions=True)
        return ["Timeout occurred"]


# Best Practice 9: Use asyncio.Lock for shared resource protection
shared_resource = {"counter": 0}
resource_lock = asyncio.Lock()

async def safe_shared_access(task_id: int):
    """Safely access shared resources"""
    async with resource_lock:
        current = shared_resource["counter"]
        await asyncio.sleep(0.01)  # Simulate some work
        shared_resource["counter"] = current + 1
        logger.info(f"Task {task_id} updated counter to {shared_resource['counter']}")


# Best Practice 10: Proper async generator usage
async def async_data_stream():
    """Async generator for streaming data"""
    for i in range(10):
        yield f"Data chunk {i}"
        await asyncio.sleep(0.1)  # Simulate data generation delay


async def process_stream():
    """Process data from async generator"""
    async for chunk in async_data_stream():
        logger.info(f"Processing: {chunk}")


# Main demonstration function
async def main():
    """Demonstrate all best practices"""
    print("=== Async Python Best Practices Demo ===\n")

    # 1. Resource management with context managers
    print("1. Resource Management with Context Managers:")
    async with managed_session() as session:
        # Simulate fetching data
        print("   Session managed properly")

    # 2. Error handling with retries
    print("\n2. Error Handling with Retries:")
    async with managed_session() as session:
        result = await fetch_with_retry(session, "https://httpbin.org/delay/1")
        print(f"   Fetch result: {result[:50] if result else 'Failed'}...")

    # 3. Exception handling in gather
    print("\n3. Exception Handling in Gather:")
    async def failing_coro():
        await asyncio.sleep(0.1)
        raise ValueError("Simulated failure")

    async def success_coro():
        await asyncio.sleep(0.1)
        return "Success"

    results = await gather_with_exception_handling(failing_coro(), success_coro())
    print(f"   Results: {results}")

    # 4. Cancellation handling
    print("\n4. Cancellation Handling:")
    task = asyncio.create_task(cancellable_task("demo", 2.0))

    # Cancel after 0.5 seconds
    await asyncio.sleep(0.5)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("   Task was properly cancelled")

    # 5. Rate limiting
    print("\n5. Rate Limiting:")
    semaphore = asyncio.Semaphore(2)  # Max 2 concurrent requests
    async with managed_session() as session:
        tasks = [
            rate_limited_request(semaphore, session, f"https://httpbin.org/delay/{i}")
            for i in range(1, 4)
        ]
        results = await asyncio.gather(*tasks)
        print(f"   Rate limited requests completed: {len([r for r in results if r])}")

    # 6. Non-blocking operations
    print("\n6. Non-blocking Operations:")
    result = await non_blocking_file_operation()
    print(f"   Non-blocking result: {result}")

    # 7. Producer-consumer pattern
    print("\n7. Producer-Consumer Pattern:")
    queue = asyncio.Queue()
    consumer_tasks = [asyncio.create_task(consumer(queue, i)) for i in range(2)]
    producer_task = asyncio.create_task(producer(queue, ["item1", "item2", "item3"], len(consumer_tasks)))

    await asyncio.gather(producer_task, *consumer_tasks)
    print("   Producer-consumer pattern completed")

    # 8. Task lifecycle management
    print("\n8. Task Lifecycle Management:")
    results = await task_lifecycle_demo()
    print(f"   Task results: {results}")

    # 9. Shared resource protection
    print("\n9. Shared Resource Protection:")
    await asyncio.gather(*[safe_shared_access(i) for i in range(5)])
    print(f"   Final counter value: {shared_resource['counter']}")

    # 10. Async generators
    print("\n10. Async Generators:")
    await process_stream()
    print("   Async stream processing completed")

    print("\n=== Best Practices Demo Complete ===")


if __name__ == "__main__":
    # Run the demo
    asyncio.run(main())
