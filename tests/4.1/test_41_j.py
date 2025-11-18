from typing import Callable, Tuple

import pytest

from tests.data.test_data_41 import j_test_data


@pytest.mark.parametrize(
    "arg, expected_output, _",
    j_test_data,
    ids=[i[-1] for i in j_test_data],
)
def test_split_numbers(
    decorated_function: Callable,
    arg: str,
    expected_output: Tuple[int],
    _: str,
) -> None:
    returned_output = decorated_function(arg)

    assert returned_output == expected_output
