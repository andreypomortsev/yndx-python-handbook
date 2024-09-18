from types import ModuleType
from typing import Callable

import pytest

from tests import utils
from tests.data.test_data_43 import (test_data_e_a_plus_b,
                                     test_data_e_get_letters,
                                     test_data_e_get_sum_of_ords)


def test_answer_a_plus_b(
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.result_accumulator
    def a_plus_b(a: int, b: int) -> int:
        return a + b

    for args, kwargs, expected_output, _ in test_data_e_a_plus_b:
        returned_output = a_plus_b(*args, **kwargs)
        assert returned_output == expected_output


def test_answer_get_letters(
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.result_accumulator
    def get_letters(text: str) -> str:
        return "".join(sorted(set(filter(str.isalpha, text.lower()))))

    for args, kwargs, expected_output, _ in test_data_e_get_letters:
        returned_output = get_letters(*args, **kwargs)
        assert returned_output == expected_output


def test_answer_get_sum_of_ords(
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    @solution_module.result_accumulator
    def get_sum_of_ords(text: str) -> int:
        return sum(map(ord, text))

    for args, kwargs, expected_output, _ in test_data_e_get_sum_of_ords:
        returned_output = get_sum_of_ords(*args, **kwargs)
        assert returned_output == expected_output
