# welcomemessage


def say_hello(name: str) -> str:
    """Return a greeting message to students in the IDS class."""
    return f"Hello, {name}, welcome to Data Engineering Systems (IDS 706)!"


# showingsubtraction


def sub(a: int, b: int) -> int:
    """Return the subtraction of two numbers."""
    return a - b


# showingaddition


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(say_hello("Shambhavi Khanna"))
    print("10 - 8 =", sub(10, 8))
    print("5 + 5 =", add(5, 5))
