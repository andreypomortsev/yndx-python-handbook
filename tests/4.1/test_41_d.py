from typing import Callable, Tuple, Union

import pytest

from tests.data.test_data_41 import d_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    d_test_data,
    ids=[i[-1] for i in d_test_data],
)
def test_input_output(
    decorated_function: Callable,
    args: Tuple[Union[int, str], str],
    expected_output: str,
    _: str,
) -> None:
    returned_output = decorated_function(*args)

    assert returned_output == expected_output
