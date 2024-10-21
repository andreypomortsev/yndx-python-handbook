from types import ModuleType
from typing import Callable

import numpy as np
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_61 import f_test_data


@pytest.mark.parametrize(
    "size, expected_matrix, _",
    f_test_data,
    ids=[i[-1] for i in f_test_data],
)
def test_multiplication_matrix(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    size: int,
    expected_matrix: np.array,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(
        solution.multiplication_matrix
    )
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned_matrix = decorated_func(size)

    assert np.array_equal(returned_matrix, expected_matrix)
