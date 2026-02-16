# Python Asynchronous Programming Lab

This lab will guide you through implementing comprehensive asynchronous programming concepts in Python. You'll build upon the concepts demonstrated in the `demos/async_python/` folder and learn how to write efficient, concurrent, and non-blocking Python code using asyncio.

## Prerequisites

Before starting, review the demo files in `demos/async_python/` to understand the concepts:

- `basic_async_await.py` - Core async/await syntax and patterns
- `coroutines_tasks.py` - Coroutines, tasks, and lifecycle management
- `concurrent_execution.py` - Running multiple operations concurrently with gather, as_completed, semaphores
- `async_context_managers.py` - Resource management with async context managers
- `async_iterators.py` - Asynchronous iterators and generators
- `error_handling.py` - Exception handling, retry logic, and cancellation
- `real_world_examples.py` - Practical applications like web scraping, file processing, API rate limiting
- `best_practices.py` - Performance optimization and robust async patterns

## Lab Structure

- **Starter files**: Located in `labs/async_python/`
- **Solutions**: Located in `solutions/async_python/` (check after completing exercises)
- **Your work**: Modify the starter files in `labs/async_python/`

## Exercise 1: Basic Async/Await

**File**: `labs/async_python/basic_async_await.py`

Implement basic async/await patterns:

1. Create an async function `simulate_download(url: str, delay: float) -> str` that simulates downloading data
2. Create an async function `process_data(data: str) -> Dict[str, Any]` that processes downloaded data
3. Create an async function `download_and_process(urls: List[str]) -> List[Dict[str, Any]]` that downloads and processes multiple URLs sequentially
4. Create an async function `async_main()` that demonstrates the usage
5. Test all functions and measure execution time

**Test your implementation**:
```python
# Test basic async/await
import asyncio

async def test_basic():
    start_time = time.time()

    # Test single download
    data = await simulate_download("https://example.com", 1.0)
    print(f"Downloaded: {data[:50]}...")

    # Test sequential processing
    urls = ["url1", "url2", "url3"]
    results = await download_and_process(urls)
    print(f"Processed {len(results)} items")

    elapsed = time.time() - start_time
    print(f"Sequential execution time: {elapsed:.2f}s")

asyncio.run(test_basic())
```

## Exercise 2: Coroutines and Tasks

**File**: `labs/async_python/coroutines_tasks.py`

Implement coroutine and task management:

1. Create an async function `background_worker(name: str, duration: float) -> str` that simulates work
2. Create a function `create_multiple_tasks(count: int) -> List[asyncio.Task]` that creates multiple tasks
3. Create an async function `monitor_tasks(tasks: List[asyncio.Task])` that monitors task progress
4. Create an async function `cancel_tasks_after_timeout(tasks: List[asyncio.Task], timeout: float)` that cancels tasks after a timeout
5. Implement proper task lifecycle management with cleanup

**Test your implementation**:
```python
# Test task management
async def test_tasks():
    # Create and monitor tasks
    tasks = create_multiple_tasks(5)
    await monitor_tasks(tasks)

    # Test cancellation
    tasks = create_multiple_tasks(3)
    await cancel_tasks_after_timeout(tasks, 1.5)

asyncio.run(test_tasks())
```

## Exercise 3: Concurrent Execution

**File**: `labs/async_python/concurrent_execution.py`

Implement concurrent execution patterns:

1. Create async functions for different types of work (CPU-bound simulation, I/O simulation)
2. Implement `run_sequential(tasks: List[Coroutine]) -> List[Any]` for sequential execution
3. Implement `run_concurrent_gather(tasks: List[Coroutine]) -> List[Any]` using asyncio.gather
4. Implement `run_concurrent_as_completed(tasks: List[Coroutine]) -> List[Any]` using asyncio.as_completed
5. Create a semaphore-based rate limiter `rate_limited_tasks(tasks: List[Coroutine], max_concurrent: int)`
6. Compare performance of different approaches

