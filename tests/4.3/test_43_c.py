from types import ModuleType
from typing import Tuple

import pytest

from tests.constants import RECURSION_ERROR
from tests.data.test_data_43 import c_test_data


@pytest.mark.parametrize(
    "numbers, expected_output, _",
    c_test_data,
    ids=[i[-1] for i in c_test_data],
)
def test_make_equation(
    setup_environment: Tuple[ModuleType, str],
    numbers: Tuple[int],
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    returned_output = wrapped_module.make_equation(*numbers)

    real_calls = wrapped_module.make_equation.call_count
    expected_calls = len(numbers)

    try:
        assert real_calls == expected_calls, RECURSION_ERROR
        assert returned_output == expected_output

    finally:
        # Сбрасываем счетчик вызова функции, независимо от результата теста
        wrapped_module.make_equation.call_count = 0
