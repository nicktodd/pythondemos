# run_demos.py
# Main file to run all class and object demos

import basic_class
import static_methods
import operator_overloading
import str_repr
import inheritance
import multiple_inheritance

if __name__ == "__main__":
    print("="*60)
    print("PYTHON CLASSES AND OBJECTS DEMOS")
    print("="*60)

    print("\n1. BASIC CLASS DEMO")
    print("-" * 30)
    # The basic_class.py has its own main block, but we can call it
    # Since it's in if __name__ == "__main__", we need to import and run
    # Actually, better to have functions in each file and call them

    # For simplicity, since each has if __name__, we can just mention they run separately
    print("Run 'python basic_class.py' to see basic class demo")

    print("\n2. STATIC METHODS DEMO")
    print("-" * 30)
    print("Run 'python static_methods.py' to see static and class methods")

    print("\n3. OPERATOR OVERLOADING DEMO")
    print("-" * 30)
    print("Run 'python operator_overloading.py' to see operator overloading")

    print("\n4. __STR__ AND __REPR__ DEMO")
    print("-" * 30)
    print("Run 'python str_repr.py' to see string representations")

    print("\n5. INHERITANCE DEMO")
    print("-" * 30)
    print("Run 'python inheritance.py' to see single inheritance")

    print("\n6. MULTIPLE INHERITANCE DEMO")
    print("-" * 30)
    print("Run 'python multiple_inheritance.py' to see multiple inheritance")

    print("\n" + "="*60)
    print("Each demo file can be run independently.")
    print("They demonstrate key OOP concepts in Python.")
    print("="*60)
