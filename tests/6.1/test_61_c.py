from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_61 import c_test_data
from tests.utils import get_mocked_print


@pytest.mark.parametrize(
    "guests_seats, expected_output, _",
    c_test_data,
    ids=[i[-1] for i in c_test_data],
)
def test_get_chanses(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    guests_seats: str,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    printed_output = get_mocked_print(
        wrapped_module,
        monkeypatch,
        guests_seats,
    )
    assert printed_output == expected_output
