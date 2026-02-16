#!/usr/bin/env python3
"""
Exception Handling Demos Runner

This script runs all the exception handling demonstration files.
"""

import sys
import os

# Add the current directory to the path so we can import the demo modules
sys.path.insert(0, os.path.dirname(__file__))

def run_demo(demo_name, description):
    """Run a single demo with proper formatting"""
    print(f"\n{'='*60}")
    print(f"Running: {demo_name}")
    print(f"Description: {description}")
    print('='*60)

    try:
        # Import and run the demo
        module = __import__(demo_name)
        if hasattr(module, '__main__'):
            # If the module has its own main block, it will run automatically
            pass
        print(f"✓ {demo_name} completed successfully")
    except Exception as e:
        print(f"✗ Error running {demo_name}: {e}")
    finally:
        print()

def main():
    """Run all exception handling demos"""
    print("Python Exception Handling Demos")
    print("This collection demonstrates various exception handling concepts in Python.\n")

    demos = [
        ("basic_try_except", "Basic try-except blocks for handling exceptions"),
        ("multiple_exceptions", "Handling multiple exception types with specific except blocks"),
        ("finally_block", "Using finally blocks for cleanup operations"),
        ("raise_exceptions", "Raising exceptions and re-raising with context"),
        ("custom_exceptions", "Creating and using custom exception classes"),
        ("exception_chaining", "Exception chaining with 'raise from' syntax"),
        ("context_managers", "Using context managers for resource management"),
        ("best_practices", "Best practices for exception handling")
    ]

    for demo_name, description in demos:
        run_demo(demo_name, description)

    print("All demos completed!")
    print("\nKey concepts covered:")
    print("- Basic try/except/else/finally blocks")
    print("- Multiple exception handling")
    print("- Raising and re-raising exceptions")
    print("- Custom exception classes")
    print("- Exception chaining")
    print("- Context managers for resource cleanup")
    print("- Best practices and common pitfalls")

if __name__ == "__main__":
    main()
