from typing import Callable, List, Union

import pytest

from tests.data.test_data_41 import d_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    d_test_data,
    ids=[i[-1] for i in d_test_data],
)
def test_month(
    decorated_function: Callable,
    args: List[Union[int, float]],
    expected_output: List[Union[int, float]],
    _: str,
) -> None:
    initial_list = list(args)
    returned_output = decorated_function(args)

    assert initial_list == args
    assert returned_output == expected_output
