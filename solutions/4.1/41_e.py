__counter = 0


def click() -> None:
    """
    Increments the global counter variable.
    """
    global __counter
    __counter += 1


def get_count() -> int:
    """
    Returns the value of the global counter variable.
    """
    global __counter
    return __counter
