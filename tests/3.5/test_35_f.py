import os
from types import ModuleType
from typing import Callable, Optional

import pytest

from tests.constants import TEST_FILE_NAMES
from tests.data.test_data_32 import j_test_data


@pytest.mark.parametrize(
    "mock_input_text, expected_output, _",  # _ - название теста
    j_test_data,
    ids=[i[2] for i in j_test_data],  # Считываем названия тестов
)
def test_input_output(
    mock_input_text: str,
    expected_output: str,
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
    temp_files: str,
) -> None:
    read_data, written_data = TEST_FILE_NAMES["3.5"]["f"]

    wrapped_module, file_path = make_test_files(read_data, mock_input_text)
    wrapped_module.main()

    directory_path = os.path.dirname(file_path)
    answer_path = os.path.join(directory_path, "..", written_data)

    # Добавляем адрес файла для удаления после теста
    temp_files(answer_path)

    with open(answer_path, "r", encoding="UTF-8") as file:
        actual_output = file.read().rstrip()

    assert actual_output == expected_output
