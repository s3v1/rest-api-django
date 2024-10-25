import pytest
from app.fibonacci import fibonacci, fibonacci_sequence


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_small_numbers():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5


def test_fibonacci_larger_number():
    assert fibonacci(7) == 13


def test_fibonacci_negative_number():
    with pytest.raises(
        ValueError, match="Fibonacci sequence not defined for negative numbers"
    ):
        fibonacci(-1)


def test_fibonacci_sequence_empty():
    assert fibonacci_sequence(0) == []


def test_fibonacci_sequence_one():
    assert fibonacci_sequence(1) == [0]


def test_fibonacci_sequence_multiple():
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]


def test_fibonacci_sequence_negative():
    with pytest.raises(ValueError, match="Cannot generate negative number of terms"):
        fibonacci_sequence(-1)
