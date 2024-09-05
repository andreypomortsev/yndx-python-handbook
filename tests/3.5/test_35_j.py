from types import ModuleType
from typing import Callable, Optional, Set

import pytest

from tests.data.test_data_35 import j_test_data
from tests.utils import assert_equal


@pytest.mark.parametrize(
    "file_name, input_text, lines_to_read, expected_output, _",
    j_test_data,
    ids=[i[-1] for i in j_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    file_name: str,
    input_text: str,
    lines_to_read: str,
    expected_output: Set[str],
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
) -> None:

    # Создаем файлы с тестовыми данными для функции
    wrapped_module, _ = make_test_files(file_name, input_text)

    # Создаем input()
    mock_input_text = f"{file_name}\n{lines_to_read}\n"

    assert_equal(
        wrapped_module,
        monkeypatch,
        mock_input_text,
        expected_output,
    )
