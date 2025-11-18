from typing import Callable, Tuple, Union

import pytest

from tests.data.test_data_41 import i_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    i_test_data,
    ids=[i[-1] for i in i_test_data],
)
def test_month(
    decorated_function: Callable,
    args: Tuple[Union[int, str], str],
    expected_output: str,
    _: str,
) -> None:
    returned_output = decorated_function(*args)

    assert returned_output == expected_output
