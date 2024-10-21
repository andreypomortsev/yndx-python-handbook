from types import ModuleType
from typing import Callable, Optional, Tuple

import numpy as np
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_61 import h_test_data


@pytest.mark.parametrize(
    "sizes, direction, expected_matrix, _",
    h_test_data,
    ids=[i[-1] for i in h_test_data],
)
def test_snake(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    sizes: Tuple[int, int],
    direction: Optional[str],
    expected_matrix: np.ndarray,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.snake)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    if direction:
        returned_board = decorated_func(*sizes, direction)
    else:
        returned_board = decorated_func(*sizes)

    type_err = "The function should return a numpy array of int16 elements"
    assert np.issubdtype(returned_board.dtype, np.int16), type_err

    type_err = "The function should return a numpy array"
    assert isinstance(returned_board, np.ndarray), type_err

    assert np.array_equal(returned_board, expected_matrix)
