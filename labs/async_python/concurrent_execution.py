"""
Async Python Lab - Exercise 3: Concurrent Execution

Implement concurrent execution patterns using asyncio.gather, as_completed, and semaphores.
Complete the TODO sections with your implementations.
"""

import asyncio
import time
import random
from typing import List, Any, Coroutine


# TODO: Implement simulate_work function
async def simulate_work(name: str, duration: float) -> str:
    """
    Simulate different types of work (CPU-bound, I/O-bound, etc.)

    Args:
        name: Name of the work item
        duration: How long the work should take

    Returns:
        Completion message with timing info
    """
    start_time = time.time()
    print(f"Starting {name}...")

    # Simulate work with some randomness
    actual_duration = duration * (0.8 + random.random() * 0.4)  # ±20% variation
    await asyncio.sleep(actual_duration)

    elapsed = time.time() - start_time
    result = f"{name} completed in {elapsed:.2f}s"
    print(result)

    return result


# TODO: Implement run_sequential function
async def run_sequential(tasks: List[Coroutine]) -> List[Any]:
    """
    Run tasks sequentially (one after another).

    Args:
        tasks: List of coroutines to run

    Returns:
        List of results in completion order
    """
    results = []

    for task in tasks:
        result = await task
        results.append(result)

    return results


# TODO: Implement run_concurrent_gather function
async def run_concurrent_gather(tasks: List[Coroutine]) -> List[Any]:
    """
    Run tasks concurrently using asyncio.gather.

    Args:
        tasks: List of coroutines to run

    Returns:
        List of results in the order tasks were provided
    """
    # Use asyncio.gather to run all tasks concurrently
    results = await asyncio.gather(*tasks)

    return list(results)


# TODO: Implement run_concurrent_as_completed function
async def run_concurrent_as_completed(tasks: List[Coroutine]) -> List[Any]:
    """
    Run tasks concurrently using asyncio.as_completed.

    Args:
        tasks: List of coroutines to run

    Returns:
        List of results in completion order (not input order)
    """
    results = []

    # Use asyncio.as_completed to get results as they complete
    for coro in asyncio.as_completed(tasks):
        result = await coro
        results.append(result)
        print(f"Got result: {result[:30]}...")

    return results


# TODO: Implement rate_limited_tasks function
async def rate_limited_tasks(tasks: List[Coroutine], max_concurrent: int) -> List[Any]:
    """
    Run tasks with a concurrency limit using semaphore.

    Args:
        tasks: List of coroutines to run
        max_concurrent: Maximum number of concurrent tasks

    Returns:
        List of results
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    results = []

    async def run_with_semaphore(coro):
        async with semaphore:
            return await coro

    # Create semaphore-wrapped tasks
    semaphore_tasks = [run_with_semaphore(task) for task in tasks]

    # Run all semaphore tasks concurrently
    results = await asyncio.gather(*semaphore_tasks)

    return list(results)


# TODO: Implement performance_comparison function
async def performance_comparison():
    """
    Compare performance of different execution strategies.
    """
    print("=== Performance Comparison ===")

    # Create test tasks
    task_count = 10
    tasks = [simulate_work(f"Task-{i+1}", random.uniform(0.5, 1.5)) for i in range(task_count)]

    # Test sequential execution
    print(f"\n1. Sequential execution ({task_count} tasks):")
    start_time = time.time()
    results = await run_sequential(tasks.copy())
    sequential_time = time.time() - start_time
    print(".2f")

    # Test concurrent with gather
    print(f"\n2. Concurrent execution with gather ({task_count} tasks):")
    start_time = time.time()
    results = await run_concurrent_gather(tasks.copy())
    gather_time = time.time() - start_time
    print(".2f")

    # Test concurrent with as_completed
    print(f"\n3. Concurrent execution with as_completed ({task_count} tasks):")
    start_time = time.time()
    results = await run_concurrent_as_completed(tasks.copy())
    as_completed_time = time.time() - start_time
    print(".2f")

    # Test rate limiting
    print(f"\n4. Rate limited execution (max 3 concurrent, {task_count} tasks):")
    start_time = time.time()
    results = await rate_limited_tasks(tasks.copy(), 3)
    rate_limited_time = time.time() - start_time
    print(".2f")

    # Calculate speedups
    print("=== Speedup Analysis ===")
    print(".2f")
    print(".2f")
    print(".2f")

    return {
        "sequential": sequential_time,
        "gather": gather_time,
        "as_completed": as_completed_time,
        "rate_limited": rate_limited_time
    }


# TODO: Implement error_handling_demo function
async def error_handling_demo():
    """
    Demonstrate error handling in concurrent execution.
    """
    print("=== Error Handling Demo ===")

    # Create tasks - some will succeed, some will fail
    async def sometimes_failing_task(name: str) -> str:
        await asyncio.sleep(0.5)
        if random.random() < 0.3:  # 30% failure rate
            raise ValueError(f"Task {name} failed randomly")
        return f"Task {name} succeeded"

    tasks = [sometimes_failing_task(f"Task-{i+1}") for i in range(8)]

    # Test with gather and exception handling
    print("\n1. Using gather with return_exceptions=True:")
    try:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        successes = sum(1 for r in results if not isinstance(r, Exception))
        failures = sum(1 for r in results if isinstance(r, Exception))
        print(f"Results: {successes} successes, {failures} failures")

        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"  Task {i+1} failed: {result}")
            else:
                print(f"  Task {i+1}: {result}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    # Test with as_completed and individual exception handling
    print("\n2. Using as_completed with individual error handling:")
    tasks = [sometimes_failing_task(f"Task-{i+1}") for i in range(8)]
    successes = 0
    failures = 0

    for coro in asyncio.as_completed(tasks):
        try:
            result = await coro
            print(f"Success: {result}")
            successes += 1
        except Exception as e:
            print(f"Failure: {e}")
            failures += 1

    print(f"Final count: {successes} successes, {failures} failures")


if __name__ == "__main__":
    # Run the demos
    asyncio.run(performance_comparison())
    asyncio.run(error_handling_demo())
