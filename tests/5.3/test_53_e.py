from types import ModuleType
from typing import Callable, List, Tuple

import pytest

from tests import utils
from tests.data.test_data_53 import e_test_data


@pytest.mark.parametrize(
    "iterables, error, _",
    e_test_data["Errors"],
    ids=[i[-1] for i in e_test_data["Errors"]],
)
def test_merge_error(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    iterables: Tuple[int | float, int | float],
    error: Exception,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    with pytest.raises(error) as info:
        solution_module.merge(*iterables)

    assert error.__name__ == info.type.__name__


@pytest.mark.parametrize(
    "numbers, expected, _",
    e_test_data["Values"],
    ids=[i[-1] for i in e_test_data["Values"]],
)
def test_merge(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    numbers: Tuple[List[int] | Tuple[int], List[float] | Tuple[float]],
    expected: Tuple[float] | Tuple[int],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    returned = solution_module.merge(*numbers)

    assert returned == list(expected)
