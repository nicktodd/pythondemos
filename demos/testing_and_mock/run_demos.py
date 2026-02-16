# filepath: d:\GitRepos\Courses\pythondemos\demos\testing_and_mock\run_demos.py
"""
Run Testing and Mocking Demos

This script runs all the testing and mocking demonstration files.
Each demo showcases different aspects of testing with pytest.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_demo(demo_file):
    """Run a single demo file."""
    print(f"\n{'='*60}")
    print(f"Running {demo_file}")
    print(f"{'='*60}")

    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest",
            demo_file,
            "-v",
            "--tb=short"
        ], capture_output=True, text=True, cwd=os.path.dirname(demo_file))

        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)

        return result.returncode == 0

    except Exception as e:
        print(f"Error running {demo_file}: {e}")
        return False


def main():
    """Run all demo files."""
    demo_dir = Path(__file__).parent

    # List of demo files in order of complexity
    demo_files = [
        "basic_pytest.py",
        "fixtures_demo.py",
        "parametrized_tests.py",
        "mocking_demo.py",
        "pyhamcrest_demo.py",
        "async_testing.py",
        "integration_testing.py",
        "best_practices.py"
    ]

    print("Testing and Mocking Demos")
    print("==========================")
    print(f"Running demos from: {demo_dir}")

    results = []

    for demo_file in demo_files:
        demo_path = demo_dir / demo_file
        if demo_path.exists():
            success = run_demo(str(demo_path))
            results.append((demo_file, success))
        else:
            print(f"Warning: {demo_file} not found")
            results.append((demo_file, False))

    # Summary
    print(f"\n{'='*60}")
    print("DEMO RUN SUMMARY")
    print(f"{'='*60}")

    passed = 0
    total = len(results)

    for demo_file, success in results:
        status = "PASSED" if success else "FAILED"
        print("30")
        if success:
            passed += 1

    print(f"\nTotal: {passed}/{total} demos passed")

    if passed == total:
        print("🎉 All demos completed successfully!")
        return 0
    else:
        print("❌ Some demos failed. Check output above for details.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
