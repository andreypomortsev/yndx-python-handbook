from types import ModuleType
from typing import Callable

import pytest

from tests import utils
from tests.conftest import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_53 import h_test_data


@pytest.mark.parametrize(
    "name, expected_error, _",
    h_test_data["Errors"],
    ids=[i[-1] for i in h_test_data["Errors"]],
)
def test_username_validation_error(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    name: str,
    expected_error: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    with pytest.raises(Exception) as exc_info:
        solution_module.username_validation(name)

    assert expected_error == exc_info.type.__name__


@pytest.mark.parametrize(
    "name, expected_return, _",
    h_test_data["Values"],
    ids=[i[-1] for i in h_test_data["Values"]],
)
def test_username_validation(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    name: str,
    expected_return: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(
        solution.username_validation
    )
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned = decorated_func(name)

    assert returned == expected_return
