"""
Coroutines and Tasks Demo
==========================

Demonstrates working with coroutines and asyncio tasks.
"""

import asyncio
import time

async def download_file(filename: str, size_mb: float):
    """Simulate downloading a file."""
    print(f"Starting download of {filename} ({size_mb} MB)")
    # Simulate download time based on file size
    download_time = size_mb * 0.1  # 0.1 seconds per MB
    await asyncio.sleep(download_time)
    print(f"Finished downloading {filename}")
    return f"{filename} downloaded successfully"

async def process_data(data_id: int, complexity: float):
    """Simulate processing data."""
    print(f"Processing data {data_id} (complexity: {complexity})")
    processing_time = complexity * 0.2
    await asyncio.sleep(processing_time)
    result = f"Data {data_id} processed"
    print(f"Finished processing data {data_id}")
    return result

async def send_notification(user_id: int, message: str):
    """Simulate sending a notification."""
    print(f"Sending notification to user {user_id}: {message}")
    await asyncio.sleep(0.3)  # Network delay
    print(f"Notification sent to user {user_id}")
    return f"Notification sent to user {user_id}"

async def main():
    """Demonstrate coroutines and tasks."""
    print("=== Coroutines and Tasks Demo ===\n")

    # 1. Creating and awaiting coroutines directly
    print("1. Direct coroutine execution:")
    start_time = time.time()
    result1 = await download_file("document.pdf", 5.0)
    result2 = await download_file("image.jpg", 10.0)
    result3 = await download_file("video.mp4", 50.0)
    end_time = time.time()
    print(f"All downloads completed in {end_time - start_time:.2f} seconds")
    print(f"Results: {result1}, {result2}, {result3}\n")

    # 2. Creating tasks for concurrent execution
    print("2. Using asyncio.create_task() for concurrency:")
    start_time = time.time()

    # Create tasks (this doesn't start them yet)
    task1 = asyncio.create_task(download_file("file1.txt", 2.0))
    task2 = asyncio.create_task(download_file("file2.txt", 3.0))
    task3 = asyncio.create_task(download_file("file3.txt", 1.5))

    # Await all tasks concurrently
    results = await asyncio.gather(task1, task2, task3)
    end_time = time.time()
    print(f"Concurrent downloads completed in {end_time - start_time:.2f} seconds")
    print(f"Results: {results}\n")

    # 3. Mixing tasks and direct awaits
    print("3. Mixing tasks with other async operations:")
    start_time = time.time()

    # Start some downloads as tasks
    download_tasks = [
        asyncio.create_task(download_file(f"batch_{i}.dat", i * 2.0))
        for i in range(1, 4)
    ]

    # Do some processing while downloads are running
    processing_task = asyncio.create_task(process_data(100, 2.0))

    # Wait for all to complete
    all_results = await asyncio.gather(*download_tasks, processing_task)
    end_time = time.time()
    print(f"Mixed operations completed in {end_time - start_time:.2f} seconds")
    print(f"All results: {all_results}\n")

    # 4. Task lifecycle and cancellation
    print("4. Task lifecycle demonstration:")
    async def cancellable_task(task_id: int, duration: float):
        try:
            print(f"Task {task_id} starting...")
            await asyncio.sleep(duration)
            print(f"Task {task_id} completed successfully")
            return f"Task {task_id} result"
        except asyncio.CancelledError:
            print(f"Task {task_id} was cancelled!")
            raise

    # Create a task that will be cancelled
    long_task = asyncio.create_task(cancellable_task(1, 2.0))
    short_task = asyncio.create_task(cancellable_task(2, 0.5))

    # Cancel the long task after 1 second
    await asyncio.sleep(1)
    long_task.cancel()

    # Wait for both tasks
    try:
        long_result = await long_task
    except asyncio.CancelledError:
        long_result = "Task was cancelled"

    short_result = await short_task

    print(f"Long task result: {long_result}")
    print(f"Short task result: {short_result}\n")

    # 5. Task introspection
    print("5. Task introspection:")
    async def monitored_task(name: str):
        print(f"{name}: Starting")
        await asyncio.sleep(0.5)
        print(f"{name}: Working")
        await asyncio.sleep(0.5)
        print(f"{name}: Finishing")
        return f"{name} completed"

    task = asyncio.create_task(monitored_task("Worker"))
    print(f"Task done before await: {task.done()}")
    print(f"Task result before await: {task.result() if task.done() else 'Not done yet'}")

    result = await task
    print(f"Task done after await: {task.done()}")
    print(f"Task result after await: {result}")

if __name__ == "__main__":
    asyncio.run(main())
