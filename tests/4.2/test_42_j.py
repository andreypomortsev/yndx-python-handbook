from typing import Callable, Dict, Tuple

import pytest

from tests.data.test_data_42 import j_test_data


@pytest.mark.parametrize(
    "text, replacements, expected_output, _",
    j_test_data,
    ids=[i[-1] for i in j_test_data],
)
def test_secret_replace(
    decorated_function: Callable,
    text: str,
    replacements: Dict[str, Tuple[str]],
    expected_output: Tuple[int],
    _: str,
) -> None:
    returned_output = decorated_function(text, **replacements)

    assert returned_output == expected_output
