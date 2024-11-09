from typing import Callable

import numpy as np
import pytest

from tests.constants import ELEMENT_TYPE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_61 import i_test_data


@pytest.mark.parametrize(
    "matrix, angle, expected_matrix, _",
    i_test_data,
    ids=[i[-1] for i in i_test_data],
)
def test_rotate(
    decorated_function: Callable,
    matrix: np.ndarray,
    angle: int,
    expected_matrix: np.ndarray,
    _: str,
) -> None:
    returned_board = decorated_function(matrix, angle)

    assert np.issubdtype(returned_board.dtype, np.integer), ELEMENT_TYPE_ERROR
    assert isinstance(returned_board, np.ndarray), RETURN_TYPE_ERROR
    assert np.array_equal(returned_board, expected_matrix)
