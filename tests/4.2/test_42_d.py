from typing import Callable, Tuple

import pytest

from tests.data.test_data_42 import d_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    d_test_data,
    ids=[i[-1] for i in d_test_data],
)
def test_month(
    decorated_function: Callable,
    args: Tuple[Tuple[int]],
    expected_output: Tuple[int],
    _: str,
) -> None:
    returned_output = decorated_function(*args)

    assert returned_output == expected_output
