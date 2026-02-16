"""
Async Python Lab - Exercise 1: Basic Async/Await

Implement basic async/await patterns and functions.
Complete the TODO sections with your implementations.
"""

import asyncio
import time
from typing import List, Dict, Any


# TODO: Implement simulate_download function
async def simulate_download(url: str, delay: float) -> str:
    """
    Simulate downloading data from a URL with a delay.

    Args:
        url: The URL to download from
        delay: Delay in seconds to simulate network latency

    Returns:
        A string representing the downloaded data
    """
    # Simulate network delay
    await asyncio.sleep(delay)

    # Return simulated data
    return f"Downloaded content from {url} at {time.time()}"


# TODO: Implement process_data function
async def process_data(data: str) -> Dict[str, Any]:
    """
    Process downloaded data and return structured information.

    Args:
        data: Raw downloaded data string

    Returns:
        Dictionary with processed information
    """
    # Simulate processing time
    await asyncio.sleep(0.1)

    # Process the data (simple example)
    return {
        "original_data": data,
        "length": len(data),
        "timestamp": time.time(),
        "processed": True
    }


# TODO: Implement download_and_process function
async def download_and_process(urls: List[str]) -> List[Dict[str, Any]]:
    """
    Download data from multiple URLs sequentially and process each one.

    Args:
        urls: List of URLs to download from

    Returns:
        List of processed data dictionaries
    """
    results = []

    for url in urls:
        # Download data
        data = await simulate_download(url, 0.5)

        # Process data
        processed = await process_data(data)

        results.append(processed)

    return results


# TODO: Implement async_main function
async def async_main():
    """
    Main async function that demonstrates the usage of all implemented functions.
    """
    print("=== Basic Async/Await Demo ===")

    # Test single download
    print("\n1. Testing single download:")
    data = await simulate_download("https://example.com", 1.0)
    print(f"Downloaded: {data[:50]}...")

    # Test data processing
    print("\n2. Testing data processing:")
    processed = await process_data(data)
    print(f"Processed data keys: {list(processed.keys())}")

    # Test sequential downloads
    print("\n3. Testing sequential downloads:")
    urls = ["url1", "url2", "url3"]
    start_time = time.time()
    results = await download_and_process(urls)
    elapsed = time.time() - start_time

    print(f"Processed {len(results)} URLs in {elapsed:.2f} seconds")
    for i, result in enumerate(results):
        print(f"  URL {i+1}: {result['length']} characters")


# TODO: Implement synchronous version for comparison
def sync_download_and_process(urls: List[str]) -> List[Dict[str, Any]]:
    """
    Synchronous version for performance comparison.

    Args:
        urls: List of URLs to download from

    Returns:
        List of processed data dictionaries
    """
    results = []

    for url in urls:
        # Simulate synchronous download (blocking)
        time.sleep(0.5)
        data = f"Synchronously downloaded content from {url} at {time.time()}"

        # Simulate synchronous processing (blocking)
        time.sleep(0.1)
        processed = {
            "original_data": data,
            "length": len(data),
            "timestamp": time.time(),
            "processed": True
        }

        results.append(processed)

    return results


def sync_main():
    """Synchronous version for comparison"""
    print("\n=== Synchronous Version for Comparison ===")

    urls = ["url1", "url2", "url3"]
    start_time = time.time()
    results = sync_download_and_process(urls)
    elapsed = time.time() - start_time

    print(f"Synchronously processed {len(results)} URLs in {elapsed:.2f} seconds")


if __name__ == "__main__":
    # Run async version
    asyncio.run(async_main())

    # Run sync version for comparison
    sync_main()
