from typing import Callable, List, Tuple

import pytest

from tests.data.test_data_41 import l_test_data


@pytest.mark.parametrize(
    "arg, expected_output, _",
    l_test_data,
    ids=[i[-1] for i in l_test_data],
)
def test_find_mountains_2(
    decorated_function: Callable,
    arg: List[List[int]],
    expected_output: Tuple[Tuple[int]],
    _: str,
) -> None:
    returned_output = decorated_function(arg)

    assert returned_output == expected_output
