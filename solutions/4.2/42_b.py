from typing import List, Tuple, Union


def make_matrix(
    size: Union[Tuple[int], int], value: Union[int, None] = None
) -> List[List[int]]:
    if not value:
        value = 0
    if isinstance(size, int):
        size = (size, size)

    return [[value] * size[0] for _ in range(size[1])]
