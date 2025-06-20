from types import ModuleType
from typing import Any, Callable, Dict, List, Optional

import pytest

from tests.constants import TEST_FILE_NAMES
from tests.data.test_data_35 import o_test_data
from tests.utils import get_mocked_print


@pytest.mark.parametrize(
    "mock_input_text, json_data, expected_output, _",
    o_test_data,
    ids=[i[-1] for i in o_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    mock_input_text: str,
    json_data: List[Dict[str, Any]],
    expected_output: str,
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
) -> None:
    file_name = TEST_FILE_NAMES["3.5"]["o"]

    wrapped_module, _ = make_test_files(file_name, json_data)

    printed_output = get_mocked_print(
        wrapped_module,
        monkeypatch,
        mock_input_text,
    )
    assert printed_output == expected_output
