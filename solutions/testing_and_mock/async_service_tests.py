"""
Async Service Tests Solution

Complete implementation of tests for asynchronous service methods with pytest-asyncio.
"""

import pytest
from unittest.mock import AsyncMock, Mock, patch
import asyncio
import aiofiles
import time


class AsyncDataProcessor:
    """Asynchronous data processing service."""

    def __init__(self, api_client=None):
        self.api_client = api_client or Mock()

    async def process_data(self, data):
        """Process data asynchronously."""
        await asyncio.sleep(0.1)  # Simulate async work
        if "input" in data:
            result = {
                "status": "processed",
                "input_length": len(str(data["input"])),
                "processed_at": "timestamp"
            }
            return result
        else:
            raise ValueError("Invalid data format")

    async def fetch_multiple_items(self, item_ids):
        """Fetch multiple items concurrently."""
        async def fetch_item(item_id):
            await asyncio.sleep(0.05)  # Simulate network delay
            if item_id == 999:  # Simulate error for specific ID
                raise ValueError(f"Item {item_id} not found")
            return {"id": item_id, "data": f"item_{item_id}"}

        tasks = [fetch_item(item_id) for item_id in item_ids]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

    async def save_results(self, results, filename):
        """Save results to file asynchronously."""
        async with aiofiles.open(filename, 'w') as f:
            await f.write(str(results))
        return True


@pytest.fixture
async def async_processor():
    """Async fixture for data processor."""
    processor = AsyncDataProcessor()
    yield processor
    # Cleanup if needed


@pytest.mark.asyncio
async def test_process_data_success(async_processor):
    """Test successful data processing."""
    data = {"input": "test data"}
    result = await async_processor.process_data(data)

    assert result["status"] == "processed"
    assert result["input_length"] == len("test data")
    assert "processed_at" in result


@pytest.mark.asyncio
async def test_process_data_with_api_call(async_processor):
    """Test data processing that makes API calls."""
    # Mock the API client
    async_processor.api_client.fetch_data = AsyncMock(return_value={"external": "data"})

    data = {"input": "test", "use_api": True}
    result = await async_processor.process_data(data)

    # Verify API was called
    async_processor.api_client.fetch_data.assert_called_once()
    assert result["status"] == "processed"


@pytest.mark.asyncio
async def test_process_data_invalid_input(async_processor):
    """Test data processing with invalid input."""
    with pytest.raises(ValueError, match="Invalid data format"):
        await async_processor.process_data({"invalid": "data"})


@pytest.mark.asyncio
async def test_fetch_multiple_items_concurrent():
    """Test concurrent fetching of multiple items."""
    processor = AsyncDataProcessor()
    item_ids = [1, 2, 3, 4, 5]

    start_time = time.time()
    results = await processor.fetch_multiple_items(item_ids)
    end_time = time.time()

    # Should complete faster than sequential (5 * 0.05 = 0.25 seconds)
    assert end_time - start_time < 0.2

    assert len(results) == 5
    for i, result in enumerate(results):
        assert result["id"] == item_ids[i]
        assert result["data"] == f"item_{item_ids[i]}"


@pytest.mark.asyncio
async def test_fetch_multiple_items_with_errors():
    """Test concurrent fetching with some failures."""
    processor = AsyncDataProcessor()
    item_ids = [1, 2, 999, 4]  # 999 will fail

    results = await processor.fetch_multiple_items(item_ids)

    assert len(results) == 4
    # Check successful results
    assert results[0]["id"] == 1
    assert results[1]["id"] == 2
    assert results[3]["id"] == 4
    # Check error result
    assert isinstance(results[2], ValueError)
    assert "Item 999 not found" in str(results[2])


@pytest.mark.asyncio
async def test_save_results_to_file(tmp_path):
    """Test async file saving."""
    processor = AsyncDataProcessor()
    results = [{"id": 1, "data": "test"}]
    filename = tmp_path / "test_results.txt"

    await processor.save_results(results, str(filename))

    # Verify file was created and contains data
    assert filename.exists()
    async with aiofiles.open(filename, 'r') as f:
        content = await f.read()
    assert "test" in content


class AsyncContextManager:
    """Example async context manager for testing."""

    def __init__(self):
        self.entered = False
        self.exited = False

    async def __aenter__(self):
        self.entered = True
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.exited = True
        return None


@pytest.mark.asyncio
async def test_async_context_manager():
    """Test async context manager usage."""
    manager = AsyncContextManager()

    async with manager:
        assert manager.entered is True
        assert manager.exited is False

    assert manager.entered is True
    assert manager.exited is True


@pytest.mark.asyncio
async def test_async_operation_timeout():
    """Test async operation with timeout."""
    async def slow_operation():
        await asyncio.sleep(0.2)
        return "completed"

    # Test successful completion within timeout
    result = await asyncio.wait_for(slow_operation(), timeout=0.5)
    assert result == "completed"

    # Test timeout
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(slow_operation(), timeout=0.1)


@pytest.mark.asyncio
async def test_async_operation_cancellation():
    """Test cancelling async operations."""
    async def cancellable_operation():
        try:
            await asyncio.sleep(0.2)
            return "completed"
        except asyncio.CancelledError:
            return "cancelled"

    task = asyncio.create_task(cancellable_operation())
    await asyncio.sleep(0.05)  # Let task start
    task.cancel()

    result = await task
    assert result == "cancelled"


async def async_range(n):
    """Async generator example."""
    for i in range(n):
        yield i
        await asyncio.sleep(0.01)


@pytest.mark.asyncio
async def test_async_generator():
    """Test async generator functions."""
    results = []
    async for value in async_range(3):
        results.append(value)

    assert results == [0, 1, 2]


@pytest.mark.asyncio
async def test_concurrent_performance():
    """Test performance of concurrent operations."""
    async def slow_task(task_id):
        await asyncio.sleep(0.1)
        return f"task_{task_id}"

    # Sequential execution
    start_time = time.time()
    sequential_results = []
    for i in range(3):
        result = await slow_task(i)
        sequential_results.append(result)
    sequential_time = time.time() - start_time

    # Concurrent execution
    start_time = time.time()
    concurrent_results = await asyncio.gather(*[slow_task(i) for i in range(3)])
    concurrent_time = time.time() - start_time

    # Verify results are the same
    assert sequential_results == concurrent_results

    # Concurrent should be significantly faster
    assert concurrent_time < sequential_time * 0.8  # At least 20% faster
