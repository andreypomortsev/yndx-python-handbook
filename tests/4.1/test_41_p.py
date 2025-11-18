from typing import Any, Callable

import pytest

from tests.data.test_data_41 import p_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    p_test_data,
    ids=[i[-1] for i in p_test_data],
)
def test_is_palindrome(
    decorated_function: Callable,
    args: Any,
    expected_output: bool,
    _: str,
) -> None:
    returned_output = decorated_function(args)

    assert returned_output == expected_output
