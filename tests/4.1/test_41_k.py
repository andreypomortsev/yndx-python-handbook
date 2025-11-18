from typing import Callable, List

import pytest

from tests.data.test_data_41 import k_test_data


@pytest.mark.parametrize(
    "arg, expected_output, _",
    k_test_data,
    ids=[i[-1] for i in k_test_data],
)
def test_find_mountains(
    decorated_function: Callable,
    arg: List[int],
    expected_output: List[int],
    _: str,
) -> None:
    returned_output = decorated_function(arg)

    assert returned_output == expected_output
