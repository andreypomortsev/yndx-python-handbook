from typing import Callable

import numpy as np
import pytest

from tests.constants import ELEMENT_TYPE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_61 import f_test_data


@pytest.mark.parametrize(
    "size, expected_matrix, _",
    f_test_data,
    ids=[i[-1] for i in f_test_data],
)
def test_multiplication_matrix(
    decorated_function: Callable,
    size: int,
    expected_matrix: np.ndarray,
    _: str,
) -> None:
    returned_matrix = decorated_function(size)

    assert np.issubdtype(returned_matrix.dtype, np.integer), ELEMENT_TYPE_ERROR
    assert isinstance(returned_matrix, np.ndarray), RETURN_TYPE_ERROR
    assert np.array_equal(returned_matrix, expected_matrix)
