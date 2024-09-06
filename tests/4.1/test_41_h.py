from typing import Any, Callable

import pytest

from tests.data.test_data_41 import h_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    h_test_data,
    ids=[i[-1] for i in h_test_data],
)
def test_input_output(
    decorated_function: Callable,
    args: Any,
    expected_output: bool,
    _: str,
) -> None:
    returned_output = decorated_function(args)

    assert returned_output == expected_output