**Test your implementation**:
```python
# Test concurrent execution
async def test_concurrency():
    # Create test tasks
    tasks = [simulate_work(f"task_{i}", random.uniform(0.5, 2.0)) for i in range(10)]

    # Test different execution strategies
    print("Sequential:")
    results = await run_sequential(tasks)
    print(f"Results: {len(results)}")

    print("Concurrent with gather:")
    results = await run_concurrent_gather(tasks)
    print(f"Results: {len(results)}")

    print("Concurrent with as_completed:")
    results = await run_concurrent_as_completed(tasks)
    print(f"Results: {len(results)}")

asyncio.run(test_concurrency())
```

## Exercise 4: Async Context Managers

**File**: `labs/async_python/async_context_managers.py`

Implement async context managers for resource management:

1. Create an `AsyncFileHandler` class that implements async context manager protocol
2. Create an `AsyncDatabaseConnection` class for database operations
3. Create an `AsyncTimer` context manager that measures execution time
4. Implement nested context managers
5. Create a resource pool manager with proper cleanup

**Test your implementation**:
```python
# Test async context managers
async def test_context_managers():
    # Test file handler
    async with AsyncFileHandler("test.txt") as handler:
        await handler.write("Hello, async world!")
        content = await handler.read()
        print(f"File content: {content}")

    # Test timer
    async with AsyncTimer() as timer:
        await asyncio.sleep(1.0)
    print(f"Elapsed time: {timer.elapsed:.2f}s")

    # Test nested context managers
    async with AsyncTimer() as outer_timer:
        async with AsyncFileHandler("nested_test.txt") as handler:
            await handler.write("Nested operations")
        print(f"Inner operations took: {outer_timer.elapsed:.2f}s")

asyncio.run(test_context_managers())
```

## Exercise 5: Async Iterators

**File**: `labs/async_python/async_iterators.py`

Implement asynchronous iterators and generators:

1. Create an `AsyncDataStreamer` class that yields data asynchronously
2. Create an async generator function `async_file_reader(filename: str)` that reads files line by line
3. Create an async generator `async_range(start: int, end: int, step: int = 1)` that yields numbers with delays
4. Implement an async iterator for a simple database result set
5. Create a pipeline that processes data through multiple async iterators

**Test your implementation**:
```python
# Test async iterators
async def test_async_iterators():
    # Test data streamer
    streamer = AsyncDataStreamer(["chunk1", "chunk2", "chunk3"])
    async for chunk in streamer:
        print(f"Received: {chunk}")

    # Test async range
    async for num in async_range(1, 5, 1):
        print(f"Number: {num}")

    # Test file reader (if file exists)
    try:
        async for line in async_file_reader("sample.txt"):
            print(f"Line: {line.strip()}")
    except FileNotFoundError:
        print("Sample file not found")

asyncio.run(test_async_iterators())
```

## Exercise 6: Error Handling

**File**: `labs/async_python/error_handling.py`

Implement comprehensive error handling in async code:

1. Create async functions that can raise different types of exceptions
2. Implement `retry_async(func: Callable, max_retries: int, delay: float)` decorator for retry logic
3. Create `safe_gather(*coroutines)` that handles exceptions individually
4. Implement timeout handling with `asyncio.wait_for` and `asyncio.shield`
5. Create proper cancellation handling for long-running tasks
6. Implement structured error logging

**Test your implementation**:
```python
# Test error handling
async def test_error_handling():
    # Test retry decorator
    @retry_async(max_retries=3, delay=0.5)
    async def unreliable_operation():
        if random.random() < 0.7:  # 70% failure rate
            raise ConnectionError("Network error")
        return "Success"

    result = await unreliable_operation()
    print(f"Operation result: {result}")

    # Test safe gather
    async def failing_task():
        raise ValueError("Task failed")

    async def success_task():
        return "Task succeeded"

    results = await safe_gather(failing_task(), success_task())
    print(f"Safe gather results: {results}")

asyncio.run(test_error_handling())
```

## Exercise 7: Real World Examples

**File**: `labs/async_python/real_world_examples.py`

Implement practical async applications:

