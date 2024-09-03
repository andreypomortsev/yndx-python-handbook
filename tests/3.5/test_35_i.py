import os
from io import StringIO
from types import ModuleType
from typing import Callable, Optional, Set, Tuple, Union

import pytest

from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_35 import i_test_data


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "file_names, mock_input_text, expected_output, _",  # _ - название теста
    i_test_data,
    ids=[i[-1] for i in i_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    file_names: Union[Tuple[str], str],
    mock_input_text: str,
    expected_output: Set[str],
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
    temp_files: str,
) -> None:
    input_file, output_file = file_names

    # Создаем файлы с тестовыми данными для функции
    wrapped_module, file_path = make_test_files(input_file, mock_input_text)

    # Мокаем input()
    mock_input = StringIO("\n".join(file_names) + "\n")
    monkeypatch.setattr("sys.stdin", mock_input)

    wrapped_module.main()

    directory_path = os.path.dirname(file_path)

    # Файл лежит в root дериктории проекта
    answer_path = os.path.join(directory_path, "..", output_file)
    temp_files(answer_path)

    with open(answer_path, "r", encoding="UTF-8") as file:
        actual_output = file.read()

    assert actual_output in expected_output
