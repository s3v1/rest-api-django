def fibonacci(n: int) -> int:
    """
    Calculate the nth number in the Fibonacci sequence.

    Args:
        n: The position in the sequence (0-based)

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci sequence not defined for negative numbers")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sequence(n: int) -> list[int]:
    """
    Generate a list of Fibonacci numbers up to the nth position.

    Args:
        n: The number of Fibonacci numbers to generate

    Returns:
        List of Fibonacci numbers

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Cannot generate negative number of terms")

    result = []
    if n > 0:
        result = [fibonacci(i) for i in range(n)]
    return result
