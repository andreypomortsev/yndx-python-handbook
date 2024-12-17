from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_61 import a_test_data
from tests.utils import assert_equal


@pytest.mark.parametrize(
    "real_number, expected_output, _",
    a_test_data,
    ids=[i[-1] for i in a_test_data],
)
def test_calculate_expression(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    real_number: int | float,
    expected_output: float,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    assert_equal(
        wrapped_module,
        monkeypatch,
        str(real_number),
        str(expected_output) + "\n",
    )
