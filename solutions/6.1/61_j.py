import numpy as np


def stairs(row: np.array) -> np.ndarray:
    """
    Creates a 2D array where each row is a right-shifted version of
    the input array.

    This function generates a "stair-step" effect by using modular arithmetic
    to shift the input array to the right for each subsequent row.
    The first row is the original array, the second row is the array shifted
    by one position to the right, and so on, wrapping around to
    the start of the array.

    Args:
        row (np.array): A 1D NumPy array to be shifted.

    Returns:
        np.ndarray: A 2D NumPy array containing shifted versions of
            the input array. The output array will have the same number of
            rows as the input array and the same number of columns as
            the input array.
    """
    n = row.shape[0]
    return np.array([row[(np.arange(n) - i)] for i in range(n)])
