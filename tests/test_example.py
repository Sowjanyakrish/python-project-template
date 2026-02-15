"""
Comprehensive test suite for the example module.

This module demonstrates various pytest patterns including:
- Basic assertions
- Parametrized tests
- Exception testing
- Proper test documentation
"""

import pytest

from src.example import add, greet, is_even


def test_add() -> None:
    """
    Test the add function with various numeric inputs.

    Tests basic addition with positive, negative, and decimal numbers.
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(-5, -3) == -8


def test_add_with_floats() -> None:
    """
    Test the add function specifically with floating-point numbers.

    Ensures proper handling of decimal arithmetic.
    """
    result = add(0.1, 0.2)
    assert abs(result - 0.3) < 1e-9  # Account for floating-point precision


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (1, 1, 2),
        (10, 5, 15),
        (-10, 10, 0),
        (100, 200, 300),
    ],
)
def test_add_parametrized(a: float, b: float, expected: float) -> None:
    """
    Test the add function with parametrized inputs.

    This demonstrates pytest's parametrize feature for testing
    multiple input combinations efficiently.
    """
    assert add(a, b) == expected


def test_greet() -> None:
    """
    Test the greet function with various names.

    Ensures proper string formatting in greeting messages.
    """
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("World") == "Hello, World!"
    assert greet("") == "Hello, !"


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("Charlie", "Hello, Charlie!"),
        ("123", "Hello, 123!"),
    ],
)
def test_greet_parametrized(name: str, expected: str) -> None:
    """
    Test the greet function with parametrized names.

    Demonstrates testing string functions with various inputs.
    """
    assert greet(name) == expected


def test_is_even() -> None:
    """
    Test the is_even function with various integers.

    Tests positive, negative, zero, and edge cases.
    """
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(4) is True
    assert is_even(-2) is True
    assert is_even(-4) is True
    assert is_even(1) is False
    assert is_even(3) is False
    assert is_even(-1) is False
    assert is_even(-3) is False


@pytest.mark.parametrize(
    "number,expected",
    [
        (0, True),
        (2, True),
        (4, True),
        (100, True),
        (-2, True),
        (1, False),
        (3, False),
        (99, False),
        (-1, False),
    ],
)
def test_is_even_parametrized(number: int, expected: bool) -> None:
    """
    Test the is_even function with parametrized inputs.

    Covers a wide range of even and odd numbers.
    """
    assert is_even(number) == expected


def test_add_with_strings_should_fail() -> None:
    """
    Test that add function with incompatible types raises TypeError.

    This demonstrates pytest's exception testing capabilities.
    While add() works with strings (concatenation), it fails when
    trying to add incompatible types like numbers and strings.
    """
    with pytest.raises(TypeError):
        add(5, "world")  # type: ignore

    with pytest.raises(TypeError):
        add("hello", 5)  # type: ignore

    with pytest.raises(TypeError):
        add(10, [1, 2, 3])  # type: ignore


def test_greet_with_non_string_should_work() -> None:
    """
    Test that greet function handles non-string inputs gracefully.

    Python's f-strings will convert most types to strings,
    so this should work without raising an exception.
    """
    # These should work due to Python's string conversion
    result = greet(123)  # type: ignore
    assert "123" in result
