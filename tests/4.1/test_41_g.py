from typing import Callable, Tuple

import pytest

from tests.data.test_data_41 import g_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    g_test_data,
    ids=[i[-1] for i in g_test_data],
)
def test_can_eat(
    decorated_function: Callable,
    args: Tuple[Tuple[int]],
    expected_output: bool,
    _: str,
) -> None:
    returned_output = decorated_function(*args)

    assert returned_output == expected_output
