from typing import Callable

import pytest

from tests.data.test_data_41 import c_test_data


@pytest.mark.parametrize(
    "arg, expected_output, _",
    c_test_data,
    ids=[i[-1] for i in c_test_data],
)
def test_input_output(
    decorated_function: Callable,
    arg: int,
    expected_output: int,
    _: str,
) -> None:
    returned_output = decorated_function(arg)

    assert returned_output == expected_output
