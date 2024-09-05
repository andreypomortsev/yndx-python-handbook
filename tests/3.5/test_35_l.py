import os
from io import StringIO
from types import ModuleType
from typing import Callable, List, Optional, Tuple

import pytest

from tests.data.test_data_35 import l_test_data


@pytest.mark.parametrize(
    "file_names, mock_input_text, expected_outputs, _",  # _ - название теста
    l_test_data,
    ids=[i[-1] for i in l_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    file_names: Tuple[str],
    mock_input_text: str,
    expected_outputs: List[str],
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
    temp_files: str,
) -> None:
    input_file, output_files = file_names[0], file_names[1:]

    # Создаем файлы с тестовыми данными для функции
    wrapped_module, file_path = make_test_files(input_file, mock_input_text)

    # Мокаем input()
    mock_input = StringIO("\n".join(file_names) + "\n")
    monkeypatch.setattr("sys.stdin", mock_input)

    wrapped_module.main()

    directory_path = os.path.dirname(file_path)

    for output_file, expected_output in zip(output_files, expected_outputs):
        answer_path = os.path.join(directory_path, "..", output_file)
        temp_files(answer_path)

        with open(answer_path, "r", encoding="UTF-8") as file:
            actual_output = file.read()

        assert actual_output == expected_output
