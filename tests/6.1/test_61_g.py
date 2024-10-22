from types import ModuleType
from typing import Callable

import numpy as np
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_61 import g_test_data


@pytest.mark.parametrize(
    "size, expected_matrix, _",
    g_test_data,
    ids=[i[-1] for i in g_test_data],
)
def test_make_board(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    size: int,
    expected_matrix: np.ndarray,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.make_board)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned_board = decorated_func(size)

    type_err = "The function should return a numpy array of integer elements"
    assert np.issubdtype(returned_board.dtype, np.integer), type_err

    type_err = "The function should return a numpy array"
    assert isinstance(returned_board, np.ndarray), type_err

    assert np.array_equal(returned_board, expected_matrix)