from typing import Callable

import numpy as np
import pytest

from tests.constants import RETURN_TYPE_ERROR
from tests.data.test_data_61 import j_test_data


@pytest.mark.parametrize(
    "one_d_array, expected_matrix, _",
    j_test_data,
    ids=[i[-1] for i in j_test_data],
)
def test_stairs(
    decorated_function: Callable,
    one_d_array: np.ndarray,
    expected_matrix: np.ndarray,
    _: str,
) -> None:
    returned_board = decorated_function(one_d_array)

    assert isinstance(returned_board, np.ndarray), RETURN_TYPE_ERROR
    assert np.array_equal(returned_board, expected_matrix)
