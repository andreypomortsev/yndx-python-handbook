from typing import Callable, Optional, Tuple

import numpy as np
import pytest

from tests.constants import ELEMENT_TYPE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_61 import h_test_data


@pytest.mark.parametrize(
    "sizes, direction, expected_array, _",
    h_test_data,
    ids=[i[-1] for i in h_test_data],
)
def test_snake(
    decorated_function: Callable,
    sizes: Tuple[int, int],
    direction: Optional[str],
    expected_array: np.ndarray,
    _: str,
) -> None:
    if direction:
        returned_array = decorated_function(*sizes, direction)
    else:
        returned_array = decorated_function(*sizes)

    assert np.issubdtype(returned_array.dtype, np.int16), ELEMENT_TYPE_ERROR
    assert isinstance(returned_array, np.ndarray), RETURN_TYPE_ERROR
    assert np.array_equal(returned_array, expected_array)
