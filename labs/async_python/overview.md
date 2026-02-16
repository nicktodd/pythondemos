# Async Python Lab Exercises

This directory contains starter files for the Async Python programming lab. Each exercise builds upon the concepts demonstrated in the `demos/async_python/` folder.

## Lab Structure

- `basic_async_await.py` - Basic async/await patterns
- `coroutines_tasks.py` - Coroutines and task management
- `concurrent_execution.py` - Concurrent execution patterns
- `async_context_managers.py` - Async context managers
- `async_iterators.py` - Async iterators and generators
- `error_handling.py` - Error handling in async code
- `real_world_examples.py` - Real-world async applications

## Getting Started

1. Review the corresponding demo files in `demos/async_python/` to understand the concepts
2. Read the lab instructions in `lab_instructions/async_python.md`
3. Complete each exercise by implementing the TODO sections in the starter files
4. Test your implementations using the provided test cases
5. Compare your solutions with the completed versions in `solutions/async_python/`

## Prerequisites

- Python 3.7+
- asyncio module (built-in)
- Basic understanding of async/await concepts

## Tips

- Start with Exercise 1 and progress sequentially
- Use `asyncio.run()` to execute your async functions
- Test frequently as you implement each function
- Remember that async code is concurrent, not parallel
- Handle exceptions properly in async contexts

## Testing Your Solutions

Each exercise includes test code that you can run to verify your implementation:

```python
# Example test run
python basic_async_await.py
```

## Next Steps

After completing all exercises, check your solutions against the provided answers in `solutions/async_python/` and run the comprehensive demo suite with:

```python
python demos/async_python/run_demos.py
```
