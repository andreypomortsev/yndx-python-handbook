from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_23 import e_test_data
from tests.utils import assert_equal

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "mock_input_text, expected_output, test_name",
    e_test_data,
    ids=[i[2] for i in e_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    mock_input_text: str,
    expected_output: str,
    test_name: str,
) -> None:
    wrapped_module, _ = setup_environment
    assert_equal(
        wrapped_module,
        monkeypatch,
        mock_input_text,
        expected_output,
    )
