from types import ModuleType
from typing import Callable, Dict

import pytest

from tests import utils
from tests.conftest import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_53 import j_test_data


@pytest.mark.parametrize(
    "password, kwargs, expected_error, _",
    j_test_data["Errors"],
    ids=[i[-1] for i in j_test_data["Errors"]],
)
def test_password_validation_error(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    password: str,
    kwargs: Dict[str, str | int | Callable[..., bool]],
    expected_error: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(
        solution.password_validation
    )
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    with pytest.raises(Exception) as exc_info:
        decorated_func(password, **kwargs)

    assert expected_error == exc_info.type.__name__


@pytest.mark.parametrize(
    "password, kwargs, expected_return, _",
    j_test_data["Values"],
    ids=[i[-1] for i in j_test_data["Values"]],
)
def test_password_validation(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    password: str,
    kwargs: Dict[str, str | int | Callable[..., bool]],
    expected_return: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(
        solution.password_validation
    )
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned = decorated_func(password, **kwargs)

    assert returned == expected_return
