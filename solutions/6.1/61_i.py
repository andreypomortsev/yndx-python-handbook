import numpy as np


def rotate(matrix: np.ndarray, angle: int) -> np.ndarray:
    """
    Rotates a given matrix by a specified angle in degrees.

    The function rotates the matrix counterclockwise if the angle is positive
    and clockwise if the angle is negative. The angle should be a multiple
    of 90 degrees (e.g., -90, 90, 180, 270). The rotation is performed
    using NumPy's `rot90` function.

    Args:
        matrix (np.ndarray): The input matrix to be rotated.
        angle (int): The rotation angle in degrees. Must be a multiple of 90.

    Returns:
        np.ndarray: The rotated matrix.
    """
    k = angle // 90
    return np.rot90(matrix, k=-k)
