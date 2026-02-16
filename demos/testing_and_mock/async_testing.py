# filepath: d:\GitRepos\Courses\pythondemos\demos\testing_and_mock\async_testing.py
"""
Async Testing Demo

This module demonstrates testing asynchronous code with pytest:
- pytest-asyncio for async test functions
- Async fixtures
- Testing async context managers
- Mocking async functions
- Testing concurrent operations
"""

import pytest
import asyncio
from unittest.mock import AsyncMock, Mock, patch
import aiohttp
import aiofiles
import json
from typing import List, Dict, Any
from contextlib import asynccontextmanager


# Sample async application code
class AsyncDataService:
    """Asynchronous data service."""

    def __init__(self, base_url="https://api.example.com"):
        self.base_url = base_url
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def fetch_user(self, user_id: int) -> Dict[str, Any]:
        """Fetch user data asynchronously."""
        url = f"{self.base_url}/users/{user_id}"

        async with self.session.get(url) as response:
            response.raise_for_status()
            return await response.json()

    async def fetch_users(self, user_ids: List[int]) -> List[Dict[str, Any]]:
        """Fetch multiple users concurrently."""
        tasks = [self.fetch_user(user_id) for user_id in user_ids]
        return await asyncio.gather(*tasks)

    async def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new user."""
        url = f"{self.base_url}/users"

        async with self.session.post(url, json=user_data) as response:
            response.raise_for_status()
            return await response.json()

    async def save_to_file(self, data: Dict[str, Any], filename: str) -> None:
        """Save data to file asynchronously."""
        async with aiofiles.open(filename, 'w') as f:
            await f.write(json.dumps(data, indent=2))


class AsyncCalculator:
    """Asynchronous calculator with simulated delays."""

    @staticmethod
    async def slow_add(a: float, b: float, delay: float = 0.1) -> float:
        """Add two numbers with artificial delay."""
        await asyncio.sleep(delay)
        return a + b

    @staticmethod
    async def slow_multiply(a: float, b: float, delay: float = 0.1) -> float:
        """Multiply two numbers with artificial delay."""
        await asyncio.sleep(delay)
        return a * b

    @staticmethod
    async def compute_factorial(n: int) -> int:
        """Compute factorial asynchronously."""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0 or n == 1:
            return 1

        # Simulate some async work
        await asyncio.sleep(0.01)
        result = 1
        for i in range(2, n + 1):
            result *= i
            await asyncio.sleep(0.001)  # Small delay per iteration

        return result


class AsyncFileProcessor:
    """Process files asynchronously."""

    async def process_file(self, filename: str) -> Dict[str, Any]:
        """Process a file asynchronously."""
        try:
            async with aiofiles.open(filename, 'r') as f:
                content = await f.read()

            # Simulate processing
            await asyncio.sleep(0.05)

            lines = content.split('\n')
            words = content.split()
            chars = len(content)

            return {
                "filename": filename,
                "lines": len(lines),
                "words": len(words),
                "characters": chars,
                "content": content[:100] + "..." if len(content) > 100 else content
            }
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")

    async def process_multiple_files(self, filenames: List[str]) -> List[Dict[str, Any]]:
        """Process multiple files concurrently."""
        tasks = [self.process_file(filename) for filename in filenames]
        return await asyncio.gather(*tasks, return_exceptions=True)


# Async test fixtures
@pytest.fixture
async def async_data_service():
    """Async fixture for DataService."""
    async with AsyncDataService() as service:
        yield service


@pytest.fixture
def sample_user_data():
    """Fixture providing sample user data."""
    return {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30
    }


# Basic async tests
@pytest.mark.asyncio
async def test_slow_add():
    """Test async addition."""
    result = await AsyncCalculator.slow_add(3, 5)
    assert result == 8

    result = await AsyncCalculator.slow_add(10.5, 2.3)
    assert result == 12.8


@pytest.mark.asyncio
async def test_slow_multiply():
    """Test async multiplication."""
    result = await AsyncCalculator.slow_multiply(4, 7)
    assert result == 28

    result = await AsyncCalculator.slow_multiply(3.5, 2)
    assert result == 7.0


@pytest.mark.asyncio
async def test_compute_factorial():
    """Test async factorial computation."""
    assert await AsyncCalculator.compute_factorial(0) == 1
    assert await AsyncCalculator.compute_factorial(1) == 1
    assert await AsyncCalculator.compute_factorial(5) == 120
    assert await AsyncCalculator.compute_factorial(10) == 3628800


@pytest.mark.asyncio
async def test_compute_factorial_negative():
    """Test factorial with negative input."""
    with pytest.raises(ValueError, match="not defined for negative"):
        await AsyncCalculator.compute_factorial(-1)


# Testing async context managers
@pytest.mark.asyncio
async def test_data_service_context_manager():
    """Test AsyncDataService as async context manager."""
    async with AsyncDataService() as service:
        assert service.session is not None
        assert isinstance(service.session, aiohttp.ClientSession)

    # After exiting context, session should be closed
    assert service.session.closed


# Mocking async functions
@pytest.mark.asyncio
async def test_fetch_user_with_mock():
    """Test fetch_user with mocked HTTP response."""
    mock_response_data = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }

    with patch('aiohttp.ClientSession.get') as mock_get:
        # Create mock response
        mock_response = AsyncMock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None
        mock_response.__aenter__.return_value = mock_response
        mock_response.__aexit__.return_value = None

        mock_get.return_value = mock_response

        async with AsyncDataService() as service:
            result = await service.fetch_user(1)

            assert result == mock_response_data
            mock_get.assert_called_once_with("https://api.example.com/users/1")


@pytest.mark.asyncio
async def test_fetch_users_concurrent():
    """Test fetching multiple users concurrently."""
    users_data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]

    with patch('aiohttp.ClientSession.get') as mock_get:
        # Create mock responses for each user
        mock_responses = []
        for user_data in users_data:
            mock_response = AsyncMock()
            mock_response.json.return_value = user_data
            mock_response.raise_for_status.return_value = None
            mock_response.__aenter__.return_value = mock_response
            mock_response.__aexit__.return_value = None
            mock_responses.append(mock_response)

        mock_get.side_effect = mock_responses

        async with AsyncDataService() as service:
            results = await service.fetch_users([1, 2, 3])

            assert len(results) == 3
            assert results[0]["name"] == "Alice"
            assert results[1]["name"] == "Bob"
            assert results[2]["name"] == "Charlie"


@pytest.mark.asyncio
async def test_create_user_with_mock(sample_user_data):
    """Test create_user with mocked POST request."""
    created_user_data = {**sample_user_data, "id": 123}

    with patch('aiohttp.ClientSession.post') as mock_post:
        mock_response = AsyncMock()
        mock_response.json.return_value = created_user_data
        mock_response.raise_for_status.return_value = None
        mock_response.__aenter__.return_value = mock_response
        mock_response.__aexit__.return_value = None

        mock_post.return_value = mock_response

        async with AsyncDataService() as service:
            result = await service.create_user(sample_user_data)

            assert result["id"] == 123
            assert result["name"] == "John Doe"
            mock_post.assert_called_once()


# Testing file operations
@pytest.mark.asyncio
async def test_save_to_file(tmp_path):
    """Test async file saving."""
    test_data = {"test": "data", "number": 42}

    async with AsyncDataService() as service:
        filename = tmp_path / "test.json"
        await service.save_to_file(test_data, str(filename))

        # Verify file was created and contains correct data
        assert filename.exists()

        with open(filename, 'r') as f:
            saved_data = json.load(f)
            assert saved_data == test_data


@pytest.mark.asyncio
async def test_file_processor():
    """Test AsyncFileProcessor."""
    processor = AsyncFileProcessor()

    # Create a temporary file for testing
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        test_content = "Hello World\nThis is a test file\nWith multiple lines"
        f.write(test_content)
        temp_filename = f.name

    try:
        result = await processor.process_file(temp_filename)

        assert result["filename"] == temp_filename
        assert result["lines"] == 3
        assert result["words"] == 10
        assert result["characters"] == len(test_content)
        assert "Hello World" in result["content"]

    finally:
        os.unlink(temp_filename)


@pytest.mark.asyncio
async def test_process_multiple_files():
    """Test processing multiple files concurrently."""
    processor = AsyncFileProcessor()

    # Create temporary files
    import tempfile
    import os

    temp_files = []
    contents = [
        "File one content",
        "File two content\nwith multiple lines",
        "File three content\nline 2\nline 3"
    ]

    for i, content in enumerate(contents):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_files.append(f.name)

    try:
        results = await processor.process_multiple_files(temp_files)

        assert len(results) == 3
        assert results[0]["words"] == 3  # "File one content"
        assert results[1]["lines"] == 2  # Two lines
        assert results[2]["lines"] == 3  # Three lines

    finally:
        for filename in temp_files:
            os.unlink(filename)


@pytest.mark.asyncio
async def test_process_nonexistent_file():
    """Test processing a non-existent file."""
    processor = AsyncFileProcessor()

    with pytest.raises(FileNotFoundError):
        await processor.process_file("nonexistent_file.txt")


# Testing concurrent operations
@pytest.mark.asyncio
async def test_concurrent_calculations():
    """Test running multiple async calculations concurrently."""
    # Create multiple calculation tasks
    tasks = [
        AsyncCalculator.slow_add(1, 2, 0.1),
        AsyncCalculator.slow_multiply(3, 4, 0.1),
        AsyncCalculator.compute_factorial(5),
        AsyncCalculator.slow_add(10, 20, 0.1)
    ]

    start_time = asyncio.get_event_loop().time()
    results = await asyncio.gather(*tasks)
    end_time = asyncio.get_event_loop().time()

    # Verify results
    assert results[0] == 3  # 1 + 2
    assert results[1] == 12  # 3 * 4
    assert results[2] == 120  # 5!
    assert results[3] == 30  # 10 + 20

    # Should complete faster than sequential execution
    # (4 * 0.1) = 0.4 seconds sequential, concurrent should be ~0.1 seconds
    elapsed = end_time - start_time
    assert elapsed < 0.2  # Allow some margin for timing variations


# Async generator testing
async def async_range(n):
    """Simple async generator."""
    for i in range(n):
        yield i
        await asyncio.sleep(0.01)


@pytest.mark.asyncio
async def test_async_generator():
    """Test async generator."""
    values = []
    async for value in async_range(5):
        values.append(value)

    assert values == [0, 1, 2, 3, 4]


# Testing with timeouts
@pytest.mark.asyncio
async def test_async_with_timeout():
    """Test async operation with timeout."""
    async def slow_operation():
        await asyncio.sleep(0.5)
        return "done"

    # This should complete successfully
    result = await asyncio.wait_for(slow_operation(), timeout=1.0)
    assert result == "done"


@pytest.mark.asyncio
async def test_async_timeout_exceeded():
    """Test async operation that exceeds timeout."""
    async def very_slow_operation():
        await asyncio.sleep(2.0)
        return "done"

    # This should raise TimeoutError
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(very_slow_operation(), timeout=0.1)


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
