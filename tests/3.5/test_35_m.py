import json
import os
from io import StringIO
from types import ModuleType
from typing import Any, Callable, Dict, Optional

import pytest

from tests.data.test_data_35 import m_test_data


@pytest.mark.parametrize(
    "file_name, mock_users_input, json_data, expected_output, _",
    m_test_data,
    ids=[i[-1] for i in m_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    file_name: str,
    mock_users_input: str,
    json_data: Dict[Any, Any],
    expected_output: Dict[Any, Any],
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
) -> None:
    # Создаем файлы с тестовыми данными для функции
    wrapped_module, file_path = make_test_files(file_name, json_data)

    user_input = f"{file_name}\n{mock_users_input}"

    # Мокаем input()
    mock_input = StringIO(user_input)
    monkeypatch.setattr("sys.stdin", mock_input)

    wrapped_module.main()

    directory_path = os.path.dirname(file_path)
    answer_path = os.path.join(directory_path, "..", file_name)

    with open(answer_path, "r", encoding="UTF-8") as json_file:
        actual_output = json.load(json_file)

    assert actual_output == expected_output
