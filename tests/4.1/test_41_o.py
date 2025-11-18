from typing import Any, Callable, Dict

import pytest

from tests.data.test_data_41 import o_test_data


@pytest.mark.parametrize(
    "arg, expected_output, _",
    o_test_data,
    ids=[i[-1] for i in o_test_data],
)
def test_get_dict(
    decorated_function: Callable,
    arg: str,
    expected_output: Dict[str, Any],
    _: str,
) -> None:
    returned_output = decorated_function(arg)

    assert returned_output == expected_output
