from typing import Callable

import numpy as np
import pytest

from tests.constants import ELEMENT_TYPE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_61 import g_test_data


@pytest.mark.parametrize(
    "size, expected_board, _",
    g_test_data,
    ids=[i[-1] for i in g_test_data],
)
def test_make_board(
    decorated_function: Callable,
    size: int,
    expected_board: np.ndarray,
    _: str,
) -> None:
    returned_board = decorated_function(size)

    assert np.issubdtype(returned_board.dtype, np.integer), ELEMENT_TYPE_ERROR
    assert isinstance(returned_board, np.ndarray), RETURN_TYPE_ERROR
    assert np.array_equal(returned_board, expected_board)
