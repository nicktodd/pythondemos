"""
Async Python Demos Runner

This script runs all async Python demonstration modules in sequence,
showcasing various asynchronous programming concepts and patterns.
"""

import asyncio
import sys
import time
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Import demo modules
from basic_async_await import main as basic_main
from coroutines_tasks import main as coroutines_main
from concurrent_execution import main as concurrent_main
from async_context_managers import main as context_managers_main
from async_iterators import main as iterators_main
from error_handling import main as error_handling_main
from real_world_examples import main as real_world_main
from best_practices import main as best_practices_main


async def run_demo(name: str, demo_func):
    """Run a single demo with timing and error handling"""
    print(f"\n{'='*60}")
    print(f"Running {name} Demo")
    print('='*60)

    start_time = time.time()
    try:
        await demo_func()
        elapsed = time.time() - start_time
        print(f"Demo completed in {elapsed:.2f}s")
        print("-" * 60)
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"Demo failed after {elapsed:.2f}s")
        print(f"Error details: {e}")
        print("-" * 60)


async def main():
    """Run all async Python demos"""
    print("Async Python Comprehensive Demos")
    print("=================================")
    print("This script will run all async Python demonstration modules.")
    print("Each demo showcases different aspects of asynchronous programming.\n")

    # Define demos to run
    demos = [
        ("Basic Async/Await", basic_main),
        ("Coroutines and Tasks", coroutines_main),
        ("Concurrent Execution", concurrent_main),
        ("Async Context Managers", context_managers_main),
        ("Async Iterators", iterators_main),
        ("Error Handling", error_handling_main),
        ("Real World Examples", real_world_main),
        ("Best Practices", best_practices_main),
    ]

    total_start_time = time.time()

    # Run all demos
    for name, demo_func in demos:
        await run_demo(name, demo_func)

        # Brief pause between demos
        await asyncio.sleep(0.5)

    total_elapsed = time.time() - total_start_time

    print(f"\n{'='*60}")
    print("All Async Python Demos Completed!")
    print(f"Total time: {total_elapsed:.2f}s")
    print("="*60)

    # Summary
    print("\nDemo Summary:")
    print("- Basic Async/Await: Core async/await syntax and patterns")
    print("- Coroutines and Tasks: Task lifecycle, creation, and management")
    print("- Concurrent Execution: Running multiple operations concurrently")
    print("- Async Context Managers: Resource management in async code")
    print("- Async Iterators: Asynchronous iteration patterns")
    print("- Error Handling: Exception handling and cancellation in async code")
    print("- Real World Examples: Practical applications of async programming")
    print("- Best Practices: Performance optimization and robust async patterns")

    print("\nKey Concepts Demonstrated:")
    print("- asyncio event loop and coroutines")
    print("- Task creation and lifecycle management")
    print("- Concurrent execution with gather/as_completed")
    print("- Resource management with async context managers")
    print("- Asynchronous iteration with async generators")
    print("- Error handling, cancellation, and timeouts")
    print("- Rate limiting and producer-consumer patterns")
    print("- Performance optimization techniques")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nDemo execution interrupted by user.")
    except Exception as e:
        print(f"\n\nUnexpected error during demo execution: {e}")
        sys.exit(1)
