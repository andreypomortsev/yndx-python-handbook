from types import ModuleType
from typing import Callable, Dict

import pytest

from tests import utils
from tests.conftest import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_53 import i_test_data


@pytest.mark.parametrize(
    "user_details, expected_error, _",
    i_test_data["Errors"],
    ids=[i[-1] for i in i_test_data["Errors"]],
)
def test_user_validation_error(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    user_details: Dict[str, str],
    expected_error: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    with pytest.raises(Exception) as exc_info:
        solution_module.user_validation(**user_details)

    assert expected_error == exc_info.type.__name__


@pytest.mark.parametrize(
    "user_details, expected_return, _",
    i_test_data["Values"],
    ids=[i[-1] for i in i_test_data["Values"]],
)
def test_user_validation(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    user_details: Dict[str, str],
    expected_return: Dict[str, str],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.user_validation)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned = decorated_func(**user_details)

    assert returned == expected_return
