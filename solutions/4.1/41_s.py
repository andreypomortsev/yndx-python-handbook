def swap(a: list, b: list) -> None:
    """
    Swaps the contents of two lists in place.

    Args:
        a (list): The first list to swap.
        b (list): The second list to swap.
    """
    a[:], b[:] = b[:], a[:]
