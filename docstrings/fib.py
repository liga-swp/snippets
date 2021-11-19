def fib(n):
    """Returns the n'th fibonacci number (0 based), starting with 1, 1, 2, …."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