1. Create an async web scraper that fetches multiple URLs concurrently
2. Implement async file processing that reads and processes multiple files
3. Create an API rate limiter for external service calls
4. Implement async database operations simulation
5. Create a producer-consumer pattern for data processing pipeline
6. Implement concurrent image processing simulation

**Test your implementation**:
```python
# Test real world examples
async def test_real_world():
    # Test web scraper
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1"
    ]
    results = await scrape_multiple_urls(urls)
    print(f"Scraped {len(results)} pages")

    # Test file processing
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    # Create sample files first
    for filename in filenames:
        async with aiofiles.open(filename, 'w') as f:
            await f.write(f"Content of {filename}")

    results = await process_multiple_files(filenames)
    print(f"Processed {len(results)} files")

asyncio.run(test_real_world())
```

## Exercise 8: Best Practices

**File**: `labs/async_python/best_practices.py`

Apply async programming best practices:

1. Implement proper resource management with async context managers
2. Create retry logic with exponential backoff
3. Implement rate limiting and semaphores
4. Create producer-consumer patterns with asyncio.Queue
5. Implement proper task lifecycle management
6. Add comprehensive error handling and logging
7. Optimize for performance while maintaining readability

**Test your implementation**:
```python
# Test best practices
async def test_best_practices():
    # Test resource management
    async with managed_http_session() as session:
        data = await fetch_with_retry(session, "https://httpbin.org/json")
        print(f"Fetched data: {data[:100]}...")

    # Test rate limiting
    semaphore = asyncio.Semaphore(3)
    tasks = [rate_limited_task(semaphore, f"task_{i}") for i in range(10)]
    results = await asyncio.gather(*tasks)
    print(f"Rate limited tasks completed: {len(results)}")

    # Test producer-consumer
    queue = asyncio.Queue()
    producer = asyncio.create_task(produce_items(queue, 5))
    consumers = [asyncio.create_task(consume_items(queue, i)) for i in range(3)]

    await asyncio.gather(producer, *consumers)
    print("Producer-consumer pattern completed")

asyncio.run(test_best_practices())
```

## Exercise 9: Integration Project

**File**: `labs/async_python/integration_project.py`

Create a comprehensive async application that combines all concepts:

1. Build an async web crawler that respects rate limits
2. Implement concurrent data processing pipeline
3. Create async API client with retry logic and caching
4. Implement async file monitoring and processing system
5. Create a task scheduler with proper error handling
6. Build a dashboard that monitors async operations

**Test your implementation**:
```python
# Test the complete async system
async def test_integration():
    # Initialize components
    crawler = AsyncWebCrawler(rate_limit=5)
    processor = DataProcessor(workers=3)
    api_client = AsyncAPIClient(retries=3)
    scheduler = TaskScheduler()

    # Run integrated workflow
    urls = ["https://api.example.com/data/1", "https://api.example.com/data/2"]
    tasks = []

    for url in urls:
        task = scheduler.schedule(crawler.crawl_and_process(url, processor))
        tasks.append(task)

    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Integration test completed with {len(results)} results")

asyncio.run(test_integration())
```

## Submission

1. Complete all exercises in the `labs/async_python/` files
2. Test your implementations with the provided test cases
3. Compare your solutions with the completed versions in `solutions/async_python/`
4. Run the demo files to see advanced examples
5. Run `python demos/async_python/run_demos.py` to see all concepts in action

## Tips

- Start with Exercise 1 and build upon previous exercises
- Use the demo files as references, but implement your own versions
- Test frequently as you implement each function
- Remember that async code runs concurrently, not in parallel (on a single thread)
- Always use `asyncio.run()` to run the top-level async function
- Use `await` to call async functions and `asyncio.create_task()` for concurrent execution
- Handle exceptions properly in async code
- Use semaphores and queues for resource management

## Additional Resources

- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Real Python Asyncio Guide](https://realpython.com/async-io-python/)
- [AsyncIO Best Practices](https://docs.python.org/3/library/asyncio-dev.html)
- [FastAPI Async Documentation](https://fastapi.tiangolo.com/async/)
