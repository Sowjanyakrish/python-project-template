"""
Example module demonstrating basic Python functions with type hints and docstrings.

This module provides simple example functions to demonstrate proper Python
code structure, documentation, and testing patterns.
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers together.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b


def greet(name: str) -> str:
    """
    Generate a greeting message for a given name.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string.

    Examples:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet("World")
        'Hello, World!'
    """
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    """
    Check if a number is even.

    Args:
        number: The integer to check.

    Returns:
        True if the number is even, False otherwise.

    Examples:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
        >>> is_even(0)
        True
        >>> is_even(-2)
        True
    """
    return number % 2 == 0
