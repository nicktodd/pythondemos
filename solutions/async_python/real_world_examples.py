"""
Async Python Lab - Exercise 7: Real World Examples - SOLUTION

Complete implementation of practical async applications like web scraping, file processing, and API rate limiting.
"""

import asyncio
import time
import random
import json
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin
import aiohttp


async def scrape_multiple_urls(urls: List[str]) -> List[Optional[str]]:
    """
    Scrape multiple URLs concurrently.

    Args:
        urls: List of URLs to scrape

    Returns:
        List of scraped content (or None if failed)
    """
    async def scrape_single_url(session: aiohttp.ClientSession, url: str) -> Optional[str]:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                response.raise_for_status()
                return await response.text()
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
            return None

    async with aiohttp.ClientSession() as session:
        tasks = [scrape_single_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Handle exceptions in results
        processed_results = []
        for result in results:
            if isinstance(result, Exception):
                processed_results.append(None)
            else:
                processed_results.append(result)

        return processed_results


async def process_multiple_files(filenames: List[str]) -> List[Optional[Dict[str, Any]]]:
    """
    Process multiple files concurrently.

    Args:
        filenames: List of file paths to process

    Returns:
        List of processed file data
    """
    async def process_single_file(filename: str) -> Optional[Dict[str, Any]]:
        try:
            # Simulate file reading (in real code, use aiofiles)
            await asyncio.sleep(0.2)  # Simulate I/O delay

            # For demo, create fake file content
            fake_content = f"This is content from {filename}\nLine 2\nLine 3"

            # Process the content
            lines = fake_content.split('\n')
            word_count = sum(len(line.split()) for line in lines)
            char_count = len(fake_content)

            return {
                "filename": filename,
                "lines": len(lines),
                "words": word_count,
                "characters": char_count,
                "processed_at": time.time()
            }

        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            return None

    # Process all files concurrently
    tasks = [process_single_file(filename) for filename in filenames]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle exceptions
    processed_results = []
    for result in results:
        if isinstance(result, Exception):
            processed_results.append(None)
        else:
            processed_results.append(result)

    return processed_results


class RateLimiter:
    """
    Rate limiter for API calls.
    """

    def __init__(self, calls_per_minute: int):
        self.calls_per_minute = calls_per_minute
        self.interval = 60.0 / calls_per_minute
        self.last_call_time = 0.0
        self._lock = asyncio.Lock()

    async def wait_if_needed(self):
        """Wait if necessary to respect rate limit"""
        async with self._lock:
            current_time = time.time()
            time_since_last_call = current_time - self.last_call_time

            if time_since_last_call < self.interval:
                wait_time = self.interval - time_since_last_call
                await asyncio.sleep(wait_time)

            self.last_call_time = time.time()


async def call_rate_limited_api(api_endpoints: List[str], rate_limiter: RateLimiter) -> List[Optional[Dict[str, Any]]]:
    """
    Call multiple API endpoints with rate limiting.

    Args:
        api_endpoints: List of API endpoints to call
        rate_limiter: RateLimiter instance

    Returns:
        List of API responses
    """
    async def call_single_endpoint(session: aiohttp.ClientSession, endpoint: str) -> Optional[Dict[str, Any]]:
        await rate_limiter.wait_if_needed()

        try:
            async with session.get(endpoint, timeout=aiohttp.ClientTimeout(total=5)) as response:
                response.raise_for_status()
                data = await response.json()
                return {
                    "endpoint": endpoint,
                    "status": response.status,
                    "data": data,
                    "timestamp": time.time()
                }
        except Exception as e:
            print(f"Failed to call {endpoint}: {e}")
            return None

    async with aiohttp.ClientSession() as session:
        tasks = [call_single_endpoint(session, endpoint) for endpoint in api_endpoints]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Handle exceptions
        processed_results = []
        for result in results:
            if isinstance(result, Exception):
                processed_results.append(None)
            else:
                processed_results.append(result)

        return processed_results


async def simulate_database_operations(operations: List[Dict[str, Any]]) -> List[Optional[Dict[str, Any]]]:
    """
    Simulate concurrent database operations.

    Args:
        operations: List of operation specifications

    Returns:
        List of operation results
    """
    async def execute_operation(op: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        try:
            op_type = op.get("type", "select")
            table = op.get("table", "unknown")
            duration = op.get("duration", 0.5)

            # Simulate database operation time
            await asyncio.sleep(duration)

            # Simulate different operation results
            if op_type == "select":
                result = {"rows": random.randint(1, 100), "table": table}
            elif op_type == "insert":
                result = {"inserted_id": random.randint(1000, 9999), "table": table}
            elif op_type == "update":
                result = {"affected_rows": random.randint(1, 50), "table": table}
            else:
                result = {"message": f"Unknown operation: {op_type}"}

            return {
                "operation": op,
                "result": result,
                "execution_time": duration,
                "timestamp": time.time()
            }

        except Exception as e:
            print(f"Database operation failed: {e}")
            return None

    # Execute all operations concurrently
    tasks = [execute_operation(op) for op in operations]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle exceptions
    processed_results = []
    for result in results:
        if isinstance(result, Exception):
            processed_results.append(None)
        else:
            processed_results.append(result)

    return processed_results


class ProducerConsumerPipeline:
    """
    Producer-consumer pattern for data processing pipeline.
    """

    def __init__(self, num_consumers: int = 3):
        self.queue = asyncio.Queue()
        self.num_consumers = num_consumers
        self.producer_done = False

    async def producer(self, items: List[Any]):
        """Produce items to the queue"""
        for item in items:
            await self.queue.put(item)
            await asyncio.sleep(0.1)  # Simulate production time

        # Signal that production is done
        for _ in range(self.num_consumers):
            await self.queue.put(None)

        self.producer_done = True

    async def consumer(self, consumer_id: int) -> List[Any]:
        """Consume and process items from the queue"""
        results = []

        while True:
            item = await self.queue.get()

            if item is None:  # Sentinel value
                self.queue.task_done()
                break

            # Process the item
            processed_item = {
                "original": item,
                "processed_by": consumer_id,
                "processed_at": time.time(),
                "result": f"Processed {item} by consumer {consumer_id}"
            }

            results.append(processed_item)
            await asyncio.sleep(0.2)  # Simulate processing time
            self.queue.task_done()

        return results

    async def run_pipeline(self, items: List[Any]) -> List[Any]:
        """Run the complete producer-consumer pipeline"""
        # Start producer
        producer_task = asyncio.create_task(self.producer(items))

        # Start consumers
        consumer_tasks = [asyncio.create_task(self.consumer(i)) for i in range(self.num_consumers)]

        # Wait for producer to finish
        await producer_task

        # Wait for all consumers to finish
        consumer_results = await asyncio.gather(*consumer_tasks)

        # Flatten results
        all_results = []
        for consumer_result in consumer_results:
            all_results.extend(consumer_result)

        return all_results


async def concurrent_image_processing(image_files: List[str]) -> List[Optional[Dict[str, Any]]]:
    """
    Simulate concurrent image processing operations.

    Args:
        image_files: List of image file paths

    Returns:
        List of processing results
    """
    async def process_image(filename: str) -> Optional[Dict[str, Any]]:
        try:
            # Simulate image loading
            await asyncio.sleep(0.3)

            # Simulate processing operations
            operations = ["resize", "filter", "compress"]
            results = {}

            for op in operations:
                # Simulate operation time
                await asyncio.sleep(random.uniform(0.2, 0.5))
                results[op] = f"Applied {op} to {filename}"

            return {
                "filename": filename,
                "operations": results,
                "total_time": sum(random.uniform(0.2, 0.5) for _ in operations),
                "processed_at": time.time()
            }

        except Exception as e:
            print(f"Failed to process image {filename}: {e}")
            return None

    # Process all images concurrently
    tasks = [process_image(filename) for filename in image_files]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle exceptions
    processed_results = []
    for result in results:
        if isinstance(result, Exception):
            processed_results.append(None)
        else:
            processed_results.append(result)

    return processed_results


async def web_scraping_demo():
    """
    Demonstrate concurrent web scraping.
    """
    print("=== Web Scraping Demo ===")

    # Use mock URLs for demo (these would be real URLs in production)
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1"
    ]

    print(f"Scraping {len(urls)} URLs concurrently...")
    start_time = time.time()

    results = await scrape_multiple_urls(urls)

    elapsed = time.time() - start_time
    successful = sum(1 for r in results if r is not None)

    print(f"Scraping complete: {successful}/{len(urls)} successful in {elapsed:.2f}s")


async def file_processing_demo():
    """
    Demonstrate concurrent file processing.
    """
    print("=== File Processing Demo ===")

    # Simulate file list
    filenames = [f"document_{i}.txt" for i in range(1, 6)]

    print(f"Processing {len(filenames)} files concurrently...")
    start_time = time.time()

    results = await process_multiple_files(filenames)

    elapsed = time.time() - start_time
    successful = sum(1 for r in results if r is not None)

    print(f"File processing complete: {successful}/{len(filenames)} successful in {elapsed:.2f}s")

    # Show sample results
    for result in results[:3]:  # Show first 3 results
        if result:
            print(f"  {result['filename']}: {result['words']} words, {result['lines']} lines")


async def api_rate_limiting_demo():
    """
    Demonstrate API rate limiting.
    """
    print("=== API Rate Limiting Demo ===")

    # Simulate API endpoints
    endpoints = [f"https://httpbin.org/delay/0.1?t={i}" for i in range(1, 8)]

    # Rate limit: 10 calls per minute (6 seconds between calls)
    rate_limiter = RateLimiter(calls_per_minute=10)

    print(f"Calling {len(endpoints)} API endpoints with rate limiting...")
    start_time = time.time()

    results = await call_rate_limited_api(endpoints, rate_limiter)

    elapsed = time.time() - start_time
    successful = sum(1 for r in results if r is not None)

    print(f"API calls complete: {successful}/{len(endpoints)} successful in {elapsed:.2f}s")


async def producer_consumer_demo():
    """
    Demonstrate producer-consumer pipeline.
    """
    print("=== Producer-Consumer Demo ===")

    # Create pipeline
    pipeline = ProducerConsumerPipeline(num_consumers=3)

    # Generate test data
    items = [f"item_{i}" for i in range(1, 11)]

    print(f"Processing {len(items)} items through producer-consumer pipeline...")
    start_time = time.time()

    results = await pipeline.run_pipeline(items)

    elapsed = time.time() - start_time

    print(f"Pipeline complete: {len(results)} items processed in {elapsed:.2f}s")

    # Show sample results
    for result in results[:5]:  # Show first 5 results
        print(f"  {result['original']} -> {result['result']}")


async def comprehensive_real_world_demo():
    """
    Run all real-world async demonstrations.
    """
    print("=== Comprehensive Real-World Async Demo ===")

    await web_scraping_demo()
    print()

    await file_processing_demo()
    print()

    await api_rate_limiting_demo()
    print()

    await producer_consumer_demo()
    print()

    # Additional demo: database operations
    print("=== Database Operations Demo ===")
    operations = [
        {"type": "select", "table": "users", "duration": 0.3},
        {"type": "insert", "table": "products", "duration": 0.4},
        {"type": "update", "table": "orders", "duration": 0.2},
        {"type": "select", "table": "inventory", "duration": 0.5},
        {"type": "insert", "table": "logs", "duration": 0.3}
    ]

    print(f"Executing {len(operations)} database operations concurrently...")
    start_time = time.time()

    results = await simulate_database_operations(operations)

    elapsed = time.time() - start_time
    successful = sum(1 for r in results if r is not None)

    print(f"Database operations complete: {successful}/{len(operations)} successful in {elapsed:.2f}s")

    print("\n=== All Real-World Demos Complete ===")


if __name__ == "__main__":
    asyncio.run(comprehensive_real_world_demo())
