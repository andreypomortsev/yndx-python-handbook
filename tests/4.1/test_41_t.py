from typing import Callable, Tuple

import pytest

from tests.data.test_data_41 import t_test_data


@pytest.mark.parametrize(
    "arg, expected_output, _",
    t_test_data,
    ids=[i[-1] for i in t_test_data],
)
def test_roman(
    decorated_function: Callable,
    arg: Tuple[int],
    expected_output: str,
    _: str,
) -> None:
    returned_output = decorated_function(*arg)

    assert returned_output == expected_output
