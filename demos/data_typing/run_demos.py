"""
Data Typing Demos Runner
========================

This script runs all the data typing demonstration files in sequence.
Each demo showcases different aspects of type hints and type checking in Python.
"""

import sys
import os
import subprocess
import importlib.util

# List of demo files to run
DEMOS = [
    ("basic_type_hints", "Basic type hints for variables and functions"),
    ("collections_typing", "Type hints with collections (List, Dict, Tuple, Set)"),
    ("optional_union", "Optional and Union types for flexibility"),
    ("custom_types", "Custom types, type aliases, and advanced structures"),
    ("advanced_typing", "Generics, protocols, and type variables"),
    ("type_checking", "Runtime type checking and validation"),
    ("best_practices", "Best practices for effective type hinting")
]

def run_demo(demo_name: str, description: str) -> bool:
    """Run a single demo file."""
    print("=" * 60)
    print(f"Running: {demo_name}")
    print(f"Description: {description}")
    print("=" * 60)

    try:
        # Import and run the demo module
        spec = importlib.util.spec_from_file_location(
            demo_name,
            os.path.join(os.path.dirname(__file__), f"{demo_name}.py")
        )

        if spec is None or spec.loader is None:
            print(f"✗ Failed to load {demo_name}")
            return False

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # If the module has a main function, call it
        if hasattr(module, 'main'):
            module.main()
        else:
            print(f"✓ {demo_name} loaded successfully (no main function)")

        print(f"✓ {demo_name} completed successfully")
        return True

    except Exception as e:
        print(f"✗ {demo_name} failed with error: {e}")
        return False

def main():
    """Run all data typing demos."""
    print("Python Data Typing Demos")
    print("This collection demonstrates various type hinting concepts in Python.")
    print("=" * 60)
    print()

    successful_demos = 0
    total_demos = len(DEMOS)

    for demo_name, description in DEMOS:
        success = run_demo(demo_name, description)
        if success:
            successful_demos += 1
        print()  # Add blank line between demos

    print("=" * 60)
    print(f"Demo Summary: {successful_demos}/{total_demos} demos completed successfully")
    print()

    if successful_demos == total_demos:
        print("🎉 All demos completed successfully!")
        print()
        print("Key concepts covered:")
        print("- Basic type hints (int, str, float, bool)")
        print("- Collection types (List, Dict, Tuple, Set)")
        print("- Optional and Union types")
        print("- Custom types and type aliases")
        print("- Generic types and protocols")
        print("- Runtime type checking")
        print("- Best practices for type hinting")
        print()
        print("Next steps:")
        print("1. Review the lab exercises in lab_instructions/data_typing.md")
        print("2. Complete the starter files in labs/data_typing/")
        print("3. Check your solutions against solutions/data_typing/")
        print("4. Try using mypy for static type checking: pip install mypy && mypy your_file.py")
    else:
        print(f"⚠️  {total_demos - successful_demos} demo(s) failed. Check the output above for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
