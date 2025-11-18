def find_mountains(matrix: list) -> tuple:
    """
    Finds the indices of the mountains in the given matrix.

    Approach:
    - Iterates through interior cells (excluding borders) of the matrix
    - For each cell, compares its value against all 8 neighboring cells
    - If the center cell is greater than all neighbors, it's identified
      as a mountain
    - Uses an optimization: when a mountain is found, skips the next column
      since adjacent cells cannot both be mountains
    - Returns 1-indexed coordinates of all mountains found

    Args:
        matrix (list): A 2D list of heights.

    Returns:
        tuple: A tuple of indices of the mountains.
    """
    rows = len(matrix) - 1
    cols = len(matrix[0]) - 1
    mountains = []

    for i in range(1, rows):
        j = 1
        while j < cols:
            center = matrix[i][j]
            neighbors = [
                matrix[i + di][j + dj]
                for di in (-1, 0, 1)
                for dj in (-1, 0, 1)
                if not (di == dj == 0)
            ]

            if center > max(neighbors):
                mountains.append((i + 1, j + 1))
                j += 2
            else:
                j += 1

    return tuple(mountains)
