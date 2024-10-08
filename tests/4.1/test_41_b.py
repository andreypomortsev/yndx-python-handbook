from typing import Callable, Tuple

import pytest

from tests.data.test_data_41 import b_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    b_test_data,
    ids=[i[-1] for i in b_test_data],
)
def test_gcd(
    decorated_function: Callable,
    args: Tuple[int],
    expected_output: str,
    _: str,
) -> None:
    returned_output = decorated_function(*args)

    assert returned_output == expected_output
