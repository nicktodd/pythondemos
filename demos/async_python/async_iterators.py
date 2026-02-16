"""
Async Iterators Demo
====================

Demonstrates async iterators and async generators in Python.
"""

import asyncio
import random
from typing import AsyncGenerator, AsyncIterator

class AsyncDataStreamer:
    """Async iterator that streams data."""

    def __init__(self, data_source: list, chunk_size: int = 1):
        self.data_source = data_source
        self.chunk_size = chunk_size
        self.index = 0

    def __aiter__(self):
        """Return the async iterator object."""
        return self

    async def __anext__(self):
        """Get the next item from the iterator."""
        if self.index >= len(self.data_source):
            raise StopAsyncIteration

        # Get next chunk
        chunk = self.data_source[self.index:self.index + self.chunk_size]
        self.index += self.chunk_size

        # Simulate network/data processing delay
        await asyncio.sleep(0.1)
        print(f"Streaming chunk: {chunk}")
        return chunk

async def async_range(start: int, end: int, step: int = 1) -> AsyncGenerator[int, None]:
    """Async generator that yields numbers in a range."""
    current = start
    while current < end:
        print(f"Generating: {current}")
        yield current
        await asyncio.sleep(0.05)  # Simulate some async work
        current += step

async def fibonacci_generator(n: int) -> AsyncGenerator[int, None]:
    """Async generator for Fibonacci sequence."""
    a, b = 0, 1
    count = 0
    while count < n:
        print(f"Computing Fibonacci {count}: {a}")
        yield a
        await asyncio.sleep(0.1)  # Simulate computation time
        a, b = b, a + b
        count += 1

async def file_line_reader(filename: str) -> AsyncGenerator[str, None]:
    """Async generator that simulates reading lines from a file."""
    # Simulate file content
    lines = [
        "Line 1: Hello World",
        "Line 2: This is an async generator",
        "Line 3: Reading files asynchronously",
        "Line 4: Each line takes time to read",
        "Line 5: End of file"
    ]

    print(f"Opening file: {filename}")
    await asyncio.sleep(0.2)  # File open delay

    for line_num, line in enumerate(lines, 1):
        print(f"Reading line {line_num}")
        yield line
        await asyncio.sleep(0.15)  # Simulate read delay between lines

    print(f"Closing file: {filename}")

async def async_filter(predicate, async_iterable) -> AsyncGenerator:
    """Async version of filter."""
    async for item in async_iterable:
        if await predicate(item):
            yield item

async def async_map(func, async_iterable) -> AsyncGenerator:
    """Async version of map."""
    async for item in async_iterable:
        result = await func(item)
        yield result

async def is_even_async(n: int) -> bool:
    """Async predicate to check if number is even."""
    await asyncio.sleep(0.01)  # Simulate async check
    return n % 2 == 0

async def double_async(n: int) -> int:
    """Async function to double a number."""
    await asyncio.sleep(0.01)  # Simulate async operation
    return n * 2

class AsyncDatabaseCursor:
    """Async iterator for database results."""

    def __init__(self, query: str, batch_size: int = 3):
        self.query = query
        self.batch_size = batch_size
        self.current_batch = 0
        self.total_batches = 5  # Simulate 5 batches

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current_batch >= self.total_batches:
            raise StopAsyncIteration

        # Simulate fetching a batch of results
        batch_start = self.current_batch * self.batch_size + 1
        batch = [
            f"Record {batch_start + i}: {self.query}"
            for i in range(self.batch_size)
        ]

        print(f"Fetching batch {self.current_batch + 1}/{self.total_batches}")
        await asyncio.sleep(0.2)  # Database query delay

        self.current_batch += 1
        return batch

async def main():
    """Demonstrate async iterators and generators."""
    print("=== Async Iterators Demo ===\n")

    # 1. Basic async iterator
    print("1. Async iterator (streaming data):")
    data = list(range(1, 11))  # Numbers 1-10
    streamer = AsyncDataStreamer(data, chunk_size=3)

    async for chunk in streamer:
        print(f"Received: {chunk}")
    print()

    # 2. Async generator (range)
    print("2. Async generator (range):")
    async for number in async_range(1, 8, 2):
        print(f"Got number: {number}")
    print()

    # 3. Fibonacci async generator
    print("3. Fibonacci async generator:")
    async for fib_num in fibonacci_generator(8):
        print(f"Fibonacci number: {fib_num}")
    print()

    # 4. File reading simulation
    print("4. Simulated file reading:")
    async for line in file_line_reader("example.txt"):
        print(f"Read: {line}")
    print()

    # 5. Async filter and map
    print("5. Async filter and map:")
    numbers = async_range(1, 11)  # 1 to 10

    print("Original numbers:")
    collected = []
    async for num in numbers:
        collected.append(num)
    print(f"Collected: {collected}")

    # Reset the generator for filter/map
    numbers = async_range(1, 11)

    print("\nEven numbers (async filter):")
    even_numbers = async_filter(is_even_async, numbers)
    async for num in even_numbers:
        print(f"Even: {num}")

    # Reset for map
    numbers = async_range(1, 6)
    print("\nDoubled numbers (async map):")
    doubled = async_map(double_async, numbers)
    async for num in doubled:
        print(f"Doubled: {num}")
    print()

    # 6. Database cursor simulation
    print("6. Database cursor (batch processing):")
    cursor = AsyncDatabaseCursor("SELECT * FROM users WHERE active = 1")

    total_records = 0
    async for batch in cursor:
        print(f"Processing batch: {batch}")
        total_records += len(batch)

    print(f"Total records processed: {total_records}\n")

    # 7. Combining async iterators
    print("7. Combining multiple async iterators:")

    async def merge_iterators(*iterators):
        """Merge multiple async iterators by alternating between them."""
        # Convert to list of async iterators
        async_iters = list(iterators)
        
        while async_iters:
            # Try to get next item from each iterator
            exhausted_indices = []
            for i, async_iter in enumerate(async_iters):
                try:
                    item = await async_iter.__anext__()
                    yield item
                    await asyncio.sleep(0.01)  # Small delay between items
                except StopAsyncIteration:
                    # Mark for removal
                    exhausted_indices.append(i)
            
            # Remove exhausted iterators (in reverse order to maintain indices)
            for i in reversed(exhausted_indices):
                async_iters.pop(i)

    # Create multiple data streams
    stream1 = AsyncDataStreamer([f"A{i}" for i in range(1, 4)], chunk_size=1)
    stream2 = AsyncDataStreamer([f"B{i}" for i in range(1, 4)], chunk_size=1)

    print("Merging streams:")
    async for item in merge_iterators(stream1, stream2):
        print(f"Merged item: {item}")
        await asyncio.sleep(0.05)  # Slow down output for visibility

if __name__ == "__main__":
    asyncio.run(main())
