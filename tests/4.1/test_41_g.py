from typing import Callable, List, Tuple

import pytest

from tests.data.test_data_41 import g_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    g_test_data,
    ids=[i[-1] for i in g_test_data],
)
def test_max2D(
    decorated_function: Callable,
    args: Tuple[List[int]],
    expected_output: int,
    _: str,
) -> None:
    returned_output = decorated_function(args)

    assert returned_output == expected_output
