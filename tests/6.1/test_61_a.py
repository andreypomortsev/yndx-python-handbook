from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests import utils
from tests.data.test_data_61 import a_test_data


@pytest.mark.parametrize(
    "coefficients, expected_error, _",
    a_test_data["Errors"],
    ids=[i[-1] for i in a_test_data["Errors"]],
)
def test_find_roots_error(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    coefficients: Tuple[int | float, int | float, int | float],
    expected_error: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    with pytest.raises(Exception) as exc_info:
        solution_module.find_roots(*coefficients)

    assert expected_error == exc_info.type.__name__


@pytest.mark.parametrize(
    "coefficients, expected_return, _",
    a_test_data["Values"],
    ids=[i[-1] for i in a_test_data["Values"]],
)
def test_find_roots(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    coefficients: Tuple[int | float, int | float, int | float],
    expected_return: Tuple[float, float],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    returned = solution_module.find_roots(*coefficients)

    for returned_root, expexted_root in zip(returned, expected_return):
        assert round(returned_root, 2) == expexted_root

