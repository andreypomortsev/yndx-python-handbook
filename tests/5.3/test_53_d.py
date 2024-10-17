from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests import utils
from tests.conftest import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_53 import d_test_data


@pytest.mark.parametrize(
    "numbers, expected_error, _",
    d_test_data["Errors"],
    ids=[i[-1] for i in d_test_data["Errors"]],
)
def test_only_positive_even_sum_error(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    numbers: Tuple[int | float | str, int | float | str],
    expected_error: Exception,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    with pytest.raises(expected_error) as info:
        solution_module.only_positive_even_sum(*numbers)

    assert expected_error.__name__ == info.type.__name__


@pytest.mark.parametrize(
    "numbers, expected, _",
    d_test_data["Values"],
    ids=[i[-1] for i in d_test_data["Values"]],
)
def test_only_positive_even_sum(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    numbers: Tuple[int, int],
    expected: int,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(
        solution.only_positive_even_sum
    )
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned = decorated_func(*numbers)

    assert returned == expected
