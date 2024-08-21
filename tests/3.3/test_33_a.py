import math
from math import pow
from types import CodeType

import pytest

from tests.data.test_data_33 import a_test_data

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "variables, expected_output, _",  # _ - название теста
    a_test_data,
    ids=[i[2] for i in a_test_data],  # Считываем названия тестов
)
def test_comprehensions(
    setup_environment_comprehension: CodeType,
    variables: dict,
    expected_output: str,
    _: str,
) -> None:
    # Считываем код для проверки и компилируем его из строки в код
    to_execute = setup_environment_comprehension
    safe_globals = {
        "__builtins__": {"math.pow": math.pow, "pow": pow, "range": range}
    }
    printed_output = eval(to_execute, safe_globals, variables)

    assert printed_output == expected_output
