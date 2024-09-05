import json
import os
from io import StringIO
from types import ModuleType
from typing import Callable, Dict, List, Optional, Tuple

import pytest

from tests.data.test_data_35 import n_test_data


@pytest.mark.parametrize(
    "file_names, json_data, expected_output, _",
    n_test_data,
    ids=[i[-1] for i in n_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    file_names: Tuple[str],
    json_data: Tuple[List[Dict[str, str]]],
    expected_output: Dict[str, str],
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
) -> None:
    # Создаем файлы с тестовыми данными для функции
    wrapped_module, file_path = make_test_files(file_names, json_data)

    user_input = f"{file_names[0]}\n{file_names[1]}\n"

    # Мокаем input()
    mock_input = StringIO(user_input)
    monkeypatch.setattr("sys.stdin", mock_input)

    wrapped_module.main()

    directory_path = os.path.dirname(file_path)
    answer_path = os.path.join(directory_path, "..", file_names[0])

    with open(answer_path, "r", encoding="UTF-8") as json_file:
        actual_output = json.load(json_file)

    assert actual_output == expected_output
