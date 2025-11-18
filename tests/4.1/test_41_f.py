from typing import Callable, Tuple

import pytest

from tests.data.test_data_41 import f_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    f_test_data,
    ids=[i[-1] for i in f_test_data],
)
def test_month(
    decorated_function: Callable,
    args: Tuple[Tuple[str, int]],
    expected_output: str,
    _: str,
) -> None:
    move, game_over = decorated_function
    for arg in args:
        move(*arg)
    printed_output = game_over()
    assert printed_output == expected_output
