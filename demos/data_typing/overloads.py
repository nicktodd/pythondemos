from typing import overload

# ignored at runtime, used for type checking only
@overload
def greet(name: str) -> str:
    ...

# ignored at runtime, used for type checking only
@overload
def greet(name: str, times: int) -> str:
    ...

# actual implementation that will be executed at runtime, needs to handle all cases
def greet(name: str, times: int = 1) -> str:
    return " ".join([f"Hello, {name}!" for _ in range(times)])

# Usage examples:
print(greet("Alice"))         # Output: Hello, Alice!
print(greet("Bob", 3))        # Output: Hello, Bob! Hello, Bob! Hello, Bob!