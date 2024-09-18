from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_43 import a_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    a_test_data,
    ids=[i[-1] for i in a_test_data],
)
def test_recursive_sum(
    setup_environment: Tuple[ModuleType, str],
    args: Tuple[int],
    expected_output: int,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    returned_output = wrapped_module.recursive_sum(*args)

    try:
        assert wrapped_module.recursive_sum.call_count == len(args), (
            "Функция `recursive_sum` должна быть реализована "
            "при помощи рекурсии."
        )
        assert returned_output == expected_output

    finally:
        # Сбрасываем счетчик вызова функции, независимо от результата теста
        wrapped_module.recursive_sum.call_count = 0
