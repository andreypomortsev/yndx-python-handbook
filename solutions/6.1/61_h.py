import numpy as np


def snake(width: int, height: int, direction: str = "H") -> np.ndarray:
    """
    Creates a matrix filled with numbers arranged in a "snake-like" pattern.

    The numbers increase sequentially, with every other row in reverse order
    to create a snake-like movement. The pattern can be generated in a
    horizontal ("H") or vertical ("V") direction.

    Arguments:
        width (int): The number of columns of the matrix.
        height (int): The number of rows of the matrix.
        direction (str, optional): The direction of the snake pattern.
                        "H" for horizontal (default), "V" for vertical.

    Returns:
        np.ndarray: A 2D NumPy array with the snake-like pattern.
    """
    flag = direction.upper() == "V"
    if flag:
        width, height = height, width

    base = np.arange(1, width + 1, dtype="int16")
    matrix = np.tile(base, (height, 1)) + (
        np.arange(height, dtype="int16")[:, np.newaxis] * width
    )
    matrix[1::2] = matrix[1::2, ::-1]

    return matrix.T if flag else matrix
