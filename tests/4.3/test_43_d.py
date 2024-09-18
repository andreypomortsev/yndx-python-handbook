from io import StringIO
from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests import utils
from tests.data.test_data_43 import (test_data_d_a_plus_b,
                                     test_data_d_get_letters,
                                     test_data_d_get_sum_of_ords)


@pytest.mark.parametrize(
    "args, expected_output, _",
    test_data_d_a_plus_b,
    ids=[data[2] for data in test_data_d_a_plus_b],
)
def test_answer_a_plus_b(
    monkeypatch: pytest.MonkeyPatch,
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
    args: Tuple[int],
    expected_output: str,
    _: str,  # Название теста
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.answer
    def a_plus_b(a, b):
        return a + b

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    print(a_plus_b(*args))
    printed_output = mock_print.getvalue()
    assert printed_output == expected_output


@pytest.mark.parametrize(
    "args, expected_output, _",
    test_data_d_get_letters,
    ids=[data[2] for data in test_data_d_get_letters],
)
def test_answer_get_letters(
    monkeypatch: pytest.MonkeyPatch,
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
    args: Tuple[str],
    expected_output: str,
    _: str,  # Название теста
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.answer
    def get_letters(text: str) -> str:
        return "".join(sorted(set(filter(str.isalpha, text.lower()))))

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    print(get_letters(*args))
    printed_output = mock_print.getvalue()
    assert printed_output == expected_output


@pytest.mark.parametrize(
    "args, expected_output, _",
    test_data_d_get_sum_of_ords,
    ids=[data[2] for data in test_data_d_get_sum_of_ords],
)
def test_answer_get_sum_of_ords(
    monkeypatch: pytest.MonkeyPatch,
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
    args: Tuple[str],
    expected_output: str,
    _: str,  # Название теста
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.answer
    def get_sum_of_ords(text: str) -> int:
        return sum(map(ord, text))

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    print(get_sum_of_ords(*args))
    printed_output = mock_print.getvalue()
    assert printed_output == expected_output
