from types import ModuleType
from typing import Callable

import pytest

from tests import utils
from tests.data.test_data_53 import g_test_data


@pytest.mark.parametrize(
    "name, expected_error, _",
    g_test_data["Errors"],
    ids=[i[-1] for i in g_test_data["Errors"]],
)
def test_name_validation_error(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    name: str,
    expected_error: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    with pytest.raises(Exception) as exc_info:
        solution_module.name_validation(name)

    assert expected_error == exc_info.type.__name__


@pytest.mark.parametrize(
    "name, expected_return, _",
    g_test_data["Values"],
    ids=[i[-1] for i in g_test_data["Values"]],
)
def test_name_validation(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    name: str,
    expected_return: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    returned = solution_module.name_validation(name)

    assert returned == expected_return
