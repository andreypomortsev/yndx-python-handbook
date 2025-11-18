from typing import Callable, List

import pytest

from tests.data.test_data_41 import h_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    h_test_data,
    ids=[i[-1] for i in h_test_data],
)
def test_fragments(
    decorated_function: Callable,
    args: List[int],
    expected_output: List[List[int]],
    _: str,
) -> None:
    returned_output = decorated_function(args)

    assert returned_output == expected_output
