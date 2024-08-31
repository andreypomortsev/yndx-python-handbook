import ast
from io import StringIO
from types import ModuleType
from typing import Tuple

import pytest

from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_32 import o_test_data


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_first_open_test(
    setup_environment: Tuple[ModuleType, str], monkeypatch: pytest.MonkeyPatch
):
    wrapped_module, _ = setup_environment

    mock_input_text, expected_output = o_test_data[0][:2]
    mock_input = StringIO(mock_input_text)
    mock_print = StringIO()

    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    # Используем ast.literal_eval вместо eval для преобразования строки
    # в объект Python, так как это более безопасный метод, который не выполняет
    # произвольный код, а только оценивает литералы: списки словари числа etc.
    printed_output = ast.literal_eval(mock_print.getvalue())

    for printed, expected in zip(printed_output, expected_output):
        printed = dict(sorted(printed.items()))
        assert printed == expected


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_second_open_test(
    setup_environment: Tuple[ModuleType, str], monkeypatch: pytest.MonkeyPatch
):
    wrapped_module, _ = setup_environment

    mock_input_text, expected_output = o_test_data[1][:2]
    mock_input = StringIO(mock_input_text)
    mock_print = StringIO()

    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = ast.literal_eval(mock_print.getvalue())

    for printed, expected in zip(printed_output, expected_output):
        printed = dict(sorted(printed.items()))
        assert printed == expected


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_one_digit_zero(
    setup_environment: Tuple[ModuleType, str], monkeypatch: pytest.MonkeyPatch
):
    wrapped_module, _ = setup_environment

    mock_input_text, expected_output = o_test_data[2][:2]
    mock_input = StringIO(mock_input_text)
    mock_print = StringIO()

    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = ast.literal_eval(mock_print.getvalue())

    for printed, expected in zip(printed_output, expected_output):
        printed = dict(sorted(printed.items()))
        assert printed == expected


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_all_digits_with_spaces(
    setup_environment: Tuple[ModuleType, str], monkeypatch: pytest.MonkeyPatch
):
    wrapped_module, _ = setup_environment

    mock_input_text, expected_output = o_test_data[3][:2]
    mock_input = StringIO(mock_input_text)
    mock_print = StringIO()

    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = ast.literal_eval(mock_print.getvalue())

    for printed, expected in zip(printed_output, expected_output):
        printed = dict(sorted(printed.items()))
        assert printed == expected
