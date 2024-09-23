def fibonacci(num):
    if not num:
        return
    if num < 2:
        yield 0
    else:
        a, b = 0, 1
        yield a
        yield b
        for _ in range(num - 2):
            a, b = b, a + b
            yield b
