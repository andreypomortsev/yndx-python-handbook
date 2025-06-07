from types import ModuleType
from typing import Set, Tuple

import pytest

from tests.data.test_data_32 import c_test_data
from tests.utils import get_mocked_print


@pytest.mark.parametrize(
    "mock_input_text, expected_output, _",  # _ - название теста
    c_test_data,
    ids=[i[-1] for i in c_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    mock_input_text: str,
    expected_output: Set[str],
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    printed_output = get_mocked_print(
        wrapped_module,
        monkeypatch,
        mock_input_text,
    )
    printed_set = set(printed_output.rstrip("\n").split("\n"))
    assert printed_set == expected_output
