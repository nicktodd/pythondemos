# Testing and Mocking Solutions

This directory contains complete solutions for the Python Testing and Mocking lab exercises. Use these as reference after completing the lab exercises in `../../labs/testing_and_mock/`.

## Solution Files

1. **calculator_tests.py** - Complete tests for Calculator class with comprehensive assertions
2. **user_service_tests.py** - Full implementation using fixtures and module-scoped fixtures
3. **validation_tests.py** - Parametrized tests with custom IDs and edge cases
4. **api_client_tests.py** - Mocking examples with various HTTP scenarios
5. **hamcrest_assertions.py** - Hamcrest matchers for expressive assertions
6. **async_service_tests.py** - Async testing with pytest-asyncio, timeouts, and cancellation
7. **ecommerce_integration.py** - Complete integration tests with SQLite database
8. **best_practices_example.py** - Best practices with test organization, builders, and performance tests

## Running Solutions

```bash
# Run all solution tests
pytest . -v

# Run specific solution
pytest calculator_tests.py -v

# Run with coverage
pytest . --cov=. --cov-report=html
```

## Key Concepts Demonstrated

- **Basic Testing**: Assertions, error testing, test discovery
- **Fixtures**: Function, module, and session-scoped fixtures
- **Parametrization**: @pytest.mark.parametrize with custom IDs
- **Mocking**: unittest.mock usage, patching, side effects, assertions
- **Hamcrest**: Collection, number, string, logical, and custom matchers
- **Async Testing**: pytest-asyncio, async fixtures, concurrent operations
- **Integration Testing**: Real databases, multiple component interactions
- **Best Practices**: Test organization, isolation, builders, performance testing

## Requirements

```bash
pip install pytest pyhamcrest pytest-asyncio requests aiohttp aiofiles
```

## Related Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [PyHamcrest Documentation](https://pyhamcrest.readthedocs.io/)
- [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- Demo files: `../../demos/testing_and_mock/`
- Lab instructions: `../../lab_instructions/testing_and_mock.md`
