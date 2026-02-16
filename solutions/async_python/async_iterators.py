"""
Async Python Lab - Exercise 5: Async Iterators - SOLUTION

Complete implementation of asynchronous iterators and generators.
"""

import asyncio
import time
import random
from typing import AsyncIterator, AsyncGenerator, List, Any


class AsyncDataStreamer:
    """
    An async iterator that streams data asynchronously.
    """

    def __init__(self, data: List[Any]):
        self.data = data
        self.index = 0

    def __aiter__(self):
        """Return the async iterator object"""
        return self

    async def __anext__(self):
        """Return the next item from the data stream"""
        if self.index >= len(self.data):
            raise StopAsyncIteration

        # Simulate async data fetching
        await asyncio.sleep(0.2)

        item = self.data[self.index]
        self.index += 1

        return item


async def async_file_reader(filename: str) -> AsyncGenerator[str, None]:
    """
    Async generator that reads a file line by line.

    Args:
        filename: Path to the file to read

    Yields:
        Lines from the file
    """
    try:
        # In a real implementation, you'd use aiofiles
        # For this demo, we'll simulate with regular file operations
        with open(filename, 'r') as file:
            for line in file:
                # Simulate async I/O delay
                await asyncio.sleep(0.1)
                yield line.rstrip('\n\r')

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return


async def async_range(start: int, end: int, step: int = 1) -> AsyncGenerator[int, None]:
    """
    Async generator that yields numbers in a range with delays.

    Args:
        start: Starting number
        end: Ending number (exclusive)
        step: Step size

    Yields:
        Numbers in the range
    """
    current = start

    while current < end:
        # Simulate computation delay
        await asyncio.sleep(0.15)
        yield current
        current += step


class AsyncDatabaseResult:
    """
    Async iterator for database query results.
    """

    def __init__(self, query_results: List[dict]):
        self.results = query_results
        self.index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.index >= len(self.results):
            raise StopAsyncIteration

        # Simulate database fetch delay
        await asyncio.sleep(0.1)

        result = self.results[self.index]
        self.index += 1

        return result


async def simulate_database_query(table: str, limit: int = 10) -> AsyncDatabaseResult:
    """
    Simulate a database query that returns an async iterator.

    Args:
        table: Table name to query
        limit: Maximum number of results

    Returns:
        AsyncDatabaseResult iterator
    """
    # Simulate query execution time
    await asyncio.sleep(0.3)

    # Generate fake results
    results = []
    for i in range(limit):
        results.append({
            "id": i + 1,
            "name": f"Record {i + 1}",
            "table": table,
            "timestamp": time.time() + i
        })

    return AsyncDatabaseResult(results)


async def data_processing_pipeline() -> AsyncGenerator[dict, None]:
    """
    A processing pipeline that transforms data through multiple async operations.

    Yields:
        Processed data items
    """
    # Stage 1: Generate raw data
    raw_data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": 20},
        {"id": 3, "value": 30},
        {"id": 4, "value": 40},
        {"id": 5, "value": 50}
    ]

    for item in raw_data:
        # Simulate data fetching
        await asyncio.sleep(0.1)

        # Stage 2: Transform data
        transformed = {
            **item,
            "doubled": item["value"] * 2,
            "squared": item["value"] ** 2,
            "processed_at": time.time()
        }

        # Stage 3: Filter (only even values)
        if transformed["value"] % 2 == 0:
            # Stage 4: Final processing
            await asyncio.sleep(0.05)
            transformed["final_score"] = transformed["doubled"] + transformed["squared"]

            yield transformed


async def async_iterator_demo():
    """
    Demonstrate basic async iterator usage.
    """
    print("=== Async Iterator Demo ===")

    # Test AsyncDataStreamer
    print("\n1. AsyncDataStreamer:")
    data = ["chunk1", "chunk2", "chunk3", "chunk4", "chunk5"]
    streamer = AsyncDataStreamer(data)

    async for chunk in streamer:
        print(f"Received: {chunk}")

    # Test async_range
    print("\n2. Async Range:")
    async for num in async_range(1, 6, 1):
        print(f"Number: {num}")

    # Test async_range with step
    print("\n3. Async Range with step 2:")
    async for num in async_range(0, 10, 2):
        print(f"Even number: {num}")


async def file_processing_demo():
    """
    Demonstrate async file reading.
    """
    print("=== File Processing Demo ===")

    # Create a test file
    test_filename = "async_test_file.txt"
    test_content = """Line 1: Hello async world
Line 2: This is a test file
Line 3: For async file reading
Line 4: Each line is processed asynchronously
Line 5: End of test file"""

    try:
        # Write test file
        with open(test_filename, 'w') as f:
            f.write(test_content)

        print(f"Created test file: {test_filename}")

        # Read file asynchronously
        print("\nReading file asynchronously:")
        line_count = 0
        async for line in async_file_reader(test_filename):
            line_count += 1
            print(f"Line {line_count}: {line}")

        print(f"\nProcessed {line_count} lines")

    except Exception as e:
        print(f"File processing error: {e}")
    finally:
        # Cleanup
        import os
        if os.path.exists(test_filename):
            os.remove(test_filename)
            print(f"Cleaned up test file: {test_filename}")


async def database_simulation_demo():
    """
    Demonstrate async database result iteration.
    """
    print("=== Database Simulation Demo ===")

    # Simulate querying different tables
    tables = ["users", "products", "orders"]

    for table in tables:
        print(f"\nQuerying table: {table}")

        try:
            results = await simulate_database_query(table, 3)

            async for row in results:
                print(f"  {row}")

        except Exception as e:
            print(f"Error querying {table}: {e}")


async def pipeline_demo():
    """
    Demonstrate the data processing pipeline.
    """
    print("=== Data Processing Pipeline Demo ===")

    print("Processing data through pipeline:")
    total_processed = 0
    total_score = 0

    async for processed_item in data_processing_pipeline():
        total_processed += 1
        total_score += processed_item["final_score"]
        print(f"Processed item {processed_item['id']}: value={processed_item['value']}, "
              f"final_score={processed_item['final_score']}")

    print(f"\nPipeline complete: {total_processed} items processed, "
          f"total score: {total_score}")


async def comprehensive_async_iterator_demo():
    """
    Run all async iterator demonstrations.
    """
    print("=== Comprehensive Async Iterator Demo ===")

    await async_iterator_demo()
    await file_processing_demo()
    await database_simulation_demo()
    await pipeline_demo()

    print("\n=== All Async Iterator Demos Complete ===")


if __name__ == "__main__":
    asyncio.run(comprehensive_async_iterator_demo())
