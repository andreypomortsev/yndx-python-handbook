from io import StringIO
from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_35 import r_test_data


@pytest.mark.parametrize(
    "mock_input_text, mock_file_size, expected_output, _",
    r_test_data,
    ids=[i[-1] for i in r_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    mock_input_text: str,
    mock_file_size: int,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    # Патчим Input
    mock_stdin = StringIO(mock_input_text)
    monkeypatch.setattr("sys.stdin", mock_stdin)

    # Патчим Output
    mock_stdout = StringIO()
    monkeypatch.setattr("sys.stdout", mock_stdout)

    # Для решений через os.path.getsize
    monkeypatch.setattr("os.path.getsize", lambda _: mock_file_size)

    wrapped_module.main()
    printed_output = mock_stdout.getvalue().rstrip("\n")

    assert printed_output == expected_output
