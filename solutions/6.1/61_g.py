import numpy as np


def make_board(size: int) -> np.ndarray:
    """
    Creates a square board of given size filled with a checkerboard pattern.

    The board is initialized with zeros, and the positions corresponding
    to a checkerboard pattern are set to 1. Specifically, the cells at
    even row and column indices, as well as odd row and column indices,
    are filled with 1s.

    Arguments:
        size (int): The size of the board (number of rows and columns).

    Returns:
        np.ndarray: A 2D NumPy array of shape (size, size) representing
        the checkerboard pattern, with values of 1 at the appropriate
        positions and 0 elsewhere.
    """
    board = np.zeros((size, size), dtype="int8")
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1

    return board
