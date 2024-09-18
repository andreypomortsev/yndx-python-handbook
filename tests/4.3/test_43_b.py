from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_43 import b_test_data


@pytest.mark.parametrize(
    "number, expected_output, _",
    b_test_data,
    ids=[i[-1] for i in b_test_data],
)
def test_recursive_digit_sum(
    setup_environment: Tuple[ModuleType, str],
    number: int,
    expected_output: int,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    returned_output = wrapped_module.recursive_digit_sum(number)

    real_calls = wrapped_module.recursive_digit_sum.call_count
    expected_calls = len(str(number))

    try:
        assert real_calls == expected_calls, (
            "Функция `recursive_digit_sum` должна быть реализована "
            "при помощи рекурсии."
        )
        assert returned_output == expected_output

    finally:
        # Сбрасываем счетчик вызова функции, независимо от результата теста
        wrapped_module.recursive_digit_sum.call_count = 0
