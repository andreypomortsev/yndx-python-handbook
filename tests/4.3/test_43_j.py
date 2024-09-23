from types import ModuleType
from typing import List, Tuple, TypeVar

import pytest

from tests.data.test_data_43 import j_test_data

T = TypeVar("T")


@pytest.mark.parametrize(
    "deep_list, expected_output, _",
    j_test_data,
    ids=[i[-1] for i in j_test_data],
)
def test_make_linear(
    setup_environment: Tuple[ModuleType, str],
    deep_list: List[T],
    expected_output: List[T],
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    returned_output = wrapped_module.make_linear(deep_list)

    assert returned_output == expected_output
