import os
from io import StringIO
from types import ModuleType
from typing import Callable, Optional

import pytest

from tests.constants import TEST_FILE_NAMES
from tests.data.test_data_35 import s_test_data


@pytest.mark.parametrize(
    "mock_input_text, mock_data_file_in, expected_output, _",
    s_test_data,
    ids=[i[-1] for i in s_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
    temp_files: str,
    mock_input_text: str,
    mock_data_file_in: str,
    expected_output: str,
    _: str,
) -> None:
    input_file, output_file = TEST_FILE_NAMES["3.5"]["s"]

    wrapped_module, file_path = make_test_files(input_file, mock_data_file_in)

    # Патчим Input
    mock_stdin = StringIO(mock_input_text)
    monkeypatch.setattr("sys.stdin", mock_stdin)

    wrapped_module.main()

    # Добавляем файл созданный тестируемым файлом в список на удаление
    directory_path = os.path.dirname(file_path)
    answer_path = os.path.join(directory_path, "..", output_file)
    temp_files(answer_path)

    with open(output_file, "r", encoding="UTF-8") as file:
        written_output = file.read()

    assert written_output == expected_output
