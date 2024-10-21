import numpy as np


def multiplication_matrix(size: int) -> np.ndarray:
    """
    Creates a 1D vector from 1 to size and then multiplies it by
    a 2D version of the vector to get a multiplication matrix.

    Arguments:
        size (int): Size of the vector.

    Returns:
        np.ndarray: Multiplication matrix of size (size x size).
    """
    vector = np.arange(1, size + 1)
    matrix = vector * vector[:, np.newaxis]

    return matrix
