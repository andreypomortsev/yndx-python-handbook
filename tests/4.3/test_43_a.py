from typing import Callable, Tuple

import pytest

from tests.data.test_data_43 import a_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    a_test_data,
    ids=[i[-1] for i in a_test_data],
)
def test_input_output(
    decorated_function: Callable,
    args: Tuple[Tuple[int]],
    expected_output: Tuple[int],
    _: str,
) -> None:
    returned_output = decorated_function(*args)

    assert returned_output == expected_output
