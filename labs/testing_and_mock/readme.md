<!-- filepath: d:\GitRepos\Courses\pythondemos\lab_instructions\testing_and_mock.md -->
# Python Testing and Mocking Lab

This lab will guide you through implementing comprehensive unit tests and mocking techniques using pytest and pyhamcrest. You'll build upon the concepts demonstrated in the `demos/testing_and_mock/` folder and learn how to write effective, maintainable tests.

## Prerequisites

Before starting, review the demo files in `demos/testing_and_mock/` to understand the concepts:

- `basic_pytest.py` - Basic pytest usage, assertions, and test discovery
- `fixtures_demo.py` - Pytest fixtures for setup and teardown
- `parametrized_tests.py` - Parametrized tests with @pytest.mark.parametrize
- `mocking_demo.py` - Mocking with unittest.mock and patching
- `pyhamcrest_demo.py` - Expressive assertions with pyhamcrest matchers
- `async_testing.py` - Testing asynchronous code with pytest-asyncio
- `integration_testing.py` - Integration testing multiple components
- `best_practices.py` - Testing best practices and organization

## Lab Structure

- **Starter files**: Located in `labs/testing_and_mock/`
- **Solutions**: Located in `solutions/testing_and_mock/` (check after completing exercises)
- **Your work**: Modify the starter files in `labs/testing_and_mock/`

## Exercise 1: Basic Pytest and Calculator Testing

**File**: `labs/testing_and_mock/calculator_tests.py`

Create comprehensive tests for a Calculator class:

1. Create a `Calculator` class with methods: `add`, `subtract`, `multiply`, `divide`, `power`, `square_root`
2. Write tests for all basic operations
3. Test error conditions (division by zero, negative square root)
4. Use appropriate assertions and error testing
5. Run tests with `pytest calculator_tests.py -v`

**Expected structure**:
```python
class Calculator:
    def add(self, a, b):
        return a + b
    # ... other methods

# Test functions
def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    # ... more test cases
```

## Exercise 2: Pytest Fixtures and User Management

**File**: `labs/testing_and_mock/user_service_tests.py`

Implement tests using fixtures for a user management system:

1. Create a `UserService` class with methods: `create_user`, `get_user`, `update_user`, `delete_user`
2. Create a `Database` mock class for testing
3. Use function-scoped fixtures for database setup
4. Use module-scoped fixtures for shared resources
5. Test user CRUD operations with proper setup/teardown

**Test your implementation**:
```python
@pytest.fixture
def db_mock():
    # Setup mock database
    return MockDatabase()

@pytest.fixture
def user_service(db_mock):
    return UserService(db_mock)

def test_create_user(user_service, db_mock):
    user_id = user_service.create_user("john", "john@example.com")
    assert user_id is not None
    # Verify database calls
```

## Exercise 3: Parametrized Tests and Data Validation

**File**: `labs/testing_and_mock/validation_tests.py`

Create parametrized tests for data validation functions:

1. Create validation functions: `validate_email`, `validate_password`, `validate_age`
2. Use `@pytest.mark.parametrize` for multiple test cases
3. Test both valid and invalid inputs
4. Use custom test IDs for better readability
5. Include edge cases and boundary conditions

**Example test cases**:
```python
@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("invalid-email", False),
    ("", False),
    ("user@", False),
])
def test_validate_email(email, expected):
    assert validate_email(email) == expected
```

## Exercise 4: Mocking External Dependencies

**File**: `labs/testing_and_mock/api_client_tests.py`

Test an API client using mocking techniques:

1. Create an `APIClient` class that makes HTTP requests
2. Create methods: `get_user`, `create_post`, `get_weather`
3. Mock `requests.get` and `requests.post` calls
4. Test success and error scenarios
5. Verify correct API calls are made

**Test structure**:
```python
def test_get_user_with_mock():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"id": 1, "name": "John"}
        client = APIClient()
        result = client.get_user(1)
        assert result["name"] == "John"
        mock_get.assert_called_once()
```

## Exercise 5: PyHamcrest Matchers

**File**: `labs/testing_and_mock/hamcrest_assertions.py`

Rewrite tests using pyhamcrest matchers for more expressive assertions:

1. Take your calculator tests and rewrite using hamcrest matchers
2. Use collection matchers for list/dict assertions
3. Use number matchers for numeric comparisons
4. Use string matchers for text validation
5. Create custom matchers if needed

**Example**:
```python
from hamcrest import assert_that, equal_to, close_to, has_length

def test_calculator_with_hamcrest(calc):
    assert_that(calc.add(2, 3), equal_to(5))
    assert_that(calc.divide(10, 3), close_to(3.33, 0.01))
```

## Exercise 6: Async Testing

**File**: `labs/testing_and_mock/async_service_tests.py`

Test asynchronous service methods:

1. Create an `AsyncDataProcessor` class with async methods
2. Implement async methods: `process_data`, `fetch_multiple_items`, `save_results`
3. Use `@pytest.mark.asyncio` decorator
4. Mock async external calls
5. Test concurrent operations and error handling

**Async test example**:
```python
@pytest.mark.asyncio
async def test_process_data():
    processor = AsyncDataProcessor()
    result = await processor.process_data({"input": "test"})
    assert result["status"] == "processed"
```

## Exercise 7: Integration Testing

**File**: `labs/testing_and_mock/ecommerce_integration.py`

Create integration tests for an e-commerce system:

1. Create classes: `UserManager`, `ProductCatalog`, `OrderProcessor`, `EmailService`
2. Test the complete order flow from user registration to order confirmation
3. Use real database connections (SQLite for testing)
4. Mock external services like email and payment
5. Test error scenarios and edge cases

**Integration test structure**:
```python
def test_complete_order_flow(user_manager, order_processor, email_service):
    # Register user
    # Add products to cart
    # Process payment
    # Send confirmation email
    # Verify order in database
    pass
```

## Exercise 8: Best Practices Implementation

**File**: `labs/testing_and_mock/best_practices_example.py`

Apply testing best practices to a complex system:

1. Organize tests into classes by component
2. Use fixtures for proper test isolation
3. Implement test data builders
4. Add performance tests where appropriate
5. Use custom markers for different test types
6. Ensure comprehensive error condition testing

**Best practices structure**:
```python
class TestUserManagement:
    @pytest.fixture
    def user_builder(self):
        return UserBuilder()

    def test_user_creation_success(self, user_manager, user_builder):
        user_data = user_builder.with_email("test@example.com").build()
        # Test implementation
        pass

@pytest.mark.performance
def test_bulk_operations_performance():
    # Performance test
    pass
```

## Running the Tests

Run all tests with:
```bash
pytest labs/testing_and_mock/ -v
```

Run specific test files:
```bash
pytest labs/testing_and_mock/calculator_tests.py -v
```

Run with coverage:
```bash
pytest labs/testing_and_mock/ --cov=. --cov-report=html
```

## Test Requirements

Make sure you have the required packages installed:
```bash
pip install pytest pyhamcrest pytest-asyncio requests
```

## Learning Objectives

By completing this lab, you will learn:

1. How to write comprehensive unit tests with pytest
2. Effective use of fixtures for test setup and teardown
3. Parametrized testing for multiple test cases
4. Mocking techniques for external dependencies
5. Expressive assertions with pyhamcrest
6. Testing asynchronous code
7. Integration testing approaches
8. Testing best practices and organization

## Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [PyHamcrest Documentation](https://pyhamcrest.readthedocs.io/)
- [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- [Testing Best Practices](https://docs.python-guide.org/writing/tests/)
