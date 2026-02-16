"""
Concurrent Execution Demo
=========================

Demonstrates running multiple async operations concurrently using asyncio.
"""

import asyncio
import time
import random

async def fetch_url(url: str, delay: float = None):
    """Simulate fetching a URL with network delay."""
    if delay is None:
        delay = random.uniform(0.1, 1.0)  # Random delay between 0.1-1.0 seconds

    print(f"Fetching {url}...")
    await asyncio.sleep(delay)
    response_size = random.randint(100, 10000)
    print(f"Completed {url} ({response_size} bytes)")
    return {"url": url, "size": response_size, "delay": delay}

async def process_image(image_id: int, size_mb: float):
    """Simulate processing an image."""
    print(f"Processing image {image_id} ({size_mb:.1f} MB)...")
    # Processing time depends on image size
    processing_time = size_mb * 0.2 + random.uniform(0.1, 0.5)
    await asyncio.sleep(processing_time)
    print(f"Image {image_id} processed")
    return f"Processed image {image_id}"

async def send_email(recipient: str, subject: str):
    """Simulate sending an email."""
    print(f"Sending email to {recipient}: {subject}")
    await asyncio.sleep(random.uniform(0.2, 0.8))  # Email sending delay
    print(f"Email sent to {recipient}")
    return f"Email sent to {recipient}"

async def calculate_fibonacci(n: int):
    """Calculate nth Fibonacci number (CPU-intensive task)."""
    print(f"Calculating Fibonacci({n})...")

    async def fib_async(num):
        # Simulate CPU-bound work by yielding control occasionally
        if num <= 1:
            return num
        await asyncio.sleep(0)  # Yield control to event loop
        return await fib_async(num - 1) + await fib_async(num - 2)

    result = await fib_async(n)
    print(f"Fibonacci({n}) = {result}")
    return result

async def main():
    """Demonstrate concurrent execution patterns."""
    print("=== Concurrent Execution Demo ===\n")

    # 1. Sequential vs Concurrent URL fetching
    print("1. Sequential vs Concurrent URL fetching:")
    urls = [f"https://api.example.com/data/{i}" for i in range(1, 6)]

    # Sequential execution
    print("Sequential execution:")
    start_time = time.time()
    sequential_results = []
    for url in urls:
        result = await fetch_url(url, 0.5)  # Fixed delay for comparison
        sequential_results.append(result)
    sequential_time = time.time() - start_time
    print(".2f")

    # Concurrent execution
    print("\nConcurrent execution:")
    start_time = time.time()
    concurrent_results = await asyncio.gather(
        *[fetch_url(url, 0.5) for url in urls]
    )
    concurrent_time = time.time() - start_time
    print(".2f")
    print(".1f")

    # 2. Mixed concurrent operations
    print("\n2. Mixed concurrent operations:")
    start_time = time.time()

    # Create tasks for different types of operations
    url_tasks = [asyncio.create_task(fetch_url(f"https://api.example.com/v2/{i}", 0.3))
                 for i in range(1, 4)]
    image_tasks = [asyncio.create_task(process_image(i, random.uniform(1, 5)))
                   for i in range(1, 4)]
    email_tasks = [asyncio.create_task(send_email(f"user{i}@example.com", f"Update {i}"))
                   for i in range(1, 4)]

    # Execute all concurrently
    all_results = await asyncio.gather(
        *url_tasks, *image_tasks, *email_tasks
    )
    total_time = time.time() - start_time
    print(".2f")
    print(f"Total operations completed: {len(all_results)}\n")

    # 3. Using asyncio.as_completed for processing results as they complete
    print("3. Processing results as they complete (asyncio.as_completed):")
    start_time = time.time()

    # Create tasks with different completion times
    tasks = [
        asyncio.create_task(fetch_url(f"https://slow-api.com/data/{i}", i * 0.2))
        for i in range(1, 6)
    ]

    print("Results as they complete:")
    completed_count = 0
    for coro in asyncio.as_completed(tasks):
        result = await coro
        completed_count += 1
        print(f"  {completed_count}. {result['url']} completed ({result['delay']:.1f}s)")

    total_time = time.time() - start_time
    print(".2f")

    # 4. Limiting concurrency with semaphore
    print("\n4. Limiting concurrency with asyncio.Semaphore:")
    semaphore = asyncio.Semaphore(3)  # Allow only 3 concurrent operations

    async def limited_fetch(url: str):
        async with semaphore:
            print(f"Acquired semaphore for {url}")
            result = await fetch_url(url, 0.5)
            print(f"Released semaphore for {url}")
            return result

    urls = [f"https://api.example.com/limited/{i}" for i in range(1, 8)]
    start_time = time.time()
    limited_results = await asyncio.gather(
        *[limited_fetch(url) for url in urls]
    )
    limited_time = time.time() - start_time
    print(".2f")

    # 5. Exception handling in concurrent operations
    print("\n5. Exception handling in concurrent operations:")

    async def unreliable_operation(operation_id: int):
        """Operation that sometimes fails."""
        print(f"Starting operation {operation_id}")
        await asyncio.sleep(0.3)

        if random.choice([True, False]):  # 50% chance of failure
            raise Exception(f"Operation {operation_id} failed!")

        print(f"Operation {operation_id} succeeded")
        return f"Success: {operation_id}"

    # Handle exceptions in gather
    print("Using asyncio.gather with exception handling:")
    tasks = [asyncio.create_task(unreliable_operation(i)) for i in range(1, 6)]

    results = []
    exceptions = []
    for task in tasks:
        try:
            result = await task
            results.append(result)
        except Exception as e:
            exceptions.append(str(e))

    print(f"Successful operations: {len(results)}")
    print(f"Failed operations: {len(exceptions)}")
    if exceptions:
        print(f"Exceptions: {exceptions}")

if __name__ == "__main__":
    asyncio.run(main())
