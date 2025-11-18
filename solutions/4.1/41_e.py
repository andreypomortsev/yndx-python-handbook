_counter = 0


def click() -> None:
    """
    Increments the global counter variable.
    """
    global _counter
    _counter += 1


def get_count() -> int:
    """
    Returns the value of the global counter variable.
    """
    return _counter
