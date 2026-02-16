"""
Real World Async Examples Demo
==============================

Demonstrates practical async Python patterns for real-world applications.
"""

import asyncio
import aiohttp
import aiofiles
import time
import random
from typing import List, Dict, Optional
import json
import os

# Note: This demo uses aiohttp and aiofiles which would need to be installed
# For this demo, we'll simulate the real operations

class AsyncWebScraper:
    """Async web scraper for fetching multiple URLs."""

    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def fetch_url(self, url: str, timeout: float = 10.0) -> Optional[Dict]:
        """Fetch a URL with timeout and error handling."""
        async with self.semaphore:
            try:
                print(f"Fetching {url}")
                # Simulate HTTP request
                await asyncio.sleep(random.uniform(0.1, 1.0))

                # Simulate occasional failures
                if random.random() < 0.1:  # 10% failure rate
                    raise aiohttp.ClientError(f"Failed to fetch {url}")

                # Simulate response
                response_data = {
                    "url": url,
                    "status": 200,
                    "content_length": random.randint(1000, 10000),
                    "response_time": random.uniform(0.1, 2.0)
                }

                print(f"Completed {url}")
                return response_data

            except asyncio.TimeoutError:
                print(f"Timeout fetching {url}")
                return None
            except Exception as e:
                print(f"Error fetching {url}: {e}")
                return None

    async def scrape_multiple_urls(self, urls: List[str]) -> List[Dict]:
        """Scrape multiple URLs concurrently."""
        print(f"Starting to scrape {len(urls)} URLs with max {self.max_concurrent} concurrent requests")

        tasks = [self.fetch_url(url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Filter out None results and exceptions
        valid_results = [r for r in results if r is not None and not isinstance(r, Exception)]

        print(f"Successfully scraped {len(valid_results)} URLs")
        return valid_results

class AsyncFileProcessor:
    """Async file processor for batch file operations."""

    async def read_file_async(self, filename: str) -> str:
        """Read a file asynchronously."""
        print(f"Reading file: {filename}")
        # Simulate file reading
        await asyncio.sleep(random.uniform(0.05, 0.2))

        # Simulate file content
        content = f"Content of {filename}\n" * random.randint(5, 20)
        print(f"Read {len(content)} characters from {filename}")
        return content

    async def write_file_async(self, filename: str, content: str):
        """Write content to a file asynchronously."""
        print(f"Writing {len(content)} characters to {filename}")
        # Simulate file writing
        await asyncio.sleep(random.uniform(0.05, 0.15))
        print(f"Successfully wrote to {filename}")

    async def process_files_batch(self, input_files: List[str], output_dir: str):
        """Process multiple files concurrently."""
        print(f"Processing {len(input_files)} files to {output_dir}")

        async def process_single_file(input_file: str):
            try:
                content = await self.read_file_async(input_file)

                # Process content (e.g., convert to uppercase)
                processed_content = content.upper()

                # Generate output filename
                output_file = os.path.join(output_dir, f"processed_{os.path.basename(input_file)}")
                await self.write_file_async(output_file, processed_content)

                return f"Processed {input_file} -> {output_file}"
            except Exception as e:
                return f"Failed to process {input_file}: {e}"

        tasks = [process_single_file(file) for file in input_files]
        results = await asyncio.gather(*tasks)

        successful = sum(1 for r in results if "Processed" in r)
        print(f"Batch processing complete: {successful}/{len(input_files)} files processed")
        return results

class AsyncDatabaseClient:
    """Async database client simulation."""

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connected = False

    async def connect(self):
        """Establish database connection."""
        print(f"Connecting to database: {self.connection_string}")
        await asyncio.sleep(0.5)  # Connection time
        self.connected = True
        print("Database connected")

    async def disconnect(self):
        """Close database connection."""
        print("Disconnecting from database")
        await asyncio.sleep(0.2)
        self.connected = False
        print("Database disconnected")

    async def execute_query(self, query: str) -> List[Dict]:
        """Execute a database query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")

        print(f"Executing query: {query}")
        await asyncio.sleep(random.uniform(0.1, 0.5))  # Query time

        # Simulate query results
        if "SELECT" in query:
            num_results = random.randint(1, 10)
            results = [
                {"id": i, "name": f"Record {i}", "value": random.randint(1, 100)}
                for i in range(1, num_results + 1)
            ]
        else:
            results = [{"affected_rows": random.randint(1, 5)}]

        print(f"Query completed, returned {len(results)} rows")
        return results

    async def execute_batch_queries(self, queries: List[str]) -> List[List[Dict]]:
        """Execute multiple queries concurrently."""
        print(f"Executing batch of {len(queries)} queries")

        async def execute_single_query(query: str):
            return await self.execute_query(query)

        tasks = [execute_single_query(query) for query in queries]
        results = await asyncio.gather(*tasks)

        print("Batch queries completed")
        return results

class AsyncAPIRateLimiter:
    """Rate limiter for API calls."""

    def __init__(self, calls_per_minute: int = 60):
        self.calls_per_minute = calls_per_minute
        self.interval = 60.0 / calls_per_minute
        self.last_call_time = 0
        self._lock = asyncio.Lock()

    async def wait_if_needed(self):
        """Wait if necessary to respect rate limit."""
        async with self._lock:
            current_time = time.time()
            time_since_last_call = current_time - self.last_call_time

            if time_since_last_call < self.interval:
                wait_time = self.interval - time_since_last_call
                print(f"Rate limit: waiting {wait_time:.2f} seconds")
                await asyncio.sleep(wait_time)

            self.last_call_time = time.time()

    async def make_api_call(self, endpoint: str) -> Dict:
        """Make a rate-limited API call."""
        await self.wait_if_needed()

        print(f"Making API call to {endpoint}")
        await asyncio.sleep(random.uniform(0.1, 0.3))  # API call time

        # Simulate API response
        response = {
            "endpoint": endpoint,
            "status": 200,
            "data": {"result": f"Data from {endpoint}"},
            "timestamp": time.time()
        }

        return response

async def demo_web_scraping():
    """Demonstrate async web scraping."""
    print("=== Web Scraping Demo ===")

    scraper = AsyncWebScraper(max_concurrent=3)
    urls = [
        "https://api.github.com/users/octocat",
        "https://api.github.com/repos/microsoft/vscode",
        "https://api.github.com/repos/python/cpython",
        "https://api.github.com/users/defunkt",
        "https://api.github.com/repos/torvalds/linux"
    ]

    start_time = time.time()
    results = await scraper.scrape_multiple_urls(urls)
    end_time = time.time()

    print(f"Scraping completed in {end_time - start_time:.2f} seconds")
    print(f"Total URLs processed: {len(results)}")
    print()

async def demo_file_processing():
    """Demonstrate async file processing."""
    print("=== File Processing Demo ===")

    processor = AsyncFileProcessor()
    input_files = [f"input_{i}.txt" for i in range(1, 6)]

    start_time = time.time()
    results = await processor.process_files_batch(input_files, "output_dir")
    end_time = time.time()

    print(f"File processing completed in {end_time - start_time:.2f} seconds")
    for result in results:
        print(f"  {result}")
    print()

async def demo_database_operations():
    """Demonstrate async database operations."""
    print("=== Database Operations Demo ===")

    db = AsyncDatabaseClient("postgresql://localhost/mydb")

    try:
        await db.connect()

        # Single queries
        users = await db.execute_query("SELECT * FROM users WHERE active = 1")
        print(f"Found {len(users)} active users")

        products = await db.execute_query("SELECT * FROM products WHERE price > 10")
        print(f"Found {len(products)} products with price > 10")

        # Batch queries
        batch_queries = [
            "SELECT COUNT(*) FROM orders",
            "SELECT SUM(amount) FROM payments",
            "SELECT * FROM categories",
            "SELECT COUNT(*) FROM users WHERE created_today = 1"
        ]

        batch_results = await db.execute_batch_queries(batch_queries)
        print(f"Batch results: {[len(r) for r in batch_results]} rows each")

    finally:
        await db.disconnect()
    print()

async def demo_api_rate_limiting():
    """Demonstrate API rate limiting."""
    print("=== API Rate Limiting Demo ===")

    limiter = AsyncAPIRateLimiter(calls_per_minute=10)  # 10 calls per minute

    endpoints = [f"/api/endpoint/{i}" for i in range(1, 8)]

    start_time = time.time()
    tasks = [limiter.make_api_call(endpoint) for endpoint in endpoints]
    results = await asyncio.gather(*tasks)
    end_time = time.time()

    print(f"API calls completed in {end_time - start_time:.2f} seconds")
    print(f"Total calls made: {len(results)}")
    print()

async def demo_combined_workflow():
    """Demonstrate a combined async workflow."""
    print("=== Combined Workflow Demo ===")

    start_time = time.time()

    # Initialize components
    scraper = AsyncWebScraper(max_concurrent=2)
    db = AsyncDatabaseClient("sqlite:///workflow.db")
    limiter = AsyncAPIRateLimiter(calls_per_minute=20)

    try:
        await db.connect()

        # Step 1: Scrape data from multiple sources
        print("Step 1: Gathering data from web sources")
        urls = ["https://api.example.com/data/1", "https://api.example.com/data/2"]
        web_data = await scraper.scrape_multiple_urls(urls)

        # Step 2: Process and store data
        print("\nStep 2: Processing and storing data")
        for data in web_data:
            # Store in database
            await db.execute_query(f"INSERT INTO raw_data (url, content) VALUES ('{data['url']}', 'processed_content')")

        # Step 3: Make API calls for additional processing
        print("\nStep 3: Making API calls for processing")
        api_tasks = [
            limiter.make_api_call(f"/process/{i}")
            for i in range(len(web_data))
        ]
        api_results = await asyncio.gather(*api_tasks)

        # Step 4: Update database with processed results
        print("\nStep 4: Updating database with results")
        for result in api_results:
            await db.execute_query(f"UPDATE raw_data SET processed = 1 WHERE url = '{result['endpoint']}'")

        total_time = time.time() - start_time
        print(f"\nWorkflow completed in {total_time:.2f} seconds")
        print(f"Processed {len(web_data)} web sources and made {len(api_results)} API calls")

    finally:
        await db.disconnect()

async def main():
    """Run all real-world examples."""
    print("=== Real World Async Python Examples ===\n")

    await demo_web_scraping()
    await demo_file_processing()
    await demo_database_operations()
    await demo_api_rate_limiting()
    await demo_combined_workflow()

    print("All demos completed!")

if __name__ == "__main__":
    asyncio.run(main())
