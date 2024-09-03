from io import StringIO
from types import ModuleType
from typing import Callable, Optional

import pytest

from tests.constants import MEMORY_LIMIT, TEST_FILE_NAMES, TIME_LIMIT
from tests.data.test_data_35 import t_test_data


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "mock_data_file_in, expected_output, _",
    t_test_data,
    ids=[i[-1] for i in t_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
    mock_data_file_in: bytes,
    expected_output: str,
    _: str,
) -> None:
    input_file = TEST_FILE_NAMES["3.5"]["t"]

    wrapped_module, _ = make_test_files(input_file, mock_data_file_in, "wb")

    # Патчим Output
    mock_stdout = StringIO()
    monkeypatch.setattr("sys.stdout", mock_stdout)

    wrapped_module.main()

    printed_output = mock_stdout.getvalue()

    assert printed_output == expected_output
