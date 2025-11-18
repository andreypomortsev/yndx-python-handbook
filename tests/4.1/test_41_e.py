from typing import Callable, Tuple

import pytest

from tests.data.test_data_41 import e_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    e_test_data,
    ids=[i[-1] for i in e_test_data],
)
def test_clicker(
    decorated_function: Callable,
    args: Tuple[str],
    expected_output: str,
    _: str,
) -> None:
    result = ""
    get_count, click = decorated_function
    for name in args:
        if name == "get_count":
            result += str(get_count())
        else:
            click()
    assert result == expected_output
