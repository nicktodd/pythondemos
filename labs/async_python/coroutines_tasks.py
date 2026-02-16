"""
Async Python Lab - Exercise 2: Coroutines and Tasks

Implement coroutine and task management patterns.
Complete the TODO sections with your implementations.
"""

import asyncio
import time
from typing import List


# TODO: Implement background_worker function
async def background_worker(name: str, duration: float) -> str:
    """
    A background worker coroutine that simulates some work.

    Args:
        name: Name of the worker
        duration: How long the work should take

    Returns:
        Completion message
    """
    print(f"Worker {name} starting...")
    start_time = time.time()

    # Simulate work
    await asyncio.sleep(duration)

    elapsed = time.time() - start_time
    result = f"Worker {name} completed in {elapsed:.2f} seconds"
    print(result)

    return result


# TODO: Implement create_multiple_tasks function
def create_multiple_tasks(count: int) -> List[asyncio.Task]:
    """
    Create multiple background worker tasks.

    Args:
        count: Number of tasks to create

    Returns:
        List of created tasks
    """
    tasks = []

    for i in range(count):
        # Create task with random duration
        duration = 0.5 + (i * 0.3)  # Increasing duration
        task = asyncio.create_task(background_worker(f"Task-{i+1}", duration))
        tasks.append(task)

    return tasks


# TODO: Implement monitor_tasks function
async def monitor_tasks(tasks: List[asyncio.Task]):
    """
    Monitor the progress of multiple tasks.

    Args:
        tasks: List of tasks to monitor
    """
    print(f"\nMonitoring {len(tasks)} tasks...")

    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks, return_exceptions=True)

    print(f"\nAll tasks completed. Results: {len(results)}")

    # Report results
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i+1} failed: {result}")
        else:
            print(f"Task {i+1}: {result}")


# TODO: Implement cancel_tasks_after_timeout function
async def cancel_tasks_after_timeout(tasks: List[asyncio.Task], timeout: float):
    """
    Run tasks with a timeout and cancel any that don't complete in time.

    Args:
        tasks: List of tasks to run
        timeout: Timeout in seconds
    """
    print(f"\nRunning {len(tasks)} tasks with {timeout}s timeout...")

    try:
        # Wait for all tasks with timeout
        results = await asyncio.wait_for(asyncio.gather(*tasks, return_exceptions=True), timeout=timeout)

        print(f"All tasks completed within timeout. Results: {len(results)}")

    except asyncio.TimeoutError:
        print(f"Timeout ({timeout}s) reached! Cancelling remaining tasks...")

        # Cancel any tasks that are still running
        cancelled_count = 0
        for task in tasks:
            if not task.done():
                task.cancel()
                cancelled_count += 1

        print(f"Cancelled {cancelled_count} tasks")

        # Wait for cancellation to complete
        await asyncio.gather(*tasks, return_exceptions=True)


# TODO: Implement task_lifecycle_demo function
async def task_lifecycle_demo():
    """
    Demonstrate proper task lifecycle management including creation, monitoring, and cleanup.
    """
    print("=== Task Lifecycle Demo ===")

    # Phase 1: Create tasks
    print("\n1. Creating tasks...")
    tasks = create_multiple_tasks(3)

    # Phase 2: Monitor tasks
    print("\n2. Monitoring tasks...")
    await monitor_tasks(tasks)

    # Phase 3: Test cancellation
    print("\n3. Testing cancellation...")
    tasks = create_multiple_tasks(5)
    await cancel_tasks_after_timeout(tasks, 1.0)

    # Phase 4: Proper cleanup
    print("\n4. Ensuring all tasks are properly cleaned up...")
    # All tasks should be done by now, but let's verify
    pending_tasks = [task for task in tasks if not task.done()]
    if pending_tasks:
        print(f"Warning: {len(pending_tasks)} tasks still pending")
        await asyncio.gather(*pending_tasks, return_exceptions=True)
    else:
        print("All tasks properly completed")

    print("\n=== Task Lifecycle Demo Complete ===")


# TODO: Implement concurrent_vs_sequential function
async def concurrent_vs_sequential():
    """
    Demonstrate the difference between concurrent and sequential task execution.
    """
    print("=== Concurrent vs Sequential Demo ===")

    task_count = 5
    durations = [1.0, 0.8, 1.2, 0.6, 1.5]

    # Sequential execution
    print("\n1. Sequential execution:")
    start_time = time.time()

    results = []
    for i, duration in enumerate(durations):
        result = await background_worker(f"Seq-{i+1}", duration)
        results.append(result)

    sequential_time = time.time() - start_time
    print(".2f")

    # Concurrent execution
    print("\n2. Concurrent execution:")
    start_time = time.time()

    tasks = [background_worker(f"Conc-{i+1}", duration) for i, duration in enumerate(durations)]
    results = await asyncio.gather(*tasks)

    concurrent_time = time.time() - start_time
    print(".2f")

    # Calculate speedup
    speedup = sequential_time / concurrent_time
    print(".2f")

    return {
        "sequential_time": sequential_time,
        "concurrent_time": concurrent_time,
        "speedup": speedup
    }


if __name__ == "__main__":
    # Run the demos
    asyncio.run(task_lifecycle_demo())
    asyncio.run(concurrent_vs_sequential())
