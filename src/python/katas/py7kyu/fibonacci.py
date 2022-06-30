def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(abs(n)):
        a, b = b, a + b

    return a
