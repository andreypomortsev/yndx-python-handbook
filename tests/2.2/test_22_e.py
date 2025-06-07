from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_22 import e_test_data
from tests.utils import get_mocked_print


@pytest.mark.parametrize(
    "mock_input_text, expected_output, _",  # _ - название теста
    e_test_data,
    ids=[i[-1] for i in e_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    mock_input_text: str,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    printed_output = get_mocked_print(
        wrapped_module,
        monkeypatch,
        mock_input_text,
    )
    assert (
        printed_output == expected_output or printed_output in expected_output
    )
