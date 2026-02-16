"""
Basic Async/Await Demo
======================

Demonstrates the fundamental async/await syntax in Python.
"""

import asyncio
import time

async def simple_coroutine():
    """A simple coroutine that demonstrates async/await syntax."""
    print("Coroutine started")
    await asyncio.sleep(1)  # Simulate async operation
    print("Coroutine finished")
    return "Hello from coroutine!"

async def greet_after_delay(name: str, delay: float):
    """Greets someone after a delay."""
    print(f"Starting greeting for {name}")
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")
    return f"Greeted {name}"

async def calculate_square(number: int):
    """Calculates square of a number with simulated delay."""
    print(f"Calculating square of {number}")
    await asyncio.sleep(0.5)  # Simulate computation time
    result = number ** 2
    print(f"Square of {number} is {result}")
    return result

async def main():
    """Main coroutine that demonstrates various async patterns."""
    print("=== Basic Async/Await Demo ===\n")

    # 1. Simple coroutine execution
    print("1. Simple coroutine:")
    result = await simple_coroutine()
    print(f"Result: {result}\n")

    # 2. Multiple coroutines with different delays
    print("2. Multiple greetings with delays:")
    await greet_after_delay("Alice", 0.5)
    await greet_after_delay("Bob", 0.3)
    await greet_after_delay("Charlie", 0.1)
    print()

    # 3. Sequential execution (awaiting each one)
    print("3. Sequential calculations:")
    start_time = time.time()
    result1 = await calculate_square(3)
    result2 = await calculate_square(4)
    result3 = await calculate_square(5)
    end_time = time.time()
    print(f"Sequential total time: {end_time - start_time:.2f} seconds")
    print(f"Results: {result1}, {result2}, {result3}\n")

    # 4. Demonstrate that async functions return coroutines
    print("4. Coroutine objects:")
    coro1 = simple_coroutine()
    coro2 = greet_after_delay("Dave", 0.2)
    print(f"coro1 type: {type(coro1)}")
    print(f"coro2 type: {type(coro2)}")
    print("These are coroutine objects, not the actual results!")
    print("To get results, we need to await them.\n")

    # 5. Show the difference between sync and async
    print("5. Comparison with synchronous code:")

    def sync_square(n):
        time.sleep(0.5)  # Blocking sleep
        return n ** 2

    print("Synchronous version:")
    sync_start = time.time()
    sync_results = [sync_square(i) for i in range(1, 4)]
    sync_end = time.time()
    print(f"Sync results: {sync_results}")
    print(f"Sync time: {sync_end - sync_start:.2f} seconds")

    print("\nAsync version (concept - we'll see concurrent execution later):")
    print("Async allows other operations to run while waiting!")

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
