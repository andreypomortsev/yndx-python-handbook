from io import StringIO
from types import ModuleType
from typing import Any, Callable, Tuple

import pytest
from _pytest.monkeypatch import MonkeyPatch

from tests import utils
from tests.data.test_data_43 import (test_data_g_a_plus_b,
                                     test_data_g_combine_text,
                                     test_data_g_get_sum_of_ords)


@pytest.mark.parametrize(
    "args, expected_output, _",
    test_data_g_a_plus_b,
    ids=[data[-1] for data in test_data_g_a_plus_b],
)
def test_same_type_a_plus_b(
    monkeypatch: MonkeyPatch,
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
    args: Tuple[int | float, ...],
    expected_output: str,
    _: str,  # Название теста
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.same_type
    def a_plus_b(a: int | float, b: int | float) -> int | float:
        return a + b

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    print(a_plus_b(*args) or "Fail")
    printed_output = mock_print.getvalue()
    assert printed_output == expected_output


@pytest.mark.parametrize(
    "args, expected_output, _",
    test_data_g_combine_text,
    ids=[data[-1] for data in test_data_g_combine_text],
)
def test_same_type_combine_text(
    monkeypatch: MonkeyPatch,
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
    args: Tuple[Any],
    expected_output: str,
    _: str,  # Название теста
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.same_type
    def combine_text(*words) -> str:
        return " ".join(words)

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    print(combine_text(*args) or "Fail")
    printed_output = mock_print.getvalue()
    assert printed_output == expected_output


@pytest.mark.parametrize(
    "args, expected_output, _",
    test_data_g_get_sum_of_ords,
    ids=[data[2] for data in test_data_g_get_sum_of_ords],
)
def test_same_type_get_sum_of_ords(
    monkeypatch: MonkeyPatch,
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
    args: Tuple[Any],
    expected_output: str,
    _: str,  # Название теста
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.same_type
    def get_sum_of_ords(*text) -> int:
        result = 0
        for item in text:
            result += sum(map(ord, item))
        return result

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    print(get_sum_of_ords(*args))
    printed_output = mock_print.getvalue()
    assert printed_output == expected_output
