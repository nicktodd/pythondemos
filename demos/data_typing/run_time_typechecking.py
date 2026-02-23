from typeguard import typechecked

@typechecked
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

print(greet("Nick", "50"))  # Raises TypeError at runtime