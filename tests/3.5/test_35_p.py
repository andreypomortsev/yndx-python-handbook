from types import ModuleType
from typing import Callable, Optional, Tuple

import pytest

from tests.data.test_data_35 import p_test_data
from tests.utils import assert_equal


@pytest.mark.parametrize(
    "mock_input_texts, files_data, expected_output, _",
    p_test_data,
    ids=[i[-1] for i in p_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    mock_input_texts: str,
    files_data: Tuple[str],
    expected_output: str,
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
) -> None:
    # Извлекаем и очищаем имена файлов
    file_names = mock_input_texts.split("\n")[1:]

    wrapped_module, _ = make_test_files(file_names, files_data)

    assert_equal(
        wrapped_module,
        monkeypatch,
        mock_input_texts,
        expected_output,
    )
