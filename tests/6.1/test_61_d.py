from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_61 import d_test_data
from tests.utils import get_mocked_print


@pytest.mark.parametrize(
    "line_of_nums, expected_output, _",
    d_test_data,
    ids=[i[-1] for i in d_test_data],
)
def test_geometric_mean(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    line_of_nums: str,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    printed_output = get_mocked_print(
        wrapped_module,
        monkeypatch,
        line_of_nums,
    )
    assert printed_output == expected_output
