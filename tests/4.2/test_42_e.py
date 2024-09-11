from typing import Callable, Dict, Tuple

import pytest

from tests.data.test_data_42 import e_test_data


@pytest.mark.parametrize(
    "args, kwargs, expected_output, _",
    e_test_data,
    ids=[i[-1] for i in e_test_data],
)
def test_to_string(
    decorated_function: Callable,
    args: Tuple[Tuple[int]],
    kwargs: Dict[str, str],
    expected_output: Tuple[int],
    _: str,
) -> None:
    returned_output = decorated_function(*args, **kwargs)

    assert returned_output == expected_output
